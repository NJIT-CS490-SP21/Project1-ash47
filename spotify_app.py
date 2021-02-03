from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import os
import random
import requests
import base64

app = Flask(__name__)

load_dotenv(find_dotenv())

tocken_url = "https://accounts.spotify.com/api/token"

creds = f"{os.getenv('sptfy_id')}:{os.getenv('sptfy_sectret')}"

client_creds = base64.b64encode(creds.encode())

method = "POST"

tocken_data = {
    "grant_type": "client_credentials"
}

tocken_header = {
    "Authorization": f"Basic {client_creds.decode()}"    
}

r = requests.post(tocken_url, data=tocken_data, headers=tocken_header)
tocken_responce = r.json()

access_token = tocken_responce['access_token']

artist = ['4YRxDV8wJFPHPTeXepOstw', 
          '4Ai0pGz6GhQavjzaRhPTvz', 
          '1dVygo6tRFXC8CSWURQJq2']

artist_uri = random.choice(artist)

url = f"https://api.spotify.com/v1/artists/{artist_uri}/top-tracks" + "?" + "market=US"

method = "POST"

request_header = {
    "Authorization": f"Bearer {access_token}"  
}

response = requests.get(url, headers=request_header)
results = response.json();

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
