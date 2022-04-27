# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8aabcaafe3a64000bd21b6936a2f7a9b",
#                                                            client_secret="144250a9c95d481ab07c2d293a54f64c"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sqlite3
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
import ssl
import csv
import matplotlib.pyplot as plt
import numpy as np

# remember to close conn?
def spotify_top_songs(category, playlists):
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


def add_song_by_region(cur, conn, song_data):
    start = 0
    end = 25
    while (end <= len(song_data)):
        insert_into_database_region(cur, conn, song_data, start, end)
        start += 25
        end += 25
    insert_into_database_region(cur, conn, song_data, end, len(song_data))


def insert_into_database_region(cur, conn, song_data, start, end):
    for i in song_data[start:end]:
        cur.execute("INSERT OR IGNORE INTO TopSongsByRegion (Song_URI,Song_title,Region,Artist,Artist_URI) VALUES (?,?,?,?,?)",(i[0], i[1], i[2], i[3], i[4]))
    conn.commit()
  

def add_song_by_genre(cur, conn, song_data):
    start = 0
    end = 25
    while (end <= len(song_data)):
        insert_into_database_genre(cur, conn, song_data, start, end)
        start += 25
        end += 25
    insert_into_database_genre(cur, conn, song_data, end, len(song_data))


def insert_into_database_genre(cur, conn, song_data, start, end):
    for i in song_data[start:end]:
        cur.execute("INSERT OR IGNORE INTO TopSongsByGenre (Song_URI,Song_title,Genre,Artist,Artist_URI) VALUES (?,?,?,?,?)",(i[0], i[1], i[2], i[3], i[4]))
    conn.commit()


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    # set up database (won't insert duplicates because of primary keys)
    cur.execute("DROP TABLE IF EXISTS TopSongsByGenre")
    cur.execute("CREATE TABLE TopSongsByGenre (Song_URI TEXT PRIMARY KEY, Song_title TEXT UNIQUE, Genre TEXT, Artist TEXT, Artist_URI TEXT)")
    
    cur.execute("DROP TABLE IF EXISTS TopSongsByRegion")
    cur.execute("CREATE TABLE TopSongsByRegion (Song_URI TEXT PRIMARY KEY, Song_title TEXT UNIQUE, Region TEXT, Artist TEXT, Artist_URI TEXT)")
    
    cur.execute("DROP TABLE IF EXISTS billboard")
    cur.execute("CREATE TABLE billboard (ranking INTEGER PRIMARY KEY, title TEXT, artist TEXT, weeks_on_chart INTEGER)")
    conn.commit()
    return cur, conn


# Pop rising: https://open.spotify.com/playlist/37i9dQZF1DWUa8ZRTfalHk?si=2a443aa7a8fc49a9
# Rap caviar: https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd?si=f539f715e8814d46
# r&b favourites: https://open.spotify.com/playlist/37i9dQZF1DX7FY5ma9162x?si=826a2adc16ba47c2 
# Hot country: https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda?si=619a851f09624040
# Viva latino: https://open.spotify.com/playlist/37i9dQZF1DX10zKzsJ2jva?si=42ff4a262e3e4e52 

def billboard_info(url): 
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    song_info = []
    songs = soup.find_all('li', class_ = "lrv-u-width-100p")[::2]
    
    for song in songs:
        # find song title
        title = song.find_all('h3', id = 'title-of-a-story')[0].text.strip()
        # find artist name
        item = song.find('ul', class_ = "lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
        name = item.find_all('span', None)[0].text.strip()
        if ("," in name):
            lst = name.split(",")
            name = lst[0].strip()
        if ("/" in name):
            lst = name.split("/")
            name = lst[0].strip()
        if ("Featuring" in name):
            lst = name.split("Featuring")
            name = lst[0].strip()
        if ("&" in name):
            lst = name.split("&")
            name = lst[0].strip()
        if ("X" in name):
            if (name[-1] != "X"):
                lst = name.split("X")
                name = lst[0].strip()

        # find number of weeks on chart
        wks_on_chart = item.find_all('li', class_ = "o-chart-results-list__item // a-chart-color u-width-72 u-width-55@mobile-max u-width-55@tablet-only lrv-u-flex lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light u-background-color-white-064@mobile-max u-hidden@mobile-max")[1].text.strip()
        weeks = int(wks_on_chart)

        # insert tuple into list
        song_info.append((title, name, weeks))
    return song_info        
    

def add_songs(song_info, cur, conn):
    ranking = 1
    for song in song_info:
        title = song[0]
        name = song[1]
        weeks = song[2]
        cur.execute("INSERT INTO billboard (ranking, title, artist, weeks_on_chart) VALUES(?, ?, ?, ?)", (ranking, title, name, weeks))
        ranking += 1
    conn.commit()


def find_similar_songs_region(cur):
    lst = []
    cur.execute(
        """
        SELECT TopSongsByRegion.Region, billboard.title, billboard.artist
        FROM billboard
        JOIN TopSongsByRegion ON TopSongsByRegion.Song_title = billboard.title
        """
    )
    USA, Canada, Mexico, total = 0, 0, 0, 0
    for row in cur:
        if row[0] == "USA":
            USA += 1.0
        elif row[0] == "Canada":
            Canada += 1.0
        else:
            Mexico += 1.0
    # calculate percentage of countries to total and write to csv file
    rows = [ ['USA', USA/100], 
            ['Canada', Canada/100], 
            ['Mexico', Mexico/100]] 
    # writing to csv file 
    with open("region_percentages.csv", 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(['Country', 'Percentage']) 
        csvwriter.writerows(rows)
    return ([USA, Canada, Mexico], ["USA", "Canada", "Mexico"])

def find_similar_songs_genre(cur):
    lst = []
    cur.execute(
        """
        SELECT TopSongsByGenre.Genre, billboard.title, billboard.artist
        FROM billboard
        JOIN TopSongsByGenre ON TopSongsByGenre.Song_title = billboard.title
        """
    )
    pop, rap, rb, country, latino, total = 0, 0, 0, 0, 0, 0
    for row in cur:
        total += 1.0
        if row[0] == "Pop":
            pop += 1.0
        elif row[0] == "Rap":
            rap += 1.0
        elif row[0] == "R&B":
            rb += 1.0
        elif row[0] == "Country":
            country += 1.0
        else:
            latino += 1.0
    # calculate percentage of genres to total and write to csv file
    rows = [['Pop', pop/100], 
            ['Rap', rap/100], 
            ['R&B', rb/100],
            ['Country', country/100],
            ['Latino', latino/100]] 
    # writing to csv file 
    with open("genre_percentages.csv", 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(['Genre', 'Percentage']) 
        csvwriter.writerows(rows)
    return ([pop, rap, rb, country, latino], ["Pop", "Rap", "R&B", "Country", "Latino"])


def make_bar_chart_genre(totals, labels):
    y_pos = np.arange(len(labels))
    plt.barh(y_pos, totals, align='center', alpha=0.5)
    plt.yticks(y_pos, labels)
    plt.xlabel('Songs')
    plt.title('Number of Overlapping Songs per Genre on Billboard Hot 100')
    plt.show()


def make_bar_chart_region(totals, labels):
    y_pos = np.arange(len(labels))
    plt.barh(y_pos, totals, align='center', alpha=0.5)
    plt.yticks(y_pos, labels)
    plt.xlabel('Songs')
    plt.title('Number of Overlapping Songs per Country on Billboard Hot 100')
    plt.show()


def main():
    # set up tables in the database
    cur, conn = setUpDatabase('music.db') # REDO THIS

    # insert top songs in each genre into the TopSongsByGenre table
    genres = ['Pop', 'Rap', 'R&B', 'Country', 'Latino'] # latin or latino???
    playlists = ['37i9dQZF1DWUa8ZRTfalHk', '37i9dQZF1DX0XUsuxWHRQd', 
                 '37i9dQZF1DX7FY5ma9162x', '37i9dQZF1DX1lVhptIYRda', '37i9dQZF1DX10zKzsJ2jva']
    song_data = spotify_top_songs(genres, playlists)
    add_song_by_genre(cur, conn, song_data)

    # insert top songs in each country in North America into the TopSongsByRegion table
    regions = ['USA', 'Canada', 'Mexico']
    playlists = ['37i9dQZEVXbLRQDuF5jeBp', '37i9dQZEVXbKj23U1GF4IR', '37i9dQZEVXbO3qyFxbkOE1']
    song_data = spotify_top_songs(regions, playlists)
    add_song_by_region(cur, conn, song_data)

    # insert songs from billboard 100 into billboard table
    song_info = billboard_info("https://www.billboard.com/charts/hot-100/")
    add_songs(song_info, cur, conn)

    # find overlapping songs from top songs in region and billboard 100
    region_totals, region_labels = find_similar_songs_region(cur)
    genre_totals, genre_labels = find_similar_songs_genre(cur)

    # create visualizations
    make_bar_chart_region(region_totals, region_labels)
    make_bar_chart_genre(genre_totals, genre_labels)

if __name__ == "__main__":
    main()