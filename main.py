from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0, 250, 500, 250, screen, color)
draw_line(0, 250, 0, 500, screen, color)
draw_line(0, 250, 0, -500, screen, color)
draw_line(0, 250, 250, 500, screen, color)
draw_line(0, 250, 250, -500, screen, color)
draw_line(0, 250, 500, 500, screen, color)
draw_line(0, 250, 500, -500, screen, color)
draw_line(0, 250, 125, -500, screen, color)
draw_line(0, 250, 125, 500, screen, color)


display(screen)
save_extension(screen, 'img.png')
