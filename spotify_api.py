import requests
import base64

class SpotifyApi(object):
    
    def __init__(self, sptfy_id, sptfy_secret):
        tocken_url = "https://accounts.spotify.com/api/token"
        
        creds = f"{sptfy_id}:{sptfy_secret}"
        
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
        
        self.access_token = tocken_responce['access_token']
        
    def get_song_info(self, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks" + "?" + "market=US"
        
        method = "POST"
        
        request_header = {
            "Authorization": f"Bearer {self.access_token}"  
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
        
        return song_info
        
    def get_artist(self, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        method = "GET"
        request_header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=request_header)
        results = response.json();
        
        artist_info = results['name']
        
        return artist_info

