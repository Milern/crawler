#-*_coding:utf8-*-
from selenium import webdriver
from bs4 import BeautifulSoup

# GetPlayList.py

def List_Craw(file_path, list_URL_raw, num_of_pages_crawled):
    driver = webdriver.PhantomJS()
    '''
    playlist_url_raw = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset="
    '''
    playlist_url_raw = list_URL_raw
    offset = 0
    file_object = open( file_path, 'w')
    '''
    num_of_pages_crawed = 3
    '''
    for i in range(0, num_of_pages_crawled):
        playlist_url = playlist_url_raw + str( 35 * i + offset)
        driver.get(playlist_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source

        soup = BeautifulSoup(html,'lxml')

        all_li = soup.find(id='m-pl-container').find_all('li')

        for li in all_li:
            list_id = li.find('a')['href']
            start_pos = list_id.index('=')
            file_object.write(list_id[start_pos+1:])
            file_object.write('\n')

    file_object.close()
