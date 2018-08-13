#!/usr/bin/env python3
import os
from Board import Board
from Character import char, Mario

board = Board()
mario = Mario(board.canvas)

begin = 0

x = 'i'

while x != 'q':
    os.system("tput reset")
    #print("HAHA", board.canvas[mario.pos[0]])
    #mario.draw(board.canvas)
    board.draw()
    mario.move_mario(board, board.canvas)
    #x = input()
