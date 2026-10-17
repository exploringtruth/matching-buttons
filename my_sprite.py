import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class my_sprite:
    def __init__(self, image_fname, loc=(0, 0)):
        self.image_fname = image_fname
        self.loc = loc
        self.image = pygame.image.load(image_fname)

    def get_image(self):
        return self.image

    def get_width(self):
        return pygame.Surface.get_width(self.image)

    def get_height(self):
        return pygame.Surface.get_height(self.image)
