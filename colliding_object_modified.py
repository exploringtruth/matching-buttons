import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from my_sprite_modified import my_sprite
from image_switcher import image_switcher

class colliding_object(my_sprite):
    def __init__(self, image_fname, loc=(0,0), size=None, other_image_fname=None):
        super().__init__(image_fname, loc, size)

        if other_image_fname:
            self.switcher = image_switcher(self, other_image_fname, size)
        else:
            self.switcher = None

        self.bounding_box = pygame.Rect(self.loc[0], self.loc[1], self.get_width(), self.get_height())

    def get_bounding_box(self):
        return self.bounding_box

    def is_colliding_with(self, co):
        return self.bounding_box.colliderect(co.get_bounding_box())

    def set_active_state(self, active):
        if self.switcher:
            self.switcher.switch_image(active)

    def get_active_state(self):
        if self.switcher:
            return self.switcher.is_active
        return False
