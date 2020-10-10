from move import *
import pygame
import random
 # 初始化Pygame
pygame.init()
bg = (255, 255, 255)#白色背景
black = (0, 0, 0)
white = (255,255,255)
TEXTCOLOR = (255, 0, 0) #字体颜色
FPS = 40
mainClock = pygame.time.Clock()
#设置窗口标题
pygame.display.set_caption('字母九宫格拼图')
# 加载图片
#n = random.randint(1,15)
#gameImage = pygame.image.load('images/' + str(n) + '.jpg')
#yuantu = gameImage
mubanImage = pygame.image.load('images/2.jpg')
#gameImage = pygame.image.load('images/1.jpg')
gameRect = mubanImage.get_rect()
 # 创建指定大小的窗口
#screen = pygame.display.set_mode((gameRect.width+60, gameRect.height+100))
screen = pygame.display.set_mode((820,860))
screen1 = pygame.Surface(screen.get_size())
screen2 = pygame.Surface(screen.get_size())
#screen3 = pygame.Surface(screen.get_size())
screen1.fill((255,255,255))
screen1 = screen1.convert()
#yuantu.convert()

# set up fonts设置字体
font = pygame.font.SysFont(None, 48)
# 加载图标图片
startgame = pygame.image.load('images/startgame.png')
startgame.convert()
restart =pygame.image.load('images/restart.png')
voice = pygame.image.load('images/voice.png')
silence = pygame.image.load('images/silence.png')
#获取切割的每一块小图片的高度和宽度
cellWidth = int(gameRect.width / VHNUMS)
cellHeight = int(gameRect.height / VHNUMS)
gameboard, blackcell = newgameboard()
#在屏幕上显示文字
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    #draw one image onto another
    surface.blit(textobj, textrect)