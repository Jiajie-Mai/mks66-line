from display import *
from draw import *
from random import *
import math

screen = new_screen()
color = [ 0, 100, 0 ]

def colorRand():
    i = 0
    while i < 3:
        color.insert( i ,randint( 100, 200 ) )
        i += 1

def thing():
    
    print(x0, y0, x1, y1)
    draw_line( x0, y0, x1, y1, screen, color)

x0 = 0
y0 = 500
x1 = 500
y1 = 0

print("\nDoing first part\n")
while x1 >= 0:
    thing()
    x1 -= 20
    
x1 = 500
y1 = 500

print("\nDoing second part\n")
while y1 >= 0:
    thing()
    y1 -= 20

y0 = 0
x1 = 500
y1 = 500

print("\nDoing third part\n")
while x1 >= 0:
    thing()
    x1 -= 20

    
x1 = 500

print("\nDoing fourth part\n")
while y1 >= 0:
    thing()
    y1 -= 20

x0 = 0
y0 = 500
x1 = 500
y1 = 500

print("\nDoing fifth part\n")
while y0 >= 0:
    thing()
    y0 -= 20

x0 = 500
y0 = 0

print("\nDoing sixth part\n")
while x0 >= 0:
    thing()
    x0 -= 20

x0 = 500
y0 = 500
x1 = 500
y1 = 0
    
print("\nDoing seventh part\n")
while x0 >= 0:
    thing()
    x0 -= 20

print("\nDoing eigth part\n")
while y0 >= 0:
    thing()
    y0 -= 20

'''
# 0 slope
draw_line(250, 250, 500, 250, screen, color)
colorRand()
# undefined slope (up)
draw_line(250, 250, 250, 500, screen, color)
colorRand()
# undefined slope (down)
draw_line(250, 250, 250, 0, screen, color)
colorRand()
# 1 slope (45 degrees)
draw_line(250, 250, 500, 500, screen, color)
colorRand()
# -1 slope (315 degrees)
draw_line(250, 250, 500, 0, screen, color)
colorRand()
# 1.5 slope (67.5 degrees)
draw_line(250, 250, 375, 500, screen, color)
colorRand()
# -1.5 slope (-292.5 degrees)
draw_line(250, 250, 375, 0, screen, color)
colorRand()
# 0.5 slope (22.5 degrees)
draw_line(250, 250, 500, 375, screen, color)
colorRand()
# -0.5 slope (337.5 degrees)
draw_line(250, 250, 500, 125, screen, color)
'''


display(screen)
save_extension(screen, 'img.png')
