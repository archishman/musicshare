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
        return render_template('main_feed.html', profile_data=profile_data)