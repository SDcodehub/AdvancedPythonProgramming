from PIL import Image


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        rw_start = self.x - 1
        rw_end = self.x + self.height - 1
        col_start = self.y - 1
        col_end = self.y + self.width - 1

        data = canvas.make()
        data[rw_start:rw_end, col_start:col_end] = self.color

        return Image.fromarray(data, 'RGB')
