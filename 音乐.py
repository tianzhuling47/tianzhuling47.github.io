import requests,os
class Mp3():
	def __init__(self,link,songid,title,author,lrc,music,pic):
		self.link=link
		self.id=songid
		self.title=title
		self.author=author
		self.lrc=lrc
		self.music=music
		self.pic=pic
	def download(self,path):
		if not os.path.exists('/'+path.strip('/')+'/mp3_download'):
			os.mkdir(path.strip('/')+'/mp3_download')
		if not os.path.exists('/'+path.strip('/')+f'/mp3_download/{self.title}_{self.id}'):	
			os.mkdir('/'+path.strip('/')+f'/mp3_download/{self.title}_{self.id}')
		with open('/'+path.strip('/')+f'/mp3_download/{self.title}_{str(self.id)}/info.txt','wt',encoding='utf-8')as f:
			f.write('link:'+self.link+'\nid:'+str(self.id)+'\ntitle:'+self.title+'\nauthor:'+self.author)
		resp2=requests.get(self.pic)
		with open('/'+path.strip('/')+f'/mp3_download/{self.title}_{self.id}/lrc.txt','wt',encoding='utf-8')as f:
			f.write(self.lrc)
		with open('/'+path.strip('/')+f'/mp3_download/{self.title}_{self.id}/pic.png','wb')as f:
			f.write(resp2.content)
		resp3=requests.get(self.music)
		with open('/'+path.strip('/')+f'/mp3_download/{self.title}_{self.id}/music.mp3',"wb")as f:
			f.write(resp3.content)
while True:
	name=input('歌名:')
	page=input('页数:')
	all_mp3=[]
	url='https://www.myfreemp3.com.cn/'
	headers={'Cookie':'UM_distinctid=19574621f4714e-0fa3196615660c-b457453-36380-19574621f483f7','x-requested-with':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'}
	data={'input':name,'filter':'name','page':page,'type':'netease'}
	resp=requests.post(url,headers=headers,data=data)
	mp3_list=resp.json()['data']['list']
	for mp3 in mp3_list:
		link=mp3['link']
		songid=mp3['songid']
		title=mp3['title']
		author=mp3['author']
		lrc=mp3['lrc']
		music=mp3['url']
		pic=mp3['pic']
		all_mp3.append(Mp3(link,songid,title,author,lrc,music,pic))
	a=0
	for i in all_mp3:
		a+=1
		print(a,end=':')
		print('歌名:',i.title)
		print('歌手:',i.author)
	print('1:下载全部\n2:选择下载')
	mode=input('下载模式(1/2):')
	if mode=='1':
		for i in all_mp3:
			i.download('/storage/emulated/0/')
	elif mode=='2':
		res=input('第几个:')
		all_mp3[int(res)-1].download('/storage/emulated/0/')
		print('已下载到 /storage/emulated/0/mp3_download/')