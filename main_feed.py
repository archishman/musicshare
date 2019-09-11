from flask import Blueprint, url_for, render_template, abort, request, redirect, g
from jinja2 import TemplateNotFound
from config import *
from tools import random_string
import requests
import json
from urllib.parse import quote

main_feed = Blueprint('main_feed', __name__,
                        template_folder='templates')

@main_feed.route('/feed', methods=['GET'])
def show():
    access_token = request.args.get('access_token')
    refresh_token = request.args.get('refresh_token')
    if access_token == None:
        return redirect('/spotify_authorize')
    else:
        authorization_header = {"Authorization": "Bearer {}".format(access_token)}
        user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
        profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
        profile_data = json.loads(profile_response.text)
        user_id = profile_data['id']
        posts = []
        followers = json.loads(requests.get('{}/people/{}/Following.json'.format(FIREBASE_URL, user_id)))
        for follower in followers:
            p =  json.loads(requests.get('{}/people/{}/Posts.json'.format(FIREBASE_URL, follower)))
            posts = posts + p        
        return render_template('main_feed.html', posts=posts)
    
@main_feed.route('/create_post') #SECURITY FLAWWWWWWWWWW FIX ASAP
def create_post():
    text = request.args.get('caption')
    spotify_id = request.args.get('song_id')
    poster = request.args.get('user_id')
    name = time.time()
    firebase_update_payload = {name: {'caption': text, 'spotify_id': spotify_id}}
    update_user_token = requests.patch('{}/people/{}/posts.json'.format(FIREBASE_URL, user_id), data=json.dumps(firebase_update_payload))

    