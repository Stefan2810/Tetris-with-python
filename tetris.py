from shape import Shape

class Tetris:
    level=2
    score=0
    state="start"
    grid=[]
    height=0
    width=0
    x=100
    y=60
    zoom=20
    shape=None
    '''we create a grid with the size height * width'''
    def __init__(self,h,w):
        self.height=h
        self.width=w
        for i in range(self.height):
            line=[]
            for j in range(self.width):
                line.append(0)
            self.grid.append(line)
    def new_shape(self):
        self.shape=Shape(3,0)

    def intersects(self):
        intersection=False
        for i in range(4):
            for j in range(4):
                if i*4+j in self.shape.image():
                    if i + self.shape.y > self.height - 1 or j + self.shape.x > self.width - 1 or j + self.shape.x < 0 or self.grid[i + self.shape.y][j + self.shape.x] > 0:
                        intersection = True
        return intersection

    def completed_line(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.grid[i1][j] = self.grid[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.shape.y += 1
        self.shape.y -= 1
        self.freeze()

    def go_down(self):
        self.shape.y += 1
        if self.intersects():
            self.shape.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.image():
                    self.grid[i + self.shape.y][j + self.shape.x] = self.shape.color
        self.completed_line()
        self.new_shape()
        if self.intersects():
            self.state = "game_over"

    def go_side(self, dx):
        old_x = self.shape.x
        self.shape.x += dx
        if self.intersects():
            self.shape.x = old_x

    def rotate(self):
        old_rotation = self.shape.rotation
        self.shape.rotate()
        if self.intersects():
            self.shape.rotation = old_rotation
