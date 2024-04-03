import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth

#Initial setup
username = config.client_username
playlist_ID = config.playlist_ID
client_ID = config.client_ID
client_secret = config.client_secret
red_URI = "https://localhost:8080"

#Need to feed here whatever we want
artists = ['Justice', 'Disclosure']

#Spotipy setup, with the scope to the user's playlist. No need rn bc playlist is private. Future changes
#scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret=client_secret, redirect_uri=red_URI, scope='playlist-modify-private', username=username))

#For each artist in the list, we search for the first song of the artist and add it to the playlist (now only one song per artist)
for artist in artists:
    #query as stated in Spotipy documentation
    results = sp.search(q='artist:' + artist, type='track', limit=1)
    print(results['tracks']['items'][0]['id']) #-> this works well as it prints the id of the song

    #If the search returns a result, we add the song to the playlist
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id'] 
        #print(track_id)
        sp.playlist_add_items(playlist_ID, [track_id])
