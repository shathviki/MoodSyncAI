import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, session, redirect, url_for, request

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id = 'f13c31f4ef944d45a90cff577b0af6a8'
client_secret = '58a684b699d347ebaa443e36f0db0017'
redirect_uri = 'http://localhost:5000/callback'
scope = 'playlist-modify-private playlist-modify-public playlist-read-private'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True
)

sp = Spotify(auth_manager=sp_oauth)

# Function to get songs based on mood
def get_songs_based_on_mood(mood):
    mood_keywords = {
            'happy': 'upbeat pop, teenage hits, chart-toppers',
            'sad': 'acoustic, mellow pop, slow R&B',
            'stressed': 'rap, hip-hop, intense beats',
            'excited': 'dance, electronic, pop hits',
            'relaxed': 'chill R&B, lo-fi, smooth pop',
            'party': 'pop, rap, hip-hop, party anthems',
            'vibe': 'R&B, upbeat pop, chill rap, smooth hits',
        }

    if mood not in mood_keywords:
        return []

    # Search for tracks based on the mood keyword
    results = sp.search(q=mood_keywords[mood], type='track', limit=20)
    
    # Extract song URIs from the search results
    song_uris = [track['uri'] for track in results['tracks']['items']]
    
    return song_uris

@app.route('/')
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('create_playlist'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('create_playlist'))

@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

    if request.method == 'POST':
        playlist_name = request.form['playlist_name']
        mood = request.form['mood']

        # Get user info
        user = sp.current_user()
        
        # Create the playlist
        playlist = sp.user_playlist_create(user['id'], playlist_name, public=False)

        # Get random songs based on the mood
        song_uris = get_songs_based_on_mood(mood)

        if not song_uris:
            return f"No songs found for mood '{mood}'."

        # Add the songs to the playlist
        sp.user_playlist_add_tracks(user['id'], playlist['id'], random.sample(song_uris, min(10, len(song_uris))))

        return f"Playlist '{playlist_name}' created with {mood} songs! View it <a href='{playlist['external_urls']['spotify']}'>here</a>."

    return '''
        <form method="POST">
            <label for="playlist_name">Enter Playlist Name:</label>
            <input type="text" id="playlist_name" name="playlist_name" required>
            <br><br>
            <label for="mood">Select Mood:</label>
            <select id="mood" name="mood">
                <option value="happy">Happy</option>
                <option value="sad">Sad</option>
                <option value="stressed">Stressed</option>
                <option value="excited">Excited</option>
                <option value="relaxed">Relaxed</option>
            </select>
            <br><br>
            <button type="submit">Create Playlist</button>
        </form>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)