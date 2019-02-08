from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# 0 slope
#draw_line(250, 250, 500, 250, screen, color)
# undefined slope (up)
#draw_line(250, 250, 250, 500, screen, color)

# undefined slope (down)
draw_line(250, 250, 250, 0, screen, color)

# 1 slope (45 degrees)
#draw_line(250, 250, 500, 500, screen, color)

# -1 slope (315 degrees)
#draw_line(250, 250, 500, 0, screen, color)

# 1.5 slope (67.5 degrees)
#draw_line(250, 250, 375, 500, screen, color)

# -1.5 slope (-292.5 degrees)
#draw_line(250, 250, 375, 0, screen, color)

# 0.5 slope (22.5 degrees)
#draw_line(250, 250, 500, 375, screen, color)

# -0.5 slope (337.5 degrees)
#draw_line(250, 250, 500, 125, screen, color)



display(screen)
save_extension(screen, 'img.png')
