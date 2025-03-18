import requests,webbrowser
from threading import Thread
class Movie(object):
	def __init__(self,vid,name):
		self.vid=vid
		self.name=name
def get_movie(num):
	global movies
	data={'searchword':name,
		'page':num}
		
	resp=requests.get(url,params=data)
	content=resp.content.decode('utf-8').split('<ul class="stui-page text-center clearfix">')[0].split('<ul class="stui-vodlist__media col-pd clearfix">')[1].split('</li>')
	for i in content:
			try:
				title=i.split('title="')[1].split('"')[0]
				vid=i.split('href="')[1].split('"')[0].split('/')[-1].strip('.html')
				movies.append(Movie(vid,title))
			except:
				continue
movies=[]
name=input('请输入影视名称:')
max=input('索取最大页数:')
url='http://www.xigua61.com/search.php'
url2='http://www.xigua61.com/ass.php'

num=0
while True:
	try:
		num+=1
		get_movie(num)
		print(f'已加载{num}页')
		if num==int(max):
			break
	except:
		break
num=0
for i in movies:
	num+=1
	print(f'{num}：{i.name}')
m_id=input('请输入id:')

content2=[]
num=0
data2={'url':'dp',
'vid':movies[int(m_id)-1].vid,
'vfrom':'1',
'vpart':'0','cb':'jQuery110205174952471428527_1742307967276&_=1742307967277'}
resp2=requests.get(url2,params=data2)
for i in resp2.content.decode('utf-8').split('"video":[')[1].split(']')[0].split(','):
	content2.append(i)
videos=[]
a=0
for i in content2:
	a+=1
	href=i.strip('"').replace('\\','')
	videos.append(href)
	print(f'第{a}集:{href}')
set=int(input('第几集:'))
webbrowser.open(videos[set-1])