from spotify_auth import sp
from spotify_features import playlists

def fetch_audio_features(track_ids):
    return sp.audio_features(track_ids)

# Example usage
track_ids = [track['track']['id'] for track in playlists[:10]]
audio_features = fetch_audio_features(track_ids)
for feature in audio_features:
    print(f"Track ID: {feature['id']}, Tempo: {feature['tempo']}, Danceability: {feature['danceability']}")
