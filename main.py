# Your name: Yilin Fang
# Your student id: 06010542
# Your email: yilfang@umich.edu
# List who you have worked with on this project: Amy Tang

import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.request import urlopen
import ssl
import sqlite3

def setUpBillboardDB(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_billboard_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS billboard")
    cur.execute("CREATE TABLE billboard (ranking INTEGER PRIMARY KEY, title TEXT, artist TEXT, weeks_on_chart INTEGER)")
    conn.commit()

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

        # # find artist name
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

def main():
    cur, conn = setUpBillboardDB('billboard.db')
    create_billboard_table(cur, conn)
    song_info = billboard_info("https://www.billboard.com/charts/hot-100/")
    add_songs(song_info, cur, conn)

if __name__ == "__main__":
        main()