from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #finds slope of the line and does the appropriate line drawer
    undefined = true
    if (x1 - x0 == 0 and y1 - y):
        undefined = true
        m = null
    else:
        undefined = false
        m = (y1 - y0)/(x1 - x0)
        
    if (m == null):
        q()
    elif (m <= 1 and m >= 0):
        firstq()
    elif (m > 1):
        secondq()
    elif(m < 0 and m >= -1):
        eighthq()
    elif (m < -1):
        seventhq()

def firstq()
            
