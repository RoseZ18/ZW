from game import *
from game1 import *
if __name__ == '__main__':
        n = random.randint(1, 15)
        gameImage=run_beforegame(n)#开始界面并从开始游戏界面获取目标图片
        run_game(gameImage)#进入游戏界面