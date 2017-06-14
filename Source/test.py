#-*_coding:utf8-*-
# Python3.6

import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '19930808',
    db = 'MUSIC_INFO',
)

cur = conn.cursor()
inst = \
    "INSERT INTO music_music_info_detail  " \
    "(music_local_id, music_cloud_id, music_title, music_singer, music_album,lyric_path,music_path,album_cover_path,music_type_label,play_time,frame_num) " \
    "VALUES (2,2333,'HAHA','HEHEHE','HEHEHE','a','a','a','a',1,2);"

cur.execute(inst)


cur.close()
conn.commit()
conn.close()