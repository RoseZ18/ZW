from gamescreen import *
from move import *
import pygame
from pygame.locals import *
# 加载图片

newimage=pygame.image.load('images/newimage.png')
#gameImage = pygame.image.load('images/' + str(n) + '.jpg')
def run_beforegame(n):
    gameImage = pygame.image.load('images/' + str(n) + '.jpg')
    yuantu = gameImage
    n1 = True
    flag = True
    while n1:

        screen.blit(screen1,(0,0))
        screen1.blit(yuantu, (30, 0))
        screen1.blit(startgame, (30, gameRect.height))
        screen1.blit(newimage,(gameRect.width-220,gameRect.height))
        pygame.display.update()
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= 30 and x1 <= 220+30 and y1 >=  gameRect.height and y1 <=  gameRect.height+80:
            if buttons[0]:
                n1 = False

        #更换图片
        if x1 >= gameRect.width-220 and x1 <= gameRect.width+100 and y1 >=  gameRect.height and y1 <=  gameRect.height+80:
            if buttons[0]:
                flag = False
        if flag == False:
            n = random.randint(1, 15)
            gameImage = pygame.image.load('images/' + str(n) + '.jpg')
            yuantu = gameImage
            flag =True
        # 下面是监听退出动作
        # 监听事件
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")
                # quit 卸载所有的模块
                pygame.quit()
                # exit() 直接终止当前正在执行的程序
                exit()
    screen.blit(screen2, (0, 0))
    pygame.display.update()
    return gameImage
