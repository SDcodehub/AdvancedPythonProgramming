import numpy as np


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self):
        # Numpy array
        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Overwritte color
        data[:] = self.color

        return data
