search='poker face'
import we
import requests
from threading import Thread
import pygame
obj=[]
url='https://www.myfreemp3.com.cn/'
ok=False
page=1
headers={'User-Agent':'Mozilla/5.0 (Linux; U; Android 10; zh-cn; PBET00 Build/QKQ1.190918.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 HeyTapBrowser/40.9.4.1','X-Requested-With':'XMLHttpRequest'}
class Music(object):
    def __init__(self,title,author,lrc,img_url,music_url):
        self.title=title
        self.author=author
        self.lrc=lrc
        self.img_url=img_url
        self.music_url=music_url
    def img_file(self):
        
        with open(f'/storage/emulated/0/image_from{__file__.split("/")[-1]}.png','wb')as f:
            f.write(requests.get(self.img_url).content)
        return f'/storage/emulated/0/image_from{__file__.split("/")[-1]}.png'
    def mp3_file(self):
         with open(f'/storage/emulated/0/mp3_from{__file__.split("/")[-1]}.mp3','wb')as f:
            f.write(requests.get(self.music_url).content)
         f'/storage/emulated/0/image_from{__file__.split("/")[-1]}.mp3'
def content_get(i,a):
    global obj
    obj.append(Music(i.get('title'),i.get('author'),i.get('lrc'),i.get('pic'),i.get('url')))
def page_get(x,a):
    global ok
    try:
        params={
            'input':search,
            'filter':'name',
            'page':x,
            'type':'netease'
            }
        data=requests.post(url,headers=headers,data=params)
        data=data.json()['data']['list']
        for i in data:
            Thread(target=content_get,args=[i,0]).start()
        ok=True
    except:
        return
#-----pygame-----#
pygame.init()
root=pygame.display.set_mode((0,0))  
FONT='Droid Sans Fallback'
while True:
      root.fill((255,255,255))
      root.blit(pygame.font.SysFont(FONT,50).render('提示:代码第一行:设置搜索内容',True,(200,210,0)),(0,0))
      root.blit(pygame.font.SysFont(FONT,50).render(f'当前搜索内容:"{search}"',True,(0,0,0)),(0,60))
      root.blit(pygame.font.SysFont(FONT,50).render(f'当前页数:{page}',True,(0,0,0)),(0,120))
      if not ok:
          root.blit(pygame.font.SysFont(FONT,50).render(f'正在加载中…',True,(0,0,255)),(400,200))
          obj.clear()
      else:
           ax=0
           for ob in obj:
               ax+=1
               path=ob.img_file()
              
               img_n=pygame.image.load(path)
               img_new=pygame.transform.scale(img_n,(170,170))
               add=''
               a_add=''
               if len(ob.title)>11:
                   add='…'
               if len(ob.author)>9:
                   a_add='…'
               if ax > 10:
                   root.blit(img_new,(550,0+ax*190-1900))
                   root.blit(pygame.font.SysFont(FONT,30).render(ob.title[0:10]+add,True,(0,0,0)),(730,0+ax*190-1900))
                   root.blit(pygame.font.SysFont(FONT,30).render('歌手:'+ob.author[0:8]+a_add,True,(0,0,0)),(730,0+ax*190-1850))
               else:
                   root.blit(img_new,(0,0+ax*190))     
                   root.blit(pygame.font.SysFont(FONT,30).render(ob.title[0:10]+add,True,(0,0,0)),(180,0+ax*190))
                   root.blit(pygame.font.SysFont(FONT,30).render('歌手:'+ob.author[0:8]+a_add,True,(0,0,0)),(180,50+ax*190))
      pygame.display.update()
      if not ok:
          page_get(page,0)
      