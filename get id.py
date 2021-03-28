import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import json

SPOTIPY_CLIENT_ID=os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET=os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_USER=os.environ['SPOTIPY_USER']

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists(SPOTIPY_USER)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(playlist['name'])
        print(playlist['id'])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
    