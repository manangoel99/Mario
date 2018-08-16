#!/usr/bin/env python3
import os
from Board import Board
from Character import char, Mario
from Scenery import Cloud, Mountain

board = Board()
mario = Mario(board.canvas)

begin = 0

x = 'i'

cloud_list = []
mount_list  = []

while x != 'q':
    os.system("tput reset")
    #print("HAHA", board.canvas[mario.pos[0]])
    #mario.draw(board.canvas)
    if Cloud.tot_clouds < 5:
        x = Cloud()
        if cloud_list != []:
            for cloud in cloud_list:
                if abs(x.pos_x - cloud.pos_x) > 20 and abs(x.pos_y - cloud.pos_y) > 10:
                    Cloud.tot_clouds += 1
                    x.draw(board.canvas)
                    cloud_list.append(x)
        else:
            x.draw(board.canvas)
            Cloud.tot_clouds += 1
            cloud_list.append(x)
    
    if Mountain.tot_mountains < 5:
        x = Mountain()
        if mount_list != []:
            for mountain in mount_list:
                if abs(x.pos_x - mountain.pos_x) > 30:
                    Mountain.tot_mountains += 1
                    x.draw(board.canvas)
                    mount_list.append(x)
        else:
            x.draw(board.canvas)
            Mountain.tot_mountains += 1
            mount_list.append(x)
                


    board.draw()
    mario.move_mario(board, board.canvas)
    board.draw()
    
        
    #x = input()
