#Other objects
import pygame

class controlsImage(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, width, height):
        super(controlsImage, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the controlsImage as a rectangle in the middle of the screen
        self.image = pygame.image.load('Controls.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center=(960,540))

class instructionsImage(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, width, height):
        super(instructionsImage, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the instructionsImage as a rectangle in the middle of the screen
        self.image = pygame.image.load('Instructions.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center=(960,540))

class winScreen(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, width, height):
        super(winScreen, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the winScreen as a rectangle in the middle of the screen
        self.image = pygame.image.load('Win_Screen.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center=(960,540))

class loseScreen(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, width, height):
        super(loseScreen, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the loseScreen as a rectangle in the middle of the screen
        self.image = pygame.image.load('Lose_Screen.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center=(960,540))

class SS_image(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, width, height):
        super(SS_image, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the SS_image as a rectangle in the middle of the screen
        self.image = pygame.image.load('Save_Screen.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center=(960,540))

class LS_image(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, width, height):
        super(LS_image, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((1920,1080)) 
        self.surf.fill((255,255,255))
        #set up the LS_image as a rectangle in the middle of the screen
        self.image = pygame.image.load('Load_Screen.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.surf.get_rect(center=(960,540))

class Text2(pygame.sprite.Sprite):
    def __init__(self,location,text,size,width,height,colour):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size) #Set up the font for the text
        self.textSurf = self.font.render(text, 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill(colour)
        #set up the textbox as a rectangle with the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, text, size, width, height, colour):
        self.font = pygame.font.SysFont("Arial", size) #Set up the font for the text
        self.textSurf = self.font.render(text, 1, "white") #set up the text with the string 'text'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
