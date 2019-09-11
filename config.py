#  Client Keys
CLIENT_ID = "8f5fc2a9fe0248bd8c5cfea81e026a7e"
CLIENT_SECRET = "c567661ca1734a86baa07b5542d26840"
PORT = 8080
# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)
FIREBASE_URL = "https://musicshare-ca88e.firebaseio.com/"
# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
REDIRECT_URI = "http://localhost:8080/callback/"
SCOPE = "user-library-modify  user-library-read  app-remote-control  streaming  playlist-read-private  playlist-read-collaborative  playlist-modify-public  playlist-modify-private  user-follow-modify  user-follow-read  user-read-recently-played  user-top-read  user-read-private  user-read-email  user-read-currently-playing  user-read-playback-state  user-modify-playback-state"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()