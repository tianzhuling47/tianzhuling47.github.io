try:
	import socket,json,os,colorama,requests
	from tqdm import tqdm
except Exception:
	print('错误:导入模块失败，确保有以下模块:\nsocket,json,os,colorama,tqdm,requests,webbrowser\n在终端输入以导入模块，命令为:\npip install example\n其中example为模块名')
def check(now):
    try:
	    resp=requests.get("https://tianzhuling.github.io/lib/文件传输/index.txt")
	    if now < float(resp.content.decode('utf-8').split("\n")[0]):
	    	end=input(f"目前版本为{str(now)},最高版本为"+resp.content.decode('utf-8').split('\n')[0]+"是否更新(Y/n)")
	    	if end=="Y":
	    		resp=requests.get("https://tianzhuling.github.io/lib/文件传输/文件传输("+resp.content.decode("utf-8").split('\n')[0]+").py")
	    		with open(__file__,"wt",encoding="utf-8")as f:
	    			f.write(resp.content.decode("utf-8"))
	    			print('更新成功')
	    			exit()
    except Exception as e:
	   	print(f'版本检查错误:{e}')
def bytes_to_human_readable(num_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    size = float(num_bytes)
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"
def start():
	colorama.init()
	print('初始化……')
	server=socket.socket()
	client=socket.socket()
	while True:
		try:
			ip=get_inner_ip()
			print(f'获取IP成功,IP为{ip}')
			break
		except Exception:
			error('获取IP失败，请确保网络正常')
			
	return server,client,ip
def ok(content):
	print(GREEN+f'成功:{content}'+CLEAR)
def error(content):
	print(RED+f'错误:{content}'+CLEAR)
def spline(title):
	print(YELLOW+'-'*20+title+'-'*20+CLEAR)
def get_size(path):
	with open(path,'rb')as f:
		size=0
		while True:
			content=f.read(8192)
			if not content:
				break
			size+=len(content)
	return size
def get_inner_ip():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(('8.8.8.8',80))
	ip=s.getsockname()[0]
	s.close()
	return ip
def send_file(sock2,path,ip,port):
	spline('发送文件')
	print('建立连接中')
	sock2.connect((ip,int(port)))
	ok('成功建立连接')
	size=get_size(path)
	headers={'ip':get_inner_ip(),'name':os.path.basename(path),'size':size}
	sock2.send(json.dumps(headers).encode('utf-8'))
	with open(path,'rb')as f:
		with tqdm(total=size)as pbar:
			while True:
				content=f.read(8192)
				sock2.send(content)
				if not content:
					break
				pbar.update(len(content))
			ok('数据发送完成')
			sock2.close()
def get_file(sock):
	spline('接收文件')
	sock.listen(1)
	i,addr=sock.accept()
	try:
		content=i.recv(8192)
		content=content.decode('utf-8')
		headers=json.loads(content)
	except Exception:
		error('获取和解析请求头失败')
	ok(f"IP为{headers['ip']}发送的大小为{bytes_to_human_readable(headers['size'])}的 {headers['name']} 文件")
	with open(headers['name'],'wb')as f:
		with tqdm(total=headers['size']) as pbar:
			try:
				while True:
					data=i.recv(8192)
					if not data:
						break
					f.write(data)
					pbar.update(len(data))
			except Exception as e:
				error(f'未知错误:{e}')
	ok('数据接收完成')
	ok(f'文件已保存在同目录 {headers["name"]} 文件')
def main():
	server,client,ip=start()
	global RED,GREEN,YELLOW,CLEAR
	RED=colorama.Fore.RED
	GREEN=colorama.Fore.GREEN
	YELLOW=colorama.Fore.YELLOW
	CLEAR=colorama.Style.RESET_ALL
	spline('端口绑定')
	try:
		server.bind((ip,5000))
		ok('绑定成功，端口:5000 ')
	except Exception as e:
		error('绑定失败')
		while True:
			port=input('更换端口(原5000):')
			try:
				server.bind((ip,int(port)))
				break
			except Exception:
				error('绑定失败')
				
	while True:
			spline('主功能')
			mode=input('1:发送文件/2:接受模式')
			if mode=='1':
				send_file(client,path=input('请输入要发送的文件路径:'),ip=input('请输入接收方IP地址:'),port=input('请输入接收方端口:'))
			elif mode=='2':
				get_file(server)
if __name__=='__main__':
	check(1.1)
	main()
