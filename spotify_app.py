from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv, find_dotenv
import os
import random
import spotify_api

app = Flask(__name__)

load_dotenv(find_dotenv())

# artist list: [Arijit Singh, Armaan Malik, A.R. Rahman]

artist = ['4YRxDV8wJFPHPTeXepOstw', 
          '4IKVDbCSBTxBeAsMKjAuTs', 
          '1mYsTxnqsietFxj1OgoGbG']
          
# made a spotify_api object and passed client id and secreat
# authorization token is generated automatically

spotify_api = spotify_api.SpotifyApi(os.getenv('sptfy_id'), os.getenv('sptfy_sectret'))

@app.route('/', methods =["GET", "POST"])

def run():
    
    # if a post request is made we will use user input data
    # else we will use harcoded randomized data
    
    if request.method == "POST": 
       name = request.form.get("a_name")                        # get's artist name form html form
       artist_id = spotify_api.get_artist_id(name)              # pass in artist name and gets artist id
       
    else:   
        artist_id = random.choice(artist)                       # randomly choose an artist
        
    # This if statement handels error case
    # If an error code is returned, then passes error msg to html form and use random artist to get top tracks
    # else uses user picked artist to get top tracks
        
    if(isinstance(artist_id, int) or artist_id == ''):
        artist_id = random.choice(artist)                       # randomly choose an artist
        song_info = spotify_api.get_song_info(artist_id)        # gets artist info as an array (random aritst)
        
        return render_template(
            "index.html",
            err_msg = True,                                     # error message
            len = len(song_info),                               # array length 
            len2 = len(song_info[0]),                           # array length for artists
            song_info = song_info,                              # array
            artist_name = spotify_api.get_artist(artist_id)     # gets artist's name
        )
    else:
        song_info = spotify_api.get_song_info(artist_id)        # gets artist info as an array (user picked aritst)
        return render_template(
            "index.html", 
            len = len(song_info),                               # array length 
            len2 = len(song_info[0]),                           # array length for artists
            song_info = song_info,                              # array
            artist_name = spotify_api.get_artist(artist_id)     # gets artist's name
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
