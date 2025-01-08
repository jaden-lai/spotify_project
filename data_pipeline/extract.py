from auth.spotify_oath import authenticate_spotify

def extract_recent_tracks(sp):
    results = sp.current_user_recently_played(limit=50)
    tracks = []
    
    for item in results['items']:
        track = item['track']
        tracks.append({
            'track_name': track['name'],
            'artist_name': track['artists'][0]['name'],
            'track_id': track['id'],
            'played_at': item['played_at'],
            'duration_ms': track['duration_ms'],
            'popularity': track['popularity'],
            'explicit': track['explicit'],
            'href': track['href']
        })
    
    return tracks
