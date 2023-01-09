import os

from canvas import Canvas
from rectangle import Rectangle
from squre import Square

canvas_height = int(input('Enter canvas height: '))
canvas_width = int(input('Enter canvas width: '))
canvas_color = input('Enter canvas color, black or white: ')

if canvas_color.capitalize() == 'White':
    color = [255, 255, 255]
elif canvas_color.capitalize() == 'Black':
    color = [0, 0, 0]
else:
    color = [0, 0, 0]

can = Canvas(canvas_width, canvas_height, color)

shape = input('Enter shape of canvas, rectangle or square: ')
start_pt_x = int(input('Enter start point of canvas row: '))
start_pt_y = int(input('Enter start point of canvas col: '))

if shape.capitalize() == 'Square':
    side = int(input('Enter side of square: '))

    color_1 = int(input('Enter first color, r, 0-255: '))
    color_2 = int(input('Enter second color, g, 0-255: '))
    color_3 = int(input('Enter third color, b, 0-255: '))
    sqr_color = [color_1, color_2, color_3]

    sqr = Square(start_pt_x, start_pt_y, side, sqr_color)
    img = sqr.draw(can)
elif shape.capitalize() == 'Rectangle':
    width = int(input('Enter width of rectangle: '))
    height = int(input('Enter height of rectangle: '))

    color_1 = int(input('Enter first color, r, 0-255: '))
    color_2 = int(input('Enter second color, g, 0-255: '))
    color_3 = int(input('Enter third color, b, 0-255: '))
    rect_color = [color_1, color_2, color_3]

    rect = Rectangle(start_pt_x, start_pt_y, width, height, rect_color)
    img = rect.draw(can)
else:
    pass



side = 2
sqr_color = [255, 0, 0]



# Change dir to files else use default
os.chdir('files')
img.save(f'canvas.png')