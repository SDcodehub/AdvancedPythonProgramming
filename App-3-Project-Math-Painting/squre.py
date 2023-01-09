from PIL import Image


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        rw_start = self.x-1
        rw_end = self.x+self.side - 1
        col_start = self.y-1
        col_end = self.y + self.side - 1

        data = canvas.make()
        data[rw_start:rw_end, col_start:col_end] = self.color

        return Image.fromarray(data, 'RGB')
