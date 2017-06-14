from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
from ListIDCrawler import List_Craw


#Generating playlist file, each file belongs to a Class type

file_object = open('ClassURL')
list_ID = 0
for line in file_object:
    start_pos = line.index(';')
    '''
    start_pos_2 = line.index('?')
    playlist_url_raw = "http://music.163.com/#" + line[start_pos + 1 : start_pos_2 + 1] + "order=hot&" + line[start_pos_2 + 1 : len(line)]+"&limit=35&offset="
    Mustn't delete to the last item
    '''
    playlist_url_raw = "http://music.163.com/#" + line[start_pos + 1: len(line)-1] + "&limit=35&offset="
    #define the number of pages of playist to craw per class
    num_of_pages_to_craw= 3

    print "Crawling class"
    print line[0:start_pos]

    List_Craw("/home/merlin/Crawler/Play Lists/PlayList_" + str(list_ID), playlist_url_raw, num_of_pages_to_craw)
    list_ID = list_ID + 1


file_object.close()