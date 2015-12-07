import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self,direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.direction = direction
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        
    def update(self):
        """ Move the bullet. """
        if self.direction == "up":
            self.rect.y -= 3
        elif self.direction == "down":
            self.rect.y += 3
        elif self.direction == "left":
            self.rect.x -= 3
        elif self.direction == "right":
            self.rect.x += 3
