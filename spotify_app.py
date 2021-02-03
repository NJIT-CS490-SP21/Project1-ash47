import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import os
import random

app = Flask(__name__)

load_dotenv(find_dotenv())

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=os.getenv('sptfy_id'),client_secret=os.getenv('sptfy_sectret')))

artist = ['spotify:artist:4YRxDV8wJFPHPTeXepOstw', 
          'spotify:artist:4Ai0pGz6GhQavjzaRhPTvz', 
          'spotify:artist:1dVygo6tRFXC8CSWURQJq2']

artist_uri = random.choice(artist)

results = spotify.artist_top_tracks(artist_uri)

song_info = []

count = 0

for track in results['tracks']:
    song_info.append([[]])
    for i in range (len(track['artists'])):
        song_info[count][0].append(track['artists'][i]['name'])
    song_info[count].append(track['name'])
    song_info[count].append(track['preview_url'])
    song_info[count].append(track['album']['images'][0]['url'])
    count += 1

@app.route('/')

def hello_world():
    return render_template(
        "index.html", 
        len = len(song_info), 
        len2 = len(song_info[0]),
        song_info = song_info
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)