
import sys
import random
import pygame
VHNUMS = 3
CELLNUMS = VHNUMS * VHNUMS
MAXRANDTIME = 200
# 随机生成游戏盘面
def newgameboard():
    board = []
    for i in range(CELLNUMS):
        board.append(i)#[0,1,2,3,4,5,6,7,8]
    blackcell = CELLNUMS - 1
    board[blackcell] = -1#扣掉最后一张图
    for i in range(MAXRANDTIME):
        direction = random.randint(0, 3)
        if (direction == 0):
            blackcell = moveleft(board, blackcell)
        elif (direction == 1):
            blackcell = moveright(board, blackcell)
        elif (direction == 2):
            blackcell = moveup(board, blackcell)
        elif (direction == 3):
            blackcell = movedown(board, blackcell)
    return board, blackcell

# 若空白图像块不在最左边，则将空白块左边的块移动到空白块位置
def moveright(board, blackcell):
    if blackcell % VHNUMS == 0:
        return blackcell
    board[blackcell - 1], board[blackcell] = board[blackcell], board[blackcell - 1]
    return blackcell - 1
# 若空白图像块不在最右边，则将空白块右边的块移动到空白块位置
def moveleft(board, blackcell):
    if blackcell % VHNUMS == VHNUMS - 1:
        return blackcell
    board[blackcell + 1], board[blackcell] = board[blackcell], board[blackcell + 1]
    return blackcell + 1
# 若空白图像块不在最上边，则将空白块上边的块移动到空白块位置
def movedown(board, blackcell):
    if blackcell < VHNUMS:
        return blackcell
    board[blackcell - VHNUMS], board[blackcell] = board[blackcell], board[blackcell - VHNUMS]
    return blackcell - VHNUMS
# 若空白图像块不在最下边，则将空白块下边的块移动到空白块位置
def moveup(board, blackcell):
    if blackcell >= CELLNUMS - VHNUMS:
        return blackcell
    board[blackcell + VHNUMS], board[blackcell] = board[blackcell], board[blackcell + VHNUMS]
    return blackcell + VHNUMS
# 退出
def gameover():
    pygame.quit()
    sys.exit()
# 是否完成
def isfinished(board,blackcell):
    for i in range(CELLNUMS - 1):
        if board[i] != i:
            return False
    return True

