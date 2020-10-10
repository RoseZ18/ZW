from game import *
from game1 import *
if __name__ == '__main__':
        n = random.randint(1, 15)
        gameImage=run_beforegame(n)
        run_game(gameImage)