from selenium import webdriver
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#-*- coding:utf-8 -*-
# Get music class mainpage which contains different playlists, generating ClassURL.
file_object = open('ClassURL', 'w')

driver = webdriver.PhantomJS()
playlist_url = "http://music.163.com/#/discover/playlist"
driver.get(playlist_url)
driver.switch_to.frame("g_iframe")
html = driver.page_source

soup = BeautifulSoup(html,'lxml')

all_dl = soup.find(id='m-disc-pl-c').find_all('dl')

for li in all_dl:
    class_id = li.find_all('a')
    for j in range(0,len(class_id)):
        file_object.write(class_id[j]['data-cat'])
        file_object.write(";")
        file_object.write(class_id[j]['href'])
        file_object.write('\n')

file_object.close()