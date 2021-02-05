from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import os
import random
import spotify_api

app = Flask(__name__)

load_dotenv(find_dotenv())

artist = ['4YRxDV8wJFPHPTeXepOstw', 
          '4Ai0pGz6GhQavjzaRhPTvz', 
          '1dVygo6tRFXC8CSWURQJq2']

spotify_api = spotify_api.SpotifyApi(os.getenv('sptfy_id'), os.getenv('sptfy_sectret'))

@app.route('/')

def hello_world():
    artist_id = random.choice(artist)
    song_info = spotify_api.get_song_info(artist_id)
    return render_template(
        "index.html", 
        len = len(song_info), 
        len2 = len(song_info[0]),
        song_info = song_info,
        artist_name = spotify_api.get_artist(artist_id)
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
