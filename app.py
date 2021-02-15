import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
import random

load_dotenv(find_dotenv())
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def web_app():
    CLIENT_ID = os.getenv('SPOT_ID')
    CLIENT_KEY = os.getenv('SPOT_KEY')
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    AUTH_RES = requests.post( AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_KEY,
    })
    AUTH_DATA = AUTH_RES.json()
    try:
        token = AUTH_DATA['access_token']
    except:
        token = "nodda"
    headers = {
        'Authorization': 'Bearer {token}'.format(token = token)
    }
    
    
    
    
    artist_list = ["6XyY86QOPPrYVGvF9ch6wz","72X6FHxaShda0XeQw3vbeF","3o2dn2O0FCVsWDFSh8qxgG"]
    rand_select = random.randint(0,2)
    artist_select = artist_list[rand_select]
    artist_url = 'https://api.spotify.com/v1/artists/'
    artist_param = {
        'market': 'US'
    }
    artist_request = requests.get(artist_url + artist_select + '/top-tracks', headers = headers, params = artist_param)
    artist_data = artist_request.json()
    song_select = random.randint(0,5)



    try:
        song_name = artist_data['tracks'][song_select]['name']
    except:
        song_name = '[PLACEHOLDER]'
    try:
        song_artist = artist_data['tracks'][song_select]['artists'][0]['name']
    except:
        song_artist = 'could not get data'
    try:
        song_pic = artist_data['tracks'][song_select]['album']['images'][0]['url']
    except:
        song_pic = 'https://i.redd.it/mpvq6gsxwz411.png'
    try:
        song_url = artist_data['tracks'][song_select]['preview_url']
    except:
        song_url = "https://i.scdn.co/image/4295b5ff74d4f944367144acbe616b6f62d20b17"


    GENIUS_URL = 'https://api.genius.com'
    GENIUS_TOK = os.getenv('GEN_TOK')

    gen_headers = {
        'Authorization': 'Bearer {token}'.format(token = GENIUS_TOK)
    }

    gen_search = song_artist + ' ' + song_name
    gen_search_param = {
        'q': gen_search
    }

    gen_search_url = '/search'
    gen_search_request = requests.get(GENIUS_URL + gen_search_url, headers = gen_headers, params = gen_search_param)
    gen_search_data = gen_search_request.json()

    try:
        gen_song_id = gen_search_data['response']['hits'][0]['result']['id']
    except:
        gen_song_id = "d"

    gen_song_url = '/songs/'
    gen_song_request = requests.get(GENIUS_URL + gen_song_url + str(gen_song_id), headers = gen_headers)
    gen_song_data = gen_song_request.json()

    try:
        song_lyrics = gen_song_data["response"]["song"]["url"]
    except:
        song_lyrics = 'https://genius.com/Sia-chandelier-lyrics'



    return render_template(
        "index.html", 
        name = song_name,
        artist = song_artist,
        preview = song_url,
        picture = song_pic,
        lyrics = song_lyrics
    )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    #debug=True
)





