import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import numpy as np
import pandas

client_id = 'f350e4153ac54be89d28d064b152cfeb'
client_secret = "d252e113b8414036bb891b93428c2b51"

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/6y4MPuu1OfE1bzRRGR41fI?si=366c4df1b5a94331"
# PLAYLIST_LINK = "https://open.spotify.com/playlist/3VJlwgnV4IaxGK8uIEZMjV?si=ca8c506dd5d04663"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]

    #Track name
    track_name = track["track"]["name"]

    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]

    # Album
    album = track["track"]["album"]["name"]

    # Popularity of the track
    track_pop = track["track"]["popularity"]

    result = track_name, sp.audio_features(track_uri)
print(result)
def get_playlist_uri(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]


def get_tracks():
    tracks = []
    playlist_uri = get_playlist_uri(playlist_link)
    for track in sp.playlist_tracks(playlist_uri)["items"]:
        track_uri = track["track"]["uri"]
        track_name = track["track"]["name"]
        result = track_name, sp.audio_features(track_uri)
        tracks.append(result)

    return tracks
the_stuff = get_tracks()

print(the_stuff)
