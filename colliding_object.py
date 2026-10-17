import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from my_sprite_modified import my_sprite

class colliding_object(my_sprite):
    def __init__(self, image_fname, loc=(0, 0)):
        super().__init__(image_fname, loc)
        self.bounding_box = pygame.Rect(loc[0], loc[1], self.get_width(), self.get_height())

    def get_bounding_box(self):
        return self.bounding_box

    def is_colliding_with(self, co):
        return self.bounding_box.colliderect(co.get_bounding_box())
