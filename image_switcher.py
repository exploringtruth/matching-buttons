import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
class image_switcher:
    def __init__(self, sprite, active_image_path, size=None):
        self.sprite = sprite
        self.normal_image = sprite.get_image()

        active_loaded = pygame.image.load(active_image_path)
        self.active_image = pygame.transform.scale(active_loaded, size) if size else active_loaded
        self.is_active = False

    def switch_image(self, active: bool):
        self.is_active = active
        if active:
            self.sprite.image = self.active_image
        else:
            self.sprite.image = self.normal_image
