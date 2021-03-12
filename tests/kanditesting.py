from helpermodules.kandi import *
from helpermodules.ion import *
from pygame.constants import *

for x in range(xSize):
    for y in range(ySize):
        pygame.event.pump()
        r = scaleTo(x + y + 1, xSize + ySize)
        set_pixel(x, y, color(r, r, r))
        if keydown(K_KP1):
            pygame.exit()
