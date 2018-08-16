import random

class Cloud():
    
    tot_clouds = 0

    def __init__(self):
        self.str = [

            [' ', ' ', ' ', '_', '_', ' ', ' ', ' ', '_', ' ', ' ', ' '],
            [' ', '_', '(', ' ', ' ', ')', '_', '(', ' ', ')', '_', ' '],
            ['(', '_', ' ', ' ', ' ', '_', ' ', ' ', ' ', ' ', '_', ')'],
            [' ', ' ', '(', '_', ')', ' ', '(', '_', '_', ')', ' ', ' ']

        ]

        self.pos_x = random.randint(0, 15)
        self.pos_y = random.randint(0, 180)

    def draw(self, canvas):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos_x + i][self.pos_y + j] = self.str[i][j]


class Mountain():
    
    tot_mountains = 0
    def __init__(self):
        self.str = [

            [' ', ' ', ' ', '/', '\\', ' ', ' ', ' '],
            [' ', ' ', '/', ' ', ' ', '\\', ' ', ' '],
            [' ', '/', ' ', ' ', ' ', ' ', '\\', ' '],
            ['/', ' ', ' ', ' ', ' ', ' ', ' ', '\\'],
            
        ]
        
        self.pos_x = 34
        self.pos_y = random.randint(0, 150)

    def draw(self, canvas):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos_x + i][self.pos_y + j] = self.str[i][j]
