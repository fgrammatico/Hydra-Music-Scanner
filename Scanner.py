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
        pl_id = playlist['uri']
        offset = 0
        while True:
            response = sp.playlist_items(pl_id,offset=offset,fields='items.track.id,total',additional_types=['track'])
            if len(response['items']) == 0:
                break
            # Items is the uri of each song in the playlist
            pprint (response['items'])
            pprint (playlist['uri'])
            pprint (playlist['name'])
            # original string print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))    
            offset = offset + len(response['items'])
            print(offset, "/", response['total'])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
    