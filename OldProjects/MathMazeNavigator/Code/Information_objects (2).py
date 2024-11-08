#Information objects
import pygame

class Scoreboard(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, size, color, width, height, locationX, locationY):
        CurrentScore = 0 #set 'CurrentScore' to 0
        score = "Score: "+str(CurrentScore) #create the string that will be blited on to the sprite
        pygame.sprite.Sprite.__init__(self) #Call the parent class (Sprite) constructor
        self.font = pygame.font.SysFont("Arial", size) #Set up the font for the text
        self.textSurf = self.font.render(score, 1, color) #set up the text with the string 'score'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height)) 
        self.surf.fill((0,0,255))
        #set up the Scoreboard as a rectangle in the specified part of the screen
        self.rect = self.surf.get_rect(center=(locationX,locationY))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    #define the update method of the class (to update the score)
    def update(self, CurrentScore, size, color, width, height):
        score = "Score: "+str(CurrentScore) #create the string that will be blited on to the sprite
        self.font = pygame.font.SysFont("Arial", size) #Set up the font for the text
        self.textSurf = self.font.render(score, 1, color) #set up the text with the string 'score'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #get the width and length of the text object
        W = self.textSurf.get_width() 
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

class LivesC(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, size, color, width, height, locationX, locationY):
        Lives = 300 #set 'Lives' to 3
        lives = "Lives: "+str(Lives) #create the string that will be blited on to the sprite
        pygame.sprite.Sprite.__init__(self)  #Call the parent class (Sprite) constructor
        self.font = pygame.font.SysFont("Arial", size)  #Set up the font for the text
        self.textSurf = self.font.render(lives, 1, color) #set up the text with the string 'lives'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #set up the Lives counter as a rectangle in the specified part of the screen
        self.rect = self.surf.get_rect(center=(locationX,locationY))
        #get the width and length of the text object
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, Lives, size, color, width, height):
        Lives -= 1 #Decrement the 'Lives' by 1
        lives = "Lives: "+str(Lives) #create the string that will be blited on to the sprite
        self.font = pygame.font.SysFont("Arial", size)  #Set up the font for the text
        self.textSurf = self.font.render(lives, 1, color) #set up the text with the string 'lives'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #get the width and length of the text object
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        return Lives #return the new 'Lives' to the Main program
    
class MovesC(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, size, color, width, height, locationX, locationY):
        Moves = 0 #set 'Moves' to 0
        moves = "Moves: "+str(Moves) #create the string that will be blited on to the sprite
        pygame.sprite.Sprite.__init__(self)  #Call the parent class (Sprite) constructor
        self.font = pygame.font.SysFont("Arial", size)  #Set up the font for the text
        self.textSurf = self.font.render(moves, 1, color) #set up the text with the string 'moves'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #set up the Moves counter as a rectangle in the specified part of the screen
        self.rect = self.surf.get_rect(center=(locationX,locationY))
        #get the width and length of the text object
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, Moves, size, color, width, height):
        moves = "Moves: "+str(Moves) #create the string that will be blited on to the sprite
        self.font = pygame.font.SysFont("Arial", size)  #Set up the font for the text
        self.textSurf = self.font.render(moves, 1, color) #set up the text with the string 'moves'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #get the width and length of the text object
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

class Timer(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, size, color, width, height, locationX, locationY):
        Time = 0 #set 'Time' to 0
        time = "Time: "+str(Time) #create the string that will be blited on to the sprite
        pygame.sprite.Sprite.__init__(self)  #Call the parent class (Sprite) constructor
        self.font = pygame.font.SysFont("Arial", size)  #Set up the font for the text
        self.textSurf = self.font.render(time, 1, color) #set up the text with the string 'time'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #set up the Timer as a rectangle in the specified part of the screen
        self.rect = self.surf.get_rect(center=(locationX,locationY))
        #get the width and length of the text object
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, Time, size, color, width, height):
        time = "Time: "+str(Time) #create the string that will be blited on to the sprite
        self.font = pygame.font.SysFont("Arial", size)  #Set up the font for the text
        self.textSurf = self.font.render(time, 1, color) #set up the text with the string 'time'
        #set up the sprite's surf
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,255))
        #get the width and length of the text object
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text object on to the center of the sprite
        self.surf.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        return Time #return the new 'Time' to the Main program

class SaveButton(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, location):
        super(SaveButton, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((100,100)) 
        self.surf.fill((255,255,255))
        #set up the instructionsImage as a rectangle in the middle of the screen
        self.image = pygame.image.load('Save.png').convert()
        self.rect = self.surf.get_rect(center=(location))

class LoadButton(pygame.sprite.Sprite):
    #define the constructor method of the class
    def __init__(self, location):
        super(LoadButton, self).__init__() #Call the parent class (Sprite) constructor
        #set up the sprite's surf
        self.surf = pygame.Surface((100,100)) 
        self.surf.fill((255,255,255))
        #set up the instructionsImage as a rectangle in the middle of the screen
        self.image = pygame.image.load('Load.png').convert()
        self.rect = self.surf.get_rect(center=(location))

