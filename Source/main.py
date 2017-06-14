#-*_coding:utf8-*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
from ListIDCrawler import List_Craw
from Crawler import Music_Crawler
import Crawler

import sys
import MySQLdb


def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    music_class_num = 1 # define the number of playlist file to crawl, ie. the number of music class
    music_per_playlist_crawling = 3
    global music_native_ID

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='19930808',
        db='MUSIC_INFO',
    )
    conn.set_character_set('utf8')
    cur = conn.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')

    for i in range(0,music_class_num):
        file_name = '/home/merlin/Crawler/Music File//Music Class ' + str(i)
        class_file = open(file_name,'w')
        file_object = open('/home/merlin/Crawler/Play Lists/PlayList_' + str(i))
        for line in file_object:
            print(line)
            Music_Crawler(line, music_per_playlist_crawling, class_file, cur, conn)
        file_object.close()
        class_file.close()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()