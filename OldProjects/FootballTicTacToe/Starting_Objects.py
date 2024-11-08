#Starting objects

import pygame

class Title(pygame.sprite.Sprite):
    def __init__(self,location,text):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 75) #Set up the font for the text
        self.textSurf = self.font.render(text, 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((1000, 500))
        self.surf.fill((0,0,0))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [1000/2 - W/2, 500/2 - H/2])

class TwoPlayer(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 30) #Set up the font for the text
        self.textSurf = self.font.render("2 Player Mode", 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((100,69,69))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [200/2 - W/2, 100/2 - H/2])

class OnePlayer(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 30) #Set up the font for the text
        self.textSurf = self.font.render("1 Player Mode", 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((69,100,69))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [200/2 - W/2, 100/2 - H/2])

class Instructions(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 30) #Set up the font for the text
        self.textSurf = self.font.render("Instructions", 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((100,100,69))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [200/2 - W/2, 100/2 - H/2])

class Quit(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 40) #Set up the font for the text
        self.textSurf = self.font.render("Quit!", 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((69,69,0))
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [200/2 - W/2, 100/2 - H/2])

class Text1(pygame.sprite.Sprite):
    def __init__(self,location,text,colour):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 30) #Set up the font for the text
        self.textSurf = self.font.render(text, 1, "white") #set up the text with 'text' as the string
        #set up the sprite's surf
        self.surf = pygame.Surface((200, 100))
        self.surf.fill(colour)
        #set up the player as a rectangle as the center set to the location variable
        self.rect = self.surf.get_rect(center=(location))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [200/2 - W/2, 100/2 - H/2])
