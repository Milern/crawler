#-*_coding:utf8-*-
# Python2.7

import requests
import urllib
from AlbumTagCrawler import Album_Tag_Crawler


import sys

global music_native_ID;
music_native_ID = 1

def Schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    '''   print ('%.2f%%' % per)
   '''

'''
    Here need to guarantee the playlist and song don't have duplicate
'''
def Music_Crawler( play_list_ID, num_of_music_to_crawl, class_file, cur, conn):
    global music_native_ID
    r = requests.get('http://music.163.com/api/playlist/detail?id=' + (play_list_ID))
    arr = r.json()['result']['tracks']

    '''
    The oringinal expertTag is inconsistent with the AJAX one. Need extra handling
    music_tags = (r.json()['result']['creator'])['expertTags']
    print(music_tags)
    '''
    music_tags = Album_Tag_Crawler(play_list_ID)
    print(music_tags)

    arr_length = len(arr)
    if num_of_music_to_crawl>arr_length:
        num_of_music_to_crawl = arr_length
    for i in range(0, num_of_music_to_crawl):
        title = arr[i]['name']
        name = str(music_native_ID) + ' ' + title + '.mp3'
        music_id = arr[i]['id']
        singer = (arr[i]['artists'])[0]['name']
        album = (arr[i]['album'])['name']
        link = arr[i]['mp3Url']

        try:
            '''
            urllib.request.urlretrieve(link, 'Cloud Music\\' + name, Schedule)
            '''
        except:
            print(name + link)
        else:
            print(name + '  download finished')
            print(music_id)
            print("singer:" + singer)
            print("album:" + album + '\n')

            class_file.write('[')
            class_file.write(name)
            class_file.write('; ')
            class_file.write(str(music_id))
            class_file.write('; ')
            class_file.write(singer)
            class_file.write('; ')
            class_file.write(album)
            class_file.write('; ')
            class_file.write(link)
            class_file.write('; ')
            class_file.write(']\n')
            music_native_ID = music_native_ID + 1
            inst = \
                "INSERT INTO music_music_info_detail  " \
                "(music_local_id, music_cloud_id, music_title, music_singer, music_album,lyric_path,music_path,album_cover_path,music_type_label,play_time,frame_num) " \
                "VALUES ("+ str(music_native_ID) + ","+ str(music_id)+",\""+ title+"\",\""+ singer+"\",\"" + album+ "\", 'none' ,'none','none',"+"'" +'put_music_tag_here' + "',"+ str(0)+ ","+ str(0)+ ");"


            cur.execute(inst)

            conn.commit()