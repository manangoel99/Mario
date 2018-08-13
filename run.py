import os
from Board import Board
from Character import char

board = Board()
mario = char(board.canvas, type="mario")

x = 'i'

while x != 'q':
    os.system("tput reset")
    #print("HAHA", board.canvas[mario.pos[0]])
    #mario.draw(board.canvas)
    board.draw()
    x = input()
