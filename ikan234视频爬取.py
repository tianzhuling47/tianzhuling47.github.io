import requests,colorama,webbrowser
from urllib.parse import urlencode
class Movie(object):
	def __init__(self,id,name,pic):
		self.id=id
		self.name=name
		self.pic=pic
	def show(self,id):
		print(colorama.Fore.BLUE+str(id)+' , '+colorama.Style.BRIGHT+self.name+colorama.Fore.WHITE+colorama.Style.NORMAL)
		print('编号:'+colorama.Fore.GREEN+str(self.id))
		print('封面:'+colorama.Fore.GREEN+str(self.pic)+colorama.Fore.WHITE)
		print('-'*40)
def search(name,page):
	if page==1:
		url='https://ikan234.com/index.php/ajax/suggest'
		data={'mid':(page-1)*10+1,
		'wd':name,
		'limit':'10',
		'timestamp':'1743741123771'}
		resp=requests.get(url,params=data)
		movies=resp.json()['list']
		info=[]
		for i in movies:
			info.append(Movie(i['id'],i['name'],i['pic']))
		return info
	else:
		url=f'https://ikan234.com/search/{urlencode({"wd":name}).strip("wd=")}----------{str(page)}---.html'
		resp=requests.get(url)
		content=resp.content.decode()
		content=content.split('<ul class="stui-vodlist__media col-pd clearfix">')[1].split('</ul>')[0].split('</li>')
		info=[]
		for i in content:
			try:
				name=i.split('title="')[1].split('"')[0]
				id=i.split('href="/vod/')[1].split('.html')[0]
				pic=i.split('data-original="')[1].split('"')[0]
				info.append(Movie(pic=pic,name=name,id=id))
			except:
				pass
		return info
def error(content):
	print(colorama.Fore.RED+f'错误:{content}'+colorama.Fore.WHITE)
def get_movie(id,th,set):	
	#以网页url解析视频url
	url2=f'https://ikan234.com/play/{id}-{th}-{set}.html'
	resp2=requests.get(url2)
	return resp2.content.decode().split('url":"')[3].split('"')[0].replace('\\','')
def main():
	colorama.init()
	while True:
		name=input('剧名:')
		if len(name)>6:
			error('剧名长度小于6')
		else:
			break
	while True:
		page=input('页数:')
		if not page.isdigit():
			error('页数必须为纯数字')
		else:
			break
	info=search(name,int(page))
	num=0
	for i in info:
		num+=1
		i.show(num)
	while True:
		id=input('第几个(填ID):')
		if int(id)>len(info):
			error('ID超过')
		else:
			break
	id=info[int(id)-1].id
	while True:
		set=input('集数(电影请输入1):')
		if not set.isdigit():
			error('集数必须是纯数字')
		else:
			break
	while True:
		th=int(input('线路(1-4):'))
		if 0<=th<=4:
			break
		else:
			error('线路要求未在范围内')
	url=get_movie(id,th,set)
	print(colorama.Style.BRIGHT+colorama.Fore.GREEN+f'影视地址:{url}'+colorama.Fore.WHITE+colorama.Style.NORMAL)
	webbrowser.open(url)
	while True:
		print('''弥留服务:
			1:关闭
			2:修改集数
			3:修改线路''')
		e=input('选择服务:')
		if e=='1':
			exit()
		elif e=='2':
			while True:
				set=input('集数(电影请输入1):')
				if not set.isdigit():
					error('集数必须是纯数字')
				else:
					break	
			url=get_movie(id,th,set)
			print(colorama.Fore.GREEN+f'影视地址:{url}')
			webbrowser.open(url)
		elif e=='3':
			while True:
				th=int(input('线路(1-4):'))
				if 0<=th<=4:
					break
				else:
					error('线路要求未在范围内')
			url=get_movie(id,th,set)
			print(colorama.Fore.GREEN+f'影视地址:{url}')
			webbrowser.open(url)
		else:
			error('无效的输入')
if __name__=='__main__':
	main()
	