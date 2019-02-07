from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #finds slope of the line and does the appropriate line drawer
    undefined = true

    #calculates slope and does undefined if the x's are the same
    if (x1 - x0 == 0 and y1 - y0 <= 0):
        m = -1
    elif (x1 - x0 == 0 and y1 - y0 >= 0):
        m = 1
    else:
        undefined = false
        m = (y1 - y0)/(x1 - x0)

    #does a and b for the lines
    a = y1 - y0
    b = x1 - x0

    #does things depending on slope
    if ((undefined == true and m == 1) or m > 1):
        secondq( x0, y0, x1, y1, a, b, screen, color )
    elif (m <= 1 and m >= 0):
        firstq( x0, y0, x1, y1, a, b, screen, color )
    elif(m < 0 and m >= -1):
        eighthq( x0, y0, x1, y1, a, b, screen, color )
    elif ((undefined == true and m == -1) or  m < -1):
        seventhq( x0, y0, x1, y1, a, b, screen, color )

def firstq( x0, y0, x1, y1, a, b, screen, color ):
    x = x0
    y = y0
    d = 2 * a + b
    while x < x1:
        plot( x , y )
        if d > 0
            y++
            d += 2b
        x++
        d += 2a

def secondq(  x0, y0, x1, y1, a, b, screen, color ):
    x = x0
    y = y0
    d = 2 * b + a
    while y < y1:
        plot( x , y)
        if d < 0:
            x++
            d += 2a
        y++
        d += 2b
