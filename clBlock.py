import pygame
import random
import vectors as v

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

walls = []

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        self.set_target((10, 10))
        self.speed = 0.7
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
    
    def setXY(self,x,y):
        self.x = x
        self.y = y
    @property
    def pos(self):
        return self.x, self.y

    # for drawing, we need the position as tuple of ints
    # so lets create a helper property
    @property
    def int_pos(self):
        return map(int, self.pos)
        
    @property
    def target(self):
        return self.t_x, self.t_y

    @property
    def int_target(self):
        return map(int, self.target) 
        
    def set_target(self, pos):
        self.t_x, self.t_y = pos
            
    def update(self):
        #self.rect.y -= 1
        target_vector = v.sub(self.target, self.pos) 
        move_vector = [c * self.speed for c in v.normalize(target_vector)]
        self.x, self.y = v.add(self.pos, move_vector)
        self.rect.x = self.x
        self.rect.y = self.y
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

        
