import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
CLIENT_ID = "af73efed8fb842ebbd413d01159984a2"
CLIENT_SECRET = "082911d4b6a84fbfab9c92e3bf83529d"
REDIRECT_URI = "http://localhost:8080/callback"

# Set up OAuth with required scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private playlist-read-collaborative user-read-recently-played user-top-read"
))