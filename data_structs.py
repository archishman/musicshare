class Person:
    def __init__(self, spotify_uri, name, join_date, picture, posts, followers, favorites):
        self._spotify_id = spotify_uri
        self._name = name
        self._join_date = join_date
        self._picture = picture
        self._posts = posts
        self._followers = followers
        self._favorites = favorites

class Post:
    def __init__(self, spotify_id_list, text, pictures, comments, likes):
        self._spotify_id_list = spotify_id_list
        self._text = text
        self._pictures = pictures
        self._comments = comments
        self._likes = likes

class Comment:
    def __init__(self, text, song):
        self._text = text
        self._song = song