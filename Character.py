from Global import *
from Board import Board

class char():
    
    str = []
    pos = []

    def __init__(self, canvas, type="enemy"):
        if type == "mario":
            self.str.append(['M', 'M'])
            self.str.append(['M', 'M'])
            self.pos.append(NUM_ROWS - NUM_STONE_ROWS - 3)
            self.pos.append(5)

            for i in range(len(self.str)):
                for j in range(len(self.str[i])):
                    canvas[self.pos[0] + i][self.pos[1] + j] = self.str[i][j]