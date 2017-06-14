from selenium import webdriver
from bs4 import BeautifulSoup

def Album_Tag_Crawler(album_id):
    driver = webdriver.PhantomJS()
    album_url = "http://music.163.com/#/playlist?id=" + album_id
    driver.get(album_url)
    driver.switch_to.frame("g_iframe")
    html = driver.page_source

    soup = BeautifulSoup(html,'lxml')

    all_tag = soup.find_all("a", class_= "u-tag")
    '''
    print(all_tag)
    '''
    expert_tags = ""
    for tags in all_tag:
         expert_tags = expert_tags + tags.find('i').string
         expert_tags = expert_tags + "; "
    '''
    print(expert_tags)
    '''
    return expert_tags




