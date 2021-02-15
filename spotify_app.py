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
          

@app.route('/')

def run():
    artist_id = random.choice(artist)
    song_info = spotify_api.get_song_info(artist_id)
    return render_template(
        "index.html", 
        len = len(song_info), 
        len2 = len(song_info[0]),
        song_info = song_info,
        artist_name = spotify_api.get_artist(artist_id)
    )
        
@app.route('/artist', methods =["GET", "POST"])

def artist_search():
    if request.method == "POST": 
       name = request.form.get("a_name")                        # get's artist name form html form
       artist_id = spotify_api.get_artist_id(name)              # pass in artist name and gets artist id
       
    else:   
        artist_id = random.choice(artist)                       # randomly choose an artist
        
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
        
        if(len(song_info) > 0):
            artist_len = len(song_info[0])
        else:
            artist_len = 0
            
        return render_template(
            "index.html", 
            len = len(song_info),                               # array length 
            len2 = artist_len,                                  # array length for artists
            song_info = song_info,                              # array
            artist_name = spotify_api.get_artist(artist_id)     # gets artist's name
        )
        
        
@app.route('/lyrics/<song_name>/<artist_name>')

def lyrics(song_name, artist_name):
    artist_name = artist_name[14:]
    print(artist_name)
    try:
        lyrics = spotify_api.get_lyrics(song_name, artist_name)
    except:
        lyrics = "Opps no lyrics found..!!"
    
    return{
        'Lyrics' : lyrics
    }

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)