import pygame
from pygame.constants import *


def keydown(key):
    pressed = pygame.key.get_pressed()
    if pygame.key.get_focused():
        if pressed[key]:
            return 1
