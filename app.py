import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

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

@app.route('/')
def Spotify_Display():
    print("test")
    return render_template(
        "index.html", 
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    debug=True
)







