import random

class Shape:
    x=0
    y=0

    shape_I=[[1, 5, 9, 13], [4, 5, 6, 7]]
    shape_J=[[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]]
    shape_L=[[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]
    shape_T=[[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
    shape_Q=[[1, 2, 5, 6]]
    shape_S=[[1, 2, 4, 5], [1, 5, 6, 10]]
    shape_Z=[[0, 1, 5, 6], [2, 5, 6, 9]]
    shapes=[shape_I, shape_J, shape_L, shape_T, shape_Q, shape_S, shape_Z]

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.type=random.randint(0,len(self.shapes)-1)
        self.color=random.randint(1,len(colors)-1)
        self.rotation=0
    
    def image(self):
        return self.shapes[self.type][self.rotation]
    
    def rotate(self):
        self.rotation=(self.rotation + 1) % len(self.shapes[self.type])
