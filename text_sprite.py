import pygame

class text_sprite:
    def __init__(self, text, size=32, color=(255, 255, 255), loc=(0, 0)):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect(center=loc)
        self.loc = loc

    def get_image(self):
        return self.image

    def update(self):
        pass
