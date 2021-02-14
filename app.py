import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
import random

load_dotenv(find_dotenv())



CLIENT_ID = os.getenv('SPOT_ID')
CLIENT_KEY = os.getenv('SPOT_KEY')
AUTH_URL = 'https://accounts.spotify.com/api/token'
AUTH_RES = requests.post( AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_KEY,
})
AUTH_DATA = AUTH_RES.json()
token = AUTH_DATA['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token = token)
}




app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0




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



song_name = 'no data'
song_artist = 'no data'
song_pic = 'no data'
song_url = 'no data'
song_name = artist_data['tracks'][song_select]['name']
song_artist = artist_data['tracks'][song_select]['artists'][0]['name']
song_pic = artist_data['tracks'][song_select]['album']['images'][0]['url']
try:
    song_url = artist_data['tracks'][song_select]['preview_url']
except:
    song_url = "no preview avaible"


GENIUS_URL = 'https://api.genius.com'
GENIUS_TOK = os.getenv('GEN_TOK')

gen_headers = {
    'Authorization': 'Bearer {token}'.format(token = GENIUS_TOK)
}

gen_search = song_artist + ' ' + song_name

print(gen_search)

gen_param = {
    'q': gen_search
}

gen_search_url = '/search'

gen_request = requests.get(GENIUS_URL + gen_search_url, headers = gen_headers, params = gen_param)
gen_data = gen_request.json()

print(gen_data['response']['hits'][0]['result']['full_title'])




@app.route('/')
def Spotify_Display():
    return render_template(
        "index.html", 
        name = song_name,
        artist = song_artist,
        preview = song_url,
        picture = song_pic
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    #debug=True
)





