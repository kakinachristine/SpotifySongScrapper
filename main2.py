import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import numpy as np
import pandas
import spotipy
import spotipy.util as util


CLIENT_ID = "f350e4153ac54be89d28d064b152cfeb"
CLIENT_SECRET = "76c3d163aa2e40e388d8c7da7f98192d"
token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

cache_token = "BQAGDFdRWC593Di52ticnBLHKphnrlbcJjHMhTIaqtXam8JLip8yzZPjbD3XKbws2O6_-pcQHiz-fgwb-XMH7KavA7HqMc647AHZ70JT_q9lTzpHs1E"
sp = spotipy.Spotify(cache_token)

sp.user_playlist_tracks("kiki", "6y4MPuu1OfE1bzRRGR41fI")
sp.user_playlist_tracks("spotify", "37i9dQZF1DX5IDTimEWoTd")
# https://open.spotify.com/playlist/6y4MPuu1OfE1bzRRGR41fI?si=4b12466cc5f2448b

def analyze_playlist(creator, playlist_id):
    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
                              "time_signature"]

    playlist_df = pd.DataFrame(columns=playlist_features_list)

    # Loop through every track in the playlist, extract features and append the features to the playlist df

    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]

        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]

        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index=[0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)

    return playlist_df
print(analyze_playlist("kiki", "6y4MPuu1OfE1bzRRGR41fI"))