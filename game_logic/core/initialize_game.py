import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
class initialize_game:
    def __init__(self, set_size=(1200,800), caption="Game"):
        self.set_size = set_size
        self.caption = caption
        self.screen = self.initialize_game()

    def initialize_game(self):
        pygame.init()
        screen = pygame.display.set_mode(self.set_size)
        pygame.display.set_caption(self.caption)
        return screen