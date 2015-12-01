import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
walls = []

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.rect.x > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if self.rect.x < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if self.rect.y > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if self.rect.y < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
        
    def setWalls(self,pWalls):
        global walls 
        walls = pWalls
