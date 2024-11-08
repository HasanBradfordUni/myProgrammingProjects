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
        self.__location = location
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(self.__location))

    def getLocation(self): #set up the function to get the location
        return self.__location #return the location to the main program

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

class Key(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0,0,0))
        #set the sprite's image
        self.image = pygame.image.load(image_file).convert()
        #set up the key as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))

