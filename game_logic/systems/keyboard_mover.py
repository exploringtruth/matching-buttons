import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
class keyboard_mover:
    def __init__(self, vehicle, up, left, down, right, grab_key, speed=5):
        self.vehicle = vehicle
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.click_key = grab_key
        self.speed = speed

    def update(self):
        pressedKeys = pygame.key.get_pressed()        
        x, y = self.vehicle.loc
    
        if pressedKeys[self.up]:
            y -= self.speed
        if pressedKeys[self.down]:
            y += self.speed
        if pressedKeys[self.left]:
            x -= self.speed
        if pressedKeys[self.right]:
            x += self.speed

        self.vehicle.set_location((x, y))

        if pressedKeys[self.click_key]:
            self.vehicle.set_active_state(True)
        else:
            self.vehicle.set_active_state(False)
