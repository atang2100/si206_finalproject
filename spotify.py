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
def spotify_topSongsByGenre(category, playlists):
    results = []
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="8aabcaafe3a64000bd21b6936a2f7a9b",
                                                                            client_secret="144250a9c95d481ab07c2d293a54f64c"))
    for iter in range(len(category)):
        pl_id = 'spotify:playlist:' + playlists[iter]
        offset = 0
        cat = category[iter]

        while True:
            response = sp.playlist_items(pl_id,
                                        offset=offset,
                                        fields='items.track.name, items.track.id, items.track.artists, total',
                                        additional_types=['track'])
            
            if len(response['items']) == 0:
                break
            for i in range(len(response['items'])):
                # make a tuple and insert into list
                artist_uri = response['items'][i]['track']['artists'][0]['id']
                artist_name = response['items'][i]['track']['artists'][0]['name']
                song_uri = response['items'][i]['track']['id']
                song_name = response['items'][i]['track']['name']
                results.append((song_uri, song_name, cat, artist_name, artist_uri))
            offset = offset + len(response['items'])
    return results



def insert_into_database_genre(cur, conn, song_data):
    # print(len(song_data))
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
    # stop inserting if song_data is inserting for 
    # if len(song_data) >= count:
    #     conn.commit()
    #     return
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
    
def insert_into_database_region(cur, conn, song_data):
    # print(len(song_data))
    count = 0
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
    while True:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(song_data[count][0],song_data[count][1],song_data[count][2],song_data[count][3],song_data[count][4]))
        count += 1
        if count % 25 == 0:
            break
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


# Pop rising: https://open.spotify.com/playlist/37i9dQZF1DWUa8ZRTfalHk?si=2a443aa7a8fc49a9
# Rap caviar: https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd?si=f539f715e8814d46
# r&b favourites: https://open.spotify.com/playlist/37i9dQZF1DX7FY5ma9162x?si=826a2adc16ba47c2 
# Hot country: https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda?si=619a851f09624040
# Viva latino: https://open.spotify.com/playlist/37i9dQZF1DX10zKzsJ2jva?si=42ff4a262e3e4e52 



def main():
    # set up tables in the database
    cur, conn = setUpDatabase('spotify.db') # REDO THIS

    # insert top songs in each genre into the TopSongsByGenre table
    genres = ['Pop', 'Rap', 'R&B', 'Country', 'Latino'] # latin or latino???
    playlists = ['37i9dQZF1DWUa8ZRTfalHk', '37i9dQZF1DX0XUsuxWHRQd', 
                 '37i9dQZF1DX7FY5ma9162x', '37i9dQZF1DX1lVhptIYRda', '37i9dQZF1DX10zKzsJ2jva']
    song_data = spotify_topSongsByGenre(genres, playlists)
    insert_into_database_genre(cur, conn, song_data)

    # insert top songs in each country in North America into the TopSongsByRegion table
    regions = ['USA', 'Canada', 'Mexico']
    playlists = ['37i9dQZEVXbLRQDuF5jeBp', '37i9dQZEVXbKj23U1GF4IR', '37i9dQZEVXbO3qyFxbkOE1']
    song_data = spotify_topSongsByGenre(regions, playlists)
    insert_into_database_region(cur, conn, song_data)


if __name__ == "__main__":
    main()