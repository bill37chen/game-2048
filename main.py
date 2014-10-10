__author__ = 'Bill'
from game import game
import msvcrt


if __name__ == '__main__':
    newgame = game()
    newgame.start()
    while not newgame.result:
        print "please move:"
        c = msvcrt.getch()
        c = c.upper()
        if c not in ["W", "S", "A", "D"]:
            print "wrong input"
        else:
            newgame.run(c)