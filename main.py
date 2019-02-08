from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#0 slope
draw_line(250, 250, 500, 250, screen, color)
#undefined slope (up)
draw_line(250, 250, 250, 500, screen, color)
#undefined slope (down)
draw_line(250, 250, 250, -500, screen, color)
#1 slope
draw_line(250, 250, 500, 500, screen, color)
#-1 slope
draw_line(250, 250, 500, -500, screen, color)



display(screen)
save_extension(screen, 'img.png')
