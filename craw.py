#-*_coding:utf8-*-
# 网易云音乐批量下载
# Python3.5.1
import requests
import urllib

#r = requests.get('http://music.163.com/api/playlist/detail?id=14921938')# id后面的数字为你需要爬取的歌单id，网页版云音乐网页链接可看到
r = requests.get('http://music.163.com/api/playlist/detail?id=14921938')# id后面的数字为你需要爬取的歌单id，网页版云音乐网页链接可看到
arr = r.json()['result']['tracks']	# 共有100首歌
def Schedule(a,b,c):
	'''
	a:已经下载的数据块
	b:数据块的大小
	c:远程文件的大小
	'''
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
#	print ('%.2f%%' % per)
for i in range(1,30):	#5为起始数，10为截至数。本例就是下载第5到第10首歌曲，若要从第一首开始，括号内直接写要下载的数量即可
	name = str(i+1) + '、 ' + arr[i]['name'] + '.mp3'
	link = arr[i]['mp3Url']
	urllib.request.urlretrieve(link,'网易云音乐\\'+name,Schedule)	# 提前要在同一目录下创建 网易云音乐 文件夹
	print(name+'  下载完成')
