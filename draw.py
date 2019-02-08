from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #calculates slope
    #changes to second octant if the slope is undefined and goes up
    #changes to seventh octant if the slope is undefined and goes down
    if (x1 - x0 == 0 and y1 - y0 < 0):
        m = -2
    elif (x1 - x0 == 0 and y1 - y0 > 0):
        m = 2
    else:
        m = (y1 - y0)/(x1 - x0)

    #does a and b for the lines
    a = y1 - y0
    b = -(x1 - x0)

    #does things depending on slope
    if  (m > 1):
	print("Doing second octant") 
        second( x0, y0, x1, y1, a, b, screen, color )
    elif (m <= 1 and m >= 0):
	print("Doing first octant")
        first( x0, y0, x1, y1, a, b, screen, color )
    elif(m < 0 and m >= -1):
	print("Doing eighth octant")
	eighth( x0, y0, x1, y1, a, b, screen, color )	
    elif (m < -1):
	print("Doing seventh octant")
        seventh( x0, y0, x1, y1, a, b, screen, color )

#this is for the fist octant
def first( x0, y0, x1, y1, a, b, screen, color ):
    x = x0
    y = y0
    d = 2 * a + b
    while x < x1:
        plot( screen, color, x , y )
        if d > 0:
            y += 1
            d += 2 * b
        x += 1
        d += 2 * a

#this is for the second octant
def second(  x0, y0, x1, y1, a, b, screen, color ):
    x = x0
    y = y0
    d = 2 * b + a
    while y < y1:
        plot( screen, color, x , y )
        if d < 0:
            x += 1
            d += 2 * a
        y += 1
        d += 2 * b

#this is for the seventh octant
def seventh( x0 , y0, x1, y1, a, b, screen, color ):
    x = x0
    y = y0
    d = 2 * a + b
    print(y)
    print(y1)
    while y <= y1:
        plot( screen, color, x , y )
        if d > 0:
            x += 1
            d += 2 * a
        y -= 1
        d -= 2 * a

#this is for the eighth octant
def eighth( x0 , y0, x1, y1, a, b, screen, color ):
    x = x0
    y = y0
    d = 2 * b + a
    while x <= x1:
        plot( screen, color, x , y )
        if d < 0:
            y -= 1
            d -= 2 * b
        x += 1
        d += 2 * a
