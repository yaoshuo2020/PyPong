from pygame import *
import pygame
from random import randint
from time import sleep
#介绍
init()
print('The version is 0.01.')
sleep(3)
print('Let\'s go to game:')
sleep(1)
#对象定义
#(
#Game对象
class Game:
	def __init__(self,background,music):
		self.bj=background
		self.music=music
		self.Gameoven=False
		self.Game_time=0
		self.Game_time_ding=30000
		self.score=0
	#刷新函数
	def Game_background(self):
		#加音乐和背景还有字体
		self.Game_time+=30
		if self.Game_time==self.Game_time_ding:
			for i in range(2):
				ball.speed[i]+=5
			self.Game_time_ding=Game_time_ding*2
	def refresh(self):
		if self.score==5:
			self.Gameoven='win'
		racket.move()
		ball.move()
		Fonts.refresh()
		display.flip()
		scr.fill([255,255,255])
		self.Game_background()
	def move(self):
		pass
#Ball对象
class Ball(sprite.Sprite):
	def __init__(self,img,ln,speed):
		sprite.Sprite.__init__(self)
		self.img=image.load(img)
		self.rect=self.img.get_rect()
		self.rect.left,self.rect.top=ln
		self.speed=speed
		self.score=0
	def move(self):
		if self.rect.left<0 or self.rect.right>800:
			self.speed[0]=-self.speed[0]
		if self.rect.top<=0:
			self.speed[1]=-self.speed[1]
		if self.rect.top>600:
			Game.Gameoven=True
			self.kill()
		if sprite.spritecollide(racket,BallGroup,False):
			self.speed[1]=-self.speed[1]
			Game.score+=1
		if Game.Gameoven=='win':
			self.kill()
		self.rect=self.rect.move(self.speed)
		scr.blit(self.img,[self.rect.left,self.rect.top])
#Racket对象
class Racket(sprite.Sprite):
	def __init__(self,img,ln,speed):
		sprite.Sprite.__init__(self)
		self.img=image.load(img)
		self.speed=speed
		self.rect=self.img.get_rect()
		self.rect.left,self.rect.top=ln
		self.left=0
	def obtain_xy(self):
		if event.key==K_a:
			self.rect.left-=self.speed
		elif event.key==K_d:
			self.rect.left+=self.speed
	def move(self):
		scr.blit(self.img,[self.rect.left,self.rect.top])
		if Game.Gameoven==True:
			self.kill()
#Font对象
class Fonts:
	def __init__(self,Font,size):
		self.Font=pygame.font.Font(Font,size)
		self.str='You kill '+str(Game.score)+' CaiXuKun.'
		self.Word=self.Font.render(self.str,1,[0,0,0])
		self.fp=[10,10]
	def refresh(self):
		if Game.Gameoven==True:
			self.str='Before it\'s over, you kill '+str(Game.score)+' CaiXuKun.'
		elif Game.Gameoven=='win':
			self.str='The world is not have a CaiXuKun.You win!!!'
		else:
			self.str='You kill '+str(Game.score)+' CaiXuKun.'
		self.Word=self.Font.render(self.str,1,[0,0,0])
		scr.blit(self.Word,self.fp)
#结束定义
#)
'''|##########正式执行##########|'''
#(
#实例创建:
ball=Ball('ck.png',[randint(0,750),20],[10,5])
racket=Racket('lq.png',[0,400],60)
BallGroup=pygame.sprite.Group(ball)
Game=Game(None,None)
Fonts=Fonts('zt.ttf',50)
run=True
scr=display.set_mode((800,600))
clock=time.Clock()
#游戏主循环开始:
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type==QUIT:
			run=False
		if event.type==KEYDOWN:
			racket.obtain_xy()
	#刷新
	Game.refresh()
pygame.quit()
#结束
#)