from kandinsky import *
from ion import *
from pygame.constants import *
from time import *


class testmodule:
    def __init__(self, x=50, y=50, c=color(0, 255, 128)):
        self.x = x
        self.y = y
        self.c = c

    def move(self, v = 2):
        if keydown(K_LEFT):
            self.x -= v
        if keydown(K_RIGHT):
            self.x += v
        if keydown(K_UP):
            self.y -= v
        if keydown(K_DOWN):
            self.y += v
        self.draw()

    def draw(self):
        fill_rect(self.x - 2, self.y - 2, 5, 5, self.c)


p = testmodule()
i = 0
t = 0
pygame.event.pump()
while not t:
    pygame.event.pump()
    t = keydown(K_UNDERSCORE)
    p.move()
    sleep(0.15)

print("closed")
