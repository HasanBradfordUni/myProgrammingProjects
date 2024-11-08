#Other objects
import pygame

class controlsImage(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self):
        super(controlsImage, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the controlsImage as a rectangle in the middle of the screen
        self.image = pygame.image.load('Controls.png').convert()
        self.rect = self.surf.get_rect(center=(960,540))

class instructionsImage(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self):
        super(instructionsImage, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the instructionsImage as a rectangle in the middle of the screen
        self.image = pygame.image.load('Instructions.png').convert()
        self.rect = self.surf.get_rect(center=(960,540))

class winScreen(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self):
        super(winScreen, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the winScreen as a rectangle in the middle of the screen
        self.image = pygame.image.load('Win_Screen.png').convert()
        self.rect = self.surf.get_rect(center=(960,540))

class loseScreen(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self):
        super(loseScreen, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the loseScreen as a rectangle in the middle of the screen
        self.image = pygame.image.load('Lose_Screen.png').convert()
        self.rect = self.surf.get_rect(center=(960,540))

class SS_image(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self):
        super(SS_image, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the SS_image as a rectangle in the middle of the screen
        self.image = pygame.image.load('Save_Screen.png').convert()
        self.rect = self.surf.get_rect(center=(960,540))

class LS_image(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self):
        super(LS_image, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the LS_image as a rectangle in the middle of the screen
        self.image = pygame.image.load('Load_Screen.png').convert()
        self.rect = self.surf.get_rect(center=(960,540))
