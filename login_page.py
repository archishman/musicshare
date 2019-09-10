from flask import Blueprint, render_template, abort, request, redirect, g, url_for
from jinja2 import TemplateNotFound
from config import *
from tools import random_string
import requests
import json
from urllib.parse import quote

login_page = Blueprint('login_page', __name__,
                        template_folder='templates')
auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "state": random_string(20),
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}
@login_page.route('/')
def show():    
    try:
        return render_template('login_page.html', auth_url=url_for('login_page.authorize'))
    except TemplateNotFound:
        abort(404)


@login_page.route('/spotify_authorize', methods=['GET', 'POST'])
def authorize():
    # Auth Step 1: Authorization
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


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

    return redirect("/me?access_token={}&refresh_token={}".format(access_token, refresh_token))


    