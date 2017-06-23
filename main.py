import requests
from bs4 import BeautifulSoup

def getSongList():
    songList = []
    chars = "1abcdefghijklmnopqrstuvwxyz"
    baseurl = "http://www.songfacts.com/browse-song-"
    for i in chars:
        print(i)
        firstPage = baseurl+i+"-1.php"
        page = BeautifulSoup(requests.get(firstPage).text, 'lxml')

        orangelist = page.find("ul", {"class": "songullist-orange"})
        songList.extend(orangelist.text.split("\n"))

        try:
            numPages = int(page.find("div", {"class": "pagin-orange"}).find_all("a")[1].text)
            print(numPages)
        
            for j in range(2,numPages+1):
                page = BeautifulSoup(requests.get(baseurl+i+"-"+str(j)+".php").text, 'lxml')
                orangelist = page.find("ul", {"class": "songullist-orange"})
                songList.extend(orangelist.text.split("\n"))
        except:
            pass
    return songList

def findSongs(songList, word="fruit"):
    songsWithWord = []
    for song in songList:
        
        if word in song.split("-")[0].lower():
            songsWithWord.append(song)
    return songsWithWord

print(findSongs(getSongList()))
