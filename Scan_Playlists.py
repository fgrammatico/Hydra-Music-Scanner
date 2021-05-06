import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import json
import boto3

SPOTIPY_CLIENT_ID=os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET=os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_USER=os.environ['SPOTIPY_USER']
AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
clientDynamo = boto3.client('dynamodb')

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def scan_playlists(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_USER):
    ''' Get Playlists for the user'''
    playlists = sp.user_playlists(SPOTIPY_USER)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            playlistName = playlist['name']
            playlistID = playlist['id']
            response = clientDynamo.get_item(
                Key = {
                    playlistID : {
                        'S' : '35U4PXL3W3XIkAjEUdhr36',
                        },
                        },
                TableName = playlistName,
                )
            # print (playlistName + ' ' + playlistID)
            print (response)

        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

scan_playlists(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_USER)    