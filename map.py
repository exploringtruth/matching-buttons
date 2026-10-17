import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
class map:
    def __init__(self, screen):
        self.canvas = screen

    def update(self, obj_list):
        for obj in obj_list:
            self.canvas.blit(obj.get_image(), obj.loc)
        pygame.display.flip()