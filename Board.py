from Global import *

class Board():
    canvas = [[] for i in range(NUM_ROWS)]

    def __init__(self):
        for i in self.canvas:
            for j in range(NUM_COLS):
                i.append(' ')
            i.append('\n')

        for i in range(NUM_ROWS - NUM_STONE_ROWS, NUM_ROWS):
            for j in range(0, NUM_COLS, 4):
                self.canvas[i][j] = '|'
                self.canvas[i][j + 1] = '_'
                self.canvas[i][j + 2] = '_'
                self.canvas[i][j + 3] = '|'
        
        for i in range(NUM_COLS):
            self.canvas[NUM_ROWS - NUM_STONE_ROWS - 1][i] = '_'
    
    def draw(self):
        for i in self.canvas:
            for j in i:
                print(j,end="")
