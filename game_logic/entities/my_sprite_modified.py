import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
class my_sprite:
    def __init__(self, image_fname, loc=(0,0), size=None):
        self.image_fname = image_fname
        self.loc = loc
        self.image = pygame.image.load(image_fname)
        
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
            
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_image(self):
        return self.image

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
