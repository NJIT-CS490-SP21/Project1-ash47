# Project-1 Spotify lookup
Project 1 creates Music discovery app that uses Spotify API to dynamically fetch data form Spotify libraries to show top tracks of an Artist. The user will have option to pick an artist through a search bar on page. In case an artist is not picked the page will load top tracks for one of the three pre-selected artists. 

## technologies, frameworks, libraries, and APIs
<details>
  <summary><b>Platform</b></summary>
  <br>
  This project is primarily made on amazons’ AWS cloud9 service. Cloud9 is a cloud-based IDE that lets us write, run, and debug out code just with a browser. And because it is a cloud-based service it makes it easy for us share our work.
</details>

<details>
  <summary><b>Frame work</b></summary>
  <br>
  For Project 1 we are using Flask framework. Flask is a web framework, that provide us with tools, libraries and technologies that allow us to build and setup a web application. 

</details>

<details>
  <summary><b>Libraries</b></summary>

  ### Flask:
  ```python
  from flask import Flask, render_template, request, redirect
  ```
  * Render_template: Flask configures jinj2 template automatically using [grander_templete()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template) method.
  * request: request is used to make HTTP GET and POST requests
  * redirect: [redirect()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.redirect) is used to redirect a user to different endpoint.

  ### Dotenv:
  ```python
  from dotenv import load_dotenv, find_dotenv
  ```
  Dotenv library is going to be used for calling environment variables stored in `.env` file 
  * `load_dotenv` is use to load environment variable.
  * `find_dotenv()` can be used to find `.env` file

  ### Requests:
  ```python
  import requests
  ```

  Requests allows us to easily send HTTP requests.

  Example:
  ```python
  requests.post(tocken_url, data=tocken_data, headers=tocken_header)
  ```

  ### Base64:
  ```python
  import base64
  ```
  Base64 is used for RFC 3548 encoding, for URLs and HTTP POST requests.
  Example:
  ```python
  base64.b64encode(creds.encode())
  ```

  ### urllib.parse.urlencode:
  ```python
  from urllib.parse import urlencode
  ```
  [urllib.parse.urlencode()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode) is used for generating the query string of a URL or data for a POST request
</details>

<details>
  <summary><b>APIs</b></summary>
  <br>
  
  ### 1. [Token](https://developer.spotify.com/documentation/general/guides/authorization-guide/)
  
  + *This API is used to get an access token using client id and client secret.*
  
  ### 2. [Get an Artist's Top Tracks](https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-an-artists-top-tracks)
  
  + *Get spotify catalog information about an artist's top tracks using artist id and country.*
  
  ### 3. [Get an Artist](https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-an-artist)
  
  + *Get Spotify catalog information for a single artist identified by their unique Spotify ID.*
  
  ### 4. [Search API](https://developer.spotify.com/documentation/web-api/reference/#category-search)
  
  + *Get Spotify Catalog information about albums, artists, playlists, tracks, shows or episodes that match a keyword string.*
  
  
</details>

## Installation
To use and run this project there are a couple of requirements:

**1. Install Flask**

*To install flask open up the command prompt or terminal and type,*
```bash
$ pip install Flask
```
*in case that does not work type,*
```bash
$ sudo pip install Flask
```

**2. Install requests**

*To install Requests, simply run the following command in your terminal of choise:*
```bash
$ python -m pip install requests
```

**3. Install dotenv**

*To install dotenv run following command in terminal:*
```bash
pip install python-dotenv
```

**4. setup dotenv**
  * *Create a `.env` file in the project directory containing Spotify Client id and Client secret in following format:*

```
export sptfy_id = "your client id"
export sptfy_sectret = "your client secret"
```

## Run Application

1. Open up terminal and run command ```python spotify_app.py```
2. Click on "Preview" >> "Preview running application"

## Bugs and Future improvments

### Bugs:

<details>
  <summary><b>Token API</b></summary>
  <br>
  
  One of the first bug I encountered was with Token API where I was not getting a valid repose.

  This happened because, Token API requires base-64 encoded string in header for client credentials. 

  But I was just using ```.encode()```, which means I was encoding my sting with in bytes. 

  To fix the issue I used base64 python library. 

  Before:
  ```python
  creds = f"{sptfy_id}:{sptfy_secret}"
  client_creds = creds.encode()
  ```

  After:
  ```python
  import base64

  creds = f"{sptfy_id}:{sptfy_secret}"    
  client_creds = base64.b64encode(creds.encode())
  ```
    
    
</details>

<details>
  <summary><b>Search API</b></summary>
  <br>

  Another issue I encountered was with search API. Every time I make a request, I would only get error response.

  This was happening because query parameter for the api was embaded in url ``` https://api.spotify.com/v1/search?q=tania%20bowra&type=artist" -H "Accept: application/json"``` instead of being sperated by -H

  So when I tried doing this:
  ```python
  query_param = {
            "q" : name,
            "type" : "artist",
            "limit" : "1"
        }
  response = requests.get(url_lookup, data=query_ param ,headers=request_header)
  ```
  I got an error message.

  To fix this, I used ```urllib.parse.urlencode()``` to convert query_param into query string
  ```python
  from urllib.parse import urlencode

  query_param = urlencode({
        "q" : name,
        "type" : "artist",
        "limit" : "1"
    })

    url_lookup = f"{url}?{query_param}"                             # creates a lookup url

    response = requests.get(url_lookup, headers=request_header) 
  ```
    
</details>
    
<details>
  <summary><b>Error page</b></summary>
  <br>

  Another problem I encountered was when I was implementing the search bar.

  Every time a bad input was made (e.g. Incorrect artist name or empty string name), the page will generate an error message.

  This was happening because any time a bad input is passed through the search API, It will respond with some error code instead of a JSON variable. So when the function tries to use .json() on the response, it will cause an error. 

  So to fix it, I did this:

  1. used try and except to catch an error. (If the response is not an error, then the artist id is returned. Else, error code is returned)


  ```python
  try:    
      results = response.json()
      return results["artists"]["items"][0]["id"]
  except:
      results = response.status_code
      return results
  ```

  2. If an error code is passed, I returned an error message through the template, and the artist id is picked from the hardcoded list


  ```python
  if(isinstance(artist_id, int)):
    return render_template(
          "index.html",
          err_msg = True,                                     # error message
          len = len(song_info),                               # array length 
          len2 = len(song_info[0]),                           # array length for artists
          song_info = song_info,                              # array
          artist_name = spotify_api.get_artist(artist_id)     # gets artist's name
      )
  ```

  3. In HTML file, if an error message is passed, then display the error message


  ```HTML
  {%if err_msg%}
    <h style="font-size: 20px; color: red">No results found !!!</h>
  {%endif%}
  ```
  
</details>

### Future plan

1. Genius API will be implemented, which would allow users to see lyrics of a perticular track.

2. Webpage will be deployed on heroku



