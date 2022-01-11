# Project-1 Spotify lookup
Project 1 creates Music discovery app that uses Spotify API to dynamically fetch data form Spotify libraries to show top tracks of an Artist. The user will have option to pick an artist through a search bar on page. In case an artist is not picked the page will load top tracks for one of the three pre-selected artists. 

<img src="https://github.com/NJIT-CS490-SP21/Spotify-lookup/blob/main/Spotify-lookup.PNG" width=600>

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
  
  ### 5. [Genius API](https://docs.genius.com/#search-h2)
  
  + *Get song lyrics by passing in the song name*
  
  
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
export genius_token = "your genius api access token"
```

## Run Application

1. Open up terminal and run command ```python spotify_app.py```
2. Click on "Preview" >> "Preview running application"

## Link to website

[Click here...](https://obscure-eyrie-86329.herokuapp.com/)

*(Disclaimer: If you are using Grammarly extension in your browser, the app may not work properly. Please open the page in incognito tab or disable Grammarly for the website.)*




