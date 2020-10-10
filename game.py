from gamescreen import *
from move import *
from game1 import *
import pygame
from pygame.locals import *
import time
def run_game(gameImage):
    # 加载背景音乐
    pygame.mixer.music.load('sound/backsound.mp3')
    screen = pygame.display.set_mode((gameRect.width, gameRect.height + 100))
    gameboard, blackcell = newgameboard()
    finish = False
    n1 =False
    cnt =0;#步数记录
    pygame.mixer.music.play(-1, 0.0)
    shengyin = 2
    while True:
        buttons = pygame.mouse.get_pressed()#判断是否按下鼠标
        x1, y1 = pygame.mouse.get_pos()#获取鼠标坐标
        if x1 >= gameRect.width / 2-100 and x1 <= gameRect.width /2+ 100and y1 >= gameRect.height and y1 <= gameRect.height + 100:#重玩游戏
            if buttons[0]:
                n1 = True
        if x1 >= 30 and x1 <= 120 and y1 >= gameRect.height and y1 <= gameRect.height + 100:#打开声音
            if buttons[0]:
                shengyin = 1
        if x1 >= gameRect.width-150 and x1 <= gameRect.width and y1 >= gameRect.height and y1 <= gameRect.height + 100:#关掉声音
            if buttons[0]:
                shengyin = 0
        for event in pygame.event.get():#事件监听
            if event.type == QUIT:#退出
                gameover()
            if finish:
                 continue
            # 鼠标键盘事件
            # 开始游戏，点击鼠标
            if event.type == KEYDOWN:#键盘事件
                if event.key == K_LEFT or event.key == ord('a'):
                    blackcell = moveleft(gameboard, blackcell)
                if event.key == K_RIGHT or event.key == ord('d'):
                    blackcell = moveright(gameboard, blackcell)
                if event.key == K_UP or event.key == ord('w'):
                    blackcell = moveup(gameboard, blackcell)
                if event.key == K_DOWN or event.key == ord('s'):
                    blackcell = movedown(gameboard, blackcell)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:#鼠标事件
                x, y = pygame.mouse.get_pos()
                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * VHNUMS
                if (index == blackcell - 1 or index == blackcell + 1 or index == blackcell - VHNUMS or index == blackcell + VHNUMS):
                        gameboard[blackcell], gameboard[index] = gameboard[index], gameboard[blackcell]
                        blackcell = index
                        cnt = cnt+1
            if (isfinished(gameboard, blackcell)):
                gameboard[blackcell] = CELLNUMS - 1
                finish = True
            screen.fill(bg)
            # 图像分割并打乱
            for i in range(CELLNUMS):
                rowDst = int(i / VHNUMS)
                colDst = int(i % VHNUMS)
                rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)
                if gameboard[i] == -1:
                    continue
                rowArea = int(gameboard[i] / VHNUMS)
                colArea = int(gameboard[i] % VHNUMS)
                rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
                screen.blit(gameImage, rectDst, rectArea)

            # 绘制边框线
            for i in range(VHNUMS + 1):
                pygame.draw.line(screen, white, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
            for i in range(VHNUMS + 1):
                pygame.draw.line(screen, white, (0, i * cellHeight), (gameRect.width, i * cellHeight))
            #在拼图成功后在屏幕上显示
            if(finish == True):
                pygame.mixer.music.stop()
                #pygame.mixer.music.load('sound/win.mp3')
                drawText('Congratulation!', font, screen, (gameRect.width / 2) - 110, (gameRect.height / 2))
                pygame.display.update()
                #pygame.mixer.music.stop()  # 游戏结束声音停止
            #显示步数
            drawText('cnt: %s' % (str(cnt)),font,screen,0,0)
            #图标
            screen.blit(restart,(gameRect.width/2-150,gameRect.height))#重新开始的图标
            screen.blit(silence, (30, gameRect.height))#静音图标
            screen.blit(voice, (gameRect.width-150, gameRect.height))#重新打开声音的图标
            pygame.display.update()
            mainClock.tick(FPS)
            #pygame.mixer.music.play()  # 播放游戏结束时声音
            #if (n1 == True):
                #run_game()
        if (shengyin==1):#静音
            pygame.mixer.music.pause()
        elif(shengyin ==0):#打开声音
            pygame.mixer.music.unpause()
        if (n1 == True):#重新开始
            run_game(gameImage)



