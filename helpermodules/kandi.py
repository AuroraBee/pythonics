# coding : utf-8
import pygame
import threading
import time
from helperModules import scaleTo

scale = 3  # change the value to scale up the screen

xSize = 320 # round(scaleTo(3, 5, 1980))
ySize = 222 # round(scaleTo(3, 5, 1080))+1
yOffset = 1

pygame.init()
# pygame.display.init()
screen = pygame.display.set_mode((xSize * scale, ySize * scale))
pygame.display.set_caption("Python Screen (kandi-lib)")
pygame.draw.rect(screen, (255, 255, 255), (0, yOffset * scale, (xSize - yOffset) * scale, ySize * scale))

pygame.display.flip()

font = pygame.font.Font("SourceCodeVariable-Roman.ttf", 8)


class flip(threading.Thread):
    pygame.event.pump()
    r = 1

    def run(self):
        while self.r:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.r = 0
            pygame.display.flip()
            time.sleep(0.05)


f = flip()

f.start()


def color(r, g, b):
    if r >= 256:
        r = 255
    if g >= 256:
        g = 255
    if b >= 256:
        b = 255
    pygame.event.pump()
    r = round(r)
    g = round(g)
    b = round(b)
    return r, g, b


def set_pixel(x, y, color):
    pygame.event.pump()
    red = color[0]
    green = color[1]
    blue = color[2]

    assert red <= 255
    assert green <= 255
    assert blue <= 255

    # screen.set_at((x*scale, (y+yOffset)*scale), (red, green, blue))
    pygame.draw.rect(screen, (red, green, blue),
                     pygame.rect.Rect(x * scale, (y + yOffset) * scale, scale, scale))
    # gfxdraw.pixel(screen, x, y+yOffset, (red, green, blue))


def fill_rect(x, y, width, height, color):
    pygame.event.pump()
    pygame.draw.rect(screen, color,
                     pygame.rect.Rect(x * scale, (y + yOffset) * scale, width * scale, height * scale))


def draw_string(text, x, y, color1=(0, 0, 0), color2=(255, 255, 255)):
    pygame.event.pump()
    try:
        screen.blit(font.render(text, True, color1, background=color2),
                    (x * scale, (y + yOffset) * scale))
        pygame.display.flip()
    except Exception:
        print(text, "at:", x, y, "with colour", color1, color2)
    pass


def get_pixel(x, y):
    pygame.event.pump()
    w = screen.get_at((x * scale, (y + yOffset) * scale))

    if x < 0 or x > 320 or y < 0 or y > 222:
        w = [0, 0, 0]

    red = w[0]
    green = w[1]
    blue = w[2]
    return red, green, blue
