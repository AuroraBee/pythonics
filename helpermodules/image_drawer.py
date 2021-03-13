from PIL import Image
from helpermodules.kandi import *


def draw_image(file, x, y):
    with Image.open("images/" + file + ".png", "r").convert("RGB") as image:
        pixels = image.load()
        width, height = image.size

    pygame.event.pump()
    for ImgX in range(width):
        pygame.event.pump()
        for ImgY in range(height):
            pygame.event.pump()
            set_pixel(x + ImgX, y + ImgY, pixels[ImgX, ImgY])





