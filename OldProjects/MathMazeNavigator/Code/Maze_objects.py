#Maze objects
import pygame

#set up the 'Wall' class
class Wall(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255,255,255))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))

#set up the 'Cell' class
class Cell(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0,0,255))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))

#set up the 'Empty' class
class Empty(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0,0,0))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))

