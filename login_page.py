from flask import Blueprint, render_template, abort, request, redirect, g, url_for
from jinja2 import TemplateNotFound
from config import *
from tools import random_string
import requests
import json
import time
from urllib.parse import quote

login_page = Blueprint('login_page', __name__,
                        template_folder='templates')

@login_page.route('/')
def show():    
    try:
        return render_template('login_page.html', auth_url=url_for('login_page.authorize'), main_feed = url_for('main_feed.show')
        , login_page = url_for('login_page.show'))
    except TemplateNotFound:
        abort(404)


@login_page.route('/spotify_authorize', methods=['GET', 'POST'])
def authorize():
    # Auth Step 1: Authorization
    redirect_uri = request.args.get('redirect_uri', default=REDIRECT_URI)
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": SCOPE,
        "state": random_string(20),
        # "show_dialog": SHOW_DIALOG_str,
        "client_id": CLIENT_ID
    }
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    print('Monk: ' + auth_url)
    return redirect(auth_url)
@login_page.route('/refresh_token', methods=['GET'])
def refresh():    
    access_token = request.args['access_token']
    firebase_response = json.loads(requests.get('{}/tokens/{}.json'.format(FIREBASE_URL, access_token)).text)
    expiry = firebase_response.get('expiry')
    refresh_token = firebase_response.get('refresh_token')
    if int(expiry) >= int(time.time()):
        code_payload = {
        "grant_type": "refresh_token",
        "refresh_token": str(refresh_token),
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        }
        spotify_response_data = json.loads(requests.post(SPOTIFY_TOKEN_URL, data=code_payload).text)
        access_token = spotify_response_data["access_token"]
        refresh_token = spotify_response_data["refresh_token"]
        token_type = spotify_response_data["token_type"]
        expires_in = spotify_response_data["expires_in"]
        expiry_time = int(time.time()) + expires_in - 300
        authorization_header = {"Authorization": "Bearer {}".format(access_token)}
        user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
        profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
        profile_data = json.loads(profile_response.text)
        user_id = profile_data['id']
        firebase_update_payload = {'user': user_id, 'refresh_token': refresh_token, 'expiry': expiry_time}
        update_user_token = requests.patch('{}/tokens/{}.json'.format(FIREBASE_URL, access_token), data=json.dumps(firebase_update_payload))
        return redirect("/me?access_token={}&refresh_token={}".format(access_token, refresh_token))



@login_page.route('/callback/')
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]
    expiry_time = int(time.time()) + expires_in - 300
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    user_id = profile_data['id']
    firebase_update_payload = {'user': user_id, 'refresh_token': refresh_token, 'expiry': expiry_time}
    update_user_token = requests.patch('{}/tokens/{}.json'.format(FIREBASE_URL, access_token), data=json.dumps(firebase_update_payload))

#   return redirect("/me?access_token={}&refresh_token={}".format(access_token, refresh_token))
    return redirect("/feed?access_token={}&refresh_token={}".format(access_token, refresh_token))