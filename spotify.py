# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8aabcaafe3a64000bd21b6936a2f7a9b",
#                                                            client_secret="144250a9c95d481ab07c2d293a54f64c"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
import os
import sqlite3

# remember to close conn?
def spotify_topSongsByGenre(genres, playlists, cur, conn):
    results = []
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="8aabcaafe3a64000bd21b6936a2f7a9b",
                                                                            client_secret="144250a9c95d481ab07c2d293a54f64c"))
    for iter in range(len(genres)):
        # pl_id = 'spotify:playlist:37i9dQZF1DWUa8ZRTfalHk'
        pl_id = 'spotify:playlist:' + playlists[iter]
        offset = 0
        genre = genres[iter]


        while True:
            response = sp.playlist_items(pl_id,
                                        offset=offset,
                                        fields='items.track.name, items.track.id, items.track.artists, total',
                                        additional_types=['track'])
            
            if len(response['items']) == 0:
                break
            for i in range(len(response['items'])):
                # get the first artist
                artist_uri = response['items'][i]['track']['artists'][0]['id']
                artist_name = response['items'][i]['track']['artists'][0]['name']
                song_uri = response['items'][i]['track']['id']
                song_name = response['items'][i]['track']['name']
                results.append((song_uri, song_name, genre, artist_name, artist_uri))
            offset = offset + len(response['items'])
    # print(results)
    conn.commit()
    return results



def insert_into_database(cur, conn, song_data):
    count = 0
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True and count < len(song_data):
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
    conn.commit()
    

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    # set up database (won't insert duplicates because of primary key)
    cur.execute("DROP TABLE IF EXISTS TopSongsByGenre")
    cur.execute("CREATE TABLE TopSongsByGenre (Song_URI TEXT PRIMARY KEY, Song_title TEXT UNIQUE, Genre TEXT, Artist TEXT, Artist_URI TEXT)")
    
    cur.execute("DROP TABLE IF EXISTS TopSongsByRegion")
    cur.execute("CREATE TABLE TopSongsByRegion (Song_URI TEXT PRIMARY KEY, Song_title TEXT UNIQUE, Region TEXT, Artist TEXT, Artist_URI TEXT)")
    return cur, conn

# def setUpTypesTable(data, cur, conn):
#     type_list = []
#     for pokemon in data:
#         pokemon_type = pokemon['type'][0]
#         if pokemon_type not in type_list:
#             type_list.append(pokemon_type)
#     cur.execute("CREATE TABLE IF NOT EXISTS Types (id INTEGER PRIMARY KEY, type TEXT UNIQUE)")
#     for i in range(len(type_list)):
#         cur.execute("INSERT OR IGNORE INTO Types (id,type) VALUES (?,?)",(i,type_list[i]))
#     conn.commit()


# Pop rising: https://open.spotify.com/playlist/37i9dQZF1DWUa8ZRTfalHk?si=2a443aa7a8fc49a9
# Rap caviar: https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd?si=f539f715e8814d46
# r&b favourites: https://open.spotify.com/playlist/37i9dQZF1DX7FY5ma9162x?si=826a2adc16ba47c2 
# Hot country: https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda?si=619a851f09624040
# Viva latino: https://open.spotify.com/playlist/37i9dQZF1DX10zKzsJ2jva?si=42ff4a262e3e4e52 



def main():
    genres = ['Pop', 'Rap', 'R&B', 'Country', 'Latino'] # latin or latino???
    playlists = ['37i9dQZF1DWUa8ZRTfalHk', '37i9dQZF1DX0XUsuxWHRQd', 
                 '37i9dQZF1DX7FY5ma9162x', '37i9dQZF1DX1lVhptIYRda', '37i9dQZF1DX10zKzsJ2jva']
    cur, conn = setUpDatabase('spotify.db')
    song_data = spotify_topSongsByGenre(genres, playlists, cur, conn)
    insert_into_database(cur, conn, song_data)

if __name__ == "__main__":
    main()