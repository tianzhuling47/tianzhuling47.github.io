import requests,webbrowser,time
url='https://m.wandoujia.com/search'
while True:
	name=input('输入软件名:')
	data={'key':name,
	'source':'detail'}
	resp=requests.get(url,params=data)
	apps=resp.content.decode().split('<span class="current">搜索结果</span>')[1].split('<div class="load-more">')[0].split('</li>')[1:-1]
	urls=[]
	num=0
	for i in apps:
		num+=1
		name=i.strip().split('"name">')[1].split('<')[0]
		set_up=i.strip().split('<div class="meta">')[1].split('</div>')[0].split('<span>')[1].split('</span>')[0]
		say=i.strip().split('<div class="comment">')[1].split('</div>')[0].strip()
		url=i.strip().split('href="')[1].split('">')[0]
		print(str(num)+'，',name)
		print(set_up,end='\n'*2)
		print(say,end='\n'*2)
		print(url)
		print('安装包url:',f'https://m.wandoujia.com/apps/{url.split("/")[-1]}/download/dot?ch=detail_normal_dl')
		print('-'*40)
		urls.append(url)
	n=int(input('第几个').strip())
	headers={
	    "Host": "m.wandoujia.com",
	    "upgrade-insecure-requests": "1",
	    "User-Agent": "Mozilla/5.0 (Linux; U; Android 10; zh-cn; PBET00 Build/QKQ1.190918.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 HeyTapBrowser/40.9.7.0.2beta",
	    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	    "sec-fetch-site": "none",
	    "sec-fetch-mode": "navigate",
	    "sec-fetch-dest": "document",
	    "referer": "https://m.wandoujia.com/apps/8320899",
	    "accept-encoding": "gzip, deflate, br",
	    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
	    
	  }
	data={'ch':'detail_normal_dl'}
	url2=f'https://m.wandoujia.com/apps/{urls[n-1].split("/")[-1]}/download/dot?ch=detail_normal_dl'
	webbrowser.open(url2)