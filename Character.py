import signal
import time

from alarmexception import AlarmException
from Board import Board
from getch import _getChUnix as getChar
from Global import *


class char():
    
    str = []
    pos = []
    direction = 'right'

class Mario(char):
    def __init__(self, canvas):
        '''Generate Mario'''
        self.str.append(['M', 'M'])
        self.str.append(['M', 'M'])
        self.pos.append(NUM_ROWS - NUM_STONE_ROWS - 3)
        self.pos.append(5)
        
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos[0] + i][self.pos[1] + j] = self.str[i][j]
    
    def move_mario(self, board, canvas):
        """Moves Mario"""
        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        c = user_input()
        #   board.draw()

        if c == 'q':
            quit()
        
        if c == 'd':
            self.pos[1] += 1
            for i in range(len(self.str)):
                for j in range(len(self.str[i])):
                    canvas[self.pos[0] + i][self.pos[1] + j] = self.str[i][j]
            
            canvas[self.pos[0]][self.pos[1] - 1] = ' '
            canvas[self.pos[0] + 1][self.pos[1] - 1] = ' '
            self.direction = 'right'
            #board.draw()
        
        if c == 'a':
            self.pos[1] -= 1
            for i in range(len(self.str)):
                for j in range(len(self.str[i])):
                    canvas[self.pos[0] + i][self.pos[1] + j] = self.str[i][j]

            canvas[self.pos[0]][self.pos[1] + 2] = ' '
            canvas[self.pos[0] + 1][self.pos[1] + 2] = ' '
            self.direction = 'left'
            #board.draw()
        
        if c == 'w':
            if self.direction == "right":
                for i in range(1, 10):
                    self.pos[0] -= 1
                    self.pos[1] += 1
                    for i in range(len(self.str)):
                        for j in range(len(self.str[i])):
                            canvas[self.pos[0] + i][self.pos[1] + j] = self.str[i][j]
                    
                    canvas[self.pos[0] + 1][self.pos[1] - 1] = ' '
                    canvas[self.pos[0] + 2][self.pos[1] - 1] = ' '
                    canvas[self.pos[0] + 2][self.pos[1]] = ' '
                    #canvas[self.pos[0] + 1][self.pos[1] - 1] = ' '
                    board.draw()
                    time.sleep(0.05)

                for i in range(1, 10):
                    self.pos[0] += 1
                    self.pos[1] += 1
                    for i in range(len(self.str)):
                        for j in range(len(self.str[i])):
                            canvas[self.pos[0] + i][self.pos[1] +
                                                    j] = self.str[i][j]

                    canvas[self.pos[0] - 1][self.pos[1] - 1] = ' '
                    canvas[self.pos[0] - 1][self.pos[1]] = ' '
                    canvas[self.pos[0]][self.pos[1] - 1] = ' '
                    #canvas[self.pos[0] + 1][self.pos[1] - 1] = ' '
                    board.draw()
                    time.sleep(0.05)

            if self.direction == "left":
                
                
                for i in range(1, 10):
                    self.pos[0] -= 1
                    self.pos[1] -= 1
                    for i in range(len(self.str)):
                        for j in range(len(self.str[i])):
                            canvas[self.pos[0] + i][self.pos[1] +
                                                    j] = self.str[i][j]

                    canvas[self.pos[0] + 1][self.pos[1] + 2] = ' '
                    canvas[self.pos[0] + 2][self.pos[1] + 2] = ' '
                    canvas[self.pos[0] + 2][self.pos[1] + 1] = ' '
                    #canvas[self.pos[0] + 1][self.pos[1] - 1] = ' '
                    board.draw()
                    time.sleep(0.05)
                
                
                for i in range(1, 10):
                    self.pos[0] += 1
                    self.pos[1] -= 1
                    for i in range(len(self.str)):
                        for j in range(len(self.str[i])):
                            canvas[self.pos[0] + i][self.pos[1] +
                                                    j] = self.str[i][j]

                    canvas[self.pos[0]][self.pos[1] + 2] = ' '
                    canvas[self.pos[0] - 1][self.pos[1] + 2] = ' '
                    canvas[self.pos[0] - 1][self.pos[1] + 1] = ' '
                    #canvas[self.pos[0] + 1][self.pos[1] - 1] = ' '
                    board.draw()
                    time.sleep(0.05)
                
