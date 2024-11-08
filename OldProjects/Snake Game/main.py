import pygame
from random import randint
from time import sleep
#Snake game

#Importing the commands of they keys that the user will press
from pygame.locals import (
    RLEACCEL, #for image loading
    K_UP, #for moving up 
    K_DOWN, #for moving down
    K_LEFT, #for moving left
    K_RIGHT, #for moving right
    K_w, #for moving up
    K_s, #for moving down
    K_a, #for moving left
    K_d, ##for moving right
)

class Text(pygame.sprite.Sprite): #Class for any Text boxes we want to display
    def __init__(self, text, size, color, width, height):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
        #set up the text object
        self.font = pygame.font.SysFont("Arial", size)
        #create the text object
        self.textSurf = self.font.render(text, 1, color)
        #set up the box behind the text
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(center=(400,300,))
        #get width and height of text and store in variables
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text onto the textbox (in the center)
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, size, color, width, height, locationY):
        #set CurrentScore to 0
        CurrentScore = 0
        #set score as a string
        score = "Score: "+str(CurrentScore)
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the text object
        self.font = pygame.font.SysFont("Arial", size)
        #create the text object
        self.textSurf = self.font.render(score, 1, color)
        #set up the box behind the text
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center=(100,locationY))
        #get width and height of text and store in variables
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text onto the textbox (in the center)
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, CurrentScore, size, color, width, height):
        #increment CurrentScore by 1 
        CurrentScore += 1
        #set text1 as a string
        text1 = "Score: "+str(CurrentScore)
        #set up the text object
        self.font = pygame.font.SysFont("Arial", size)
        #create the text object
        self.textSurf = self.font.render(text1, 1, color)
        #set up the box behind the text
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        #get width and height of text and store in variables
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        #blit the text onto the textbox (in the center)
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        #returns the CurrentScore so it can be incremented again
        #when player scores another point
        return CurrentScore

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.image.load("fruit.png").convert()
        self.surf.set_colorkey((0, 0, 255), RLEACCEL)
        #randomise x and y coordinates for the fruit to spawn 
        locationX = randint(140,635)
        locationY = randint(128,485)
        #set up the fruit as a rectangle
        self.rect = self.surf.get_rect(center=(locationX,locationY,))

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.image.load(image_file).convert()
        self.surf.set_colorkey((0, 0, 255), RLEACCEL)
        #set up the player as a rectangle in the center of the screen
        self.rect = self.surf.get_rect(center=(400,300,))

    def update(self, pressed_keys):
        #setv up head as the surf of the player
        head = self.surf
        #if up or w is pressed:
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -1) #moves player up by 1
            head = pygame.transform.rotate(self.surf,90) #rotates the player by 90 degrees
        #if down or s is pressed:
        if pressed_keys[K_DOWN] or pressed_keys[K_s]: 
            self.rect.move_ip(0, 1) #moves player down by 1
            head = pygame.transform.rotate(self.surf,270) #rotates the player by 270 degrees
        #if left or a is pressed:
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-1, 0) #moves player left by 1
            head = pygame.transform.rotate(self.surf,180) #rotates the player by 180 degrees
        #if right or d is pressed:
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(1, 0) #moves player right by 1
            head = pygame.transform.rotate(self.surf,0) #rotates the player by 0 degrees
            
        #blits player on to window
        win.blit(head,self.rect)
        #updates display
        pygame.display.update()

        #following 8 lines stop player from moving off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    #the method for the player growing
    def grow(self,length,image_file):
        #incxrements the length by 10
        length += 10
        #sets up the surf with length as the x-length of the player 
        self.surf = pygame.Surface((length, 30))
        self.surf.fill((255,255,255))
        self.image = pygame.image.load(image_file).convert()
        #sets up the player as a rectangle
        self.rect = self.surf.get_rect(center=(400,300,))
        #returns the length so it can be updated again later
        return length
    
class VerticalWall(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #sets up the surf of the wall
        self.surf = pygame.Surface((25, 50))
        self.surf.fill((255,255,255))
        #sets up the wall as a rectangle
        self.rect = self.surf.get_rect(center=(location))

class HorizontalWall(pygame.sprite.Sprite):
    def __init__(self,location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #sets up the surf of the wall
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255,255,255))
        #sets up the wall as a rectangle
        self.rect = self.surf.get_rect(center=(location))

if __name__ == "__main__":
    #opens the files for the wall coordinates
    file1 = open("Vertical_walls.txt",'r')
    file2 = open("Horizontal_walls.txt",'r')
    #sets the default length and score
    length = 50
    CurrentScore = 0

    #initiate pygame
    pygame.init()

    #set the window up with title
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake in python")

    #instantiate sprites
    player = Player("snake.png")
    scoreBoard = Scoreboard(12,"white",100,50,25)
    fruit = Fruit()
    game_over = Text("Game Over",30,"white",200,100)

    #set up sprite groups
    all_sprites = pygame.sprite.Group()
    all_fruit = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    #add sprites to groups
    all_sprites.add(player)
    all_sprites.add(scoreBoard)
    all_sprites.add(fruit)
    all_sprites.add(game_over)
    all_fruit.add(fruit)

    #initite a FOR loop for each line in the first file
    for line in file1:
        #store location as an array of the line of the file split at the comma
        location = line.strip().split(",")
        #take each item in the location array and store it as an integer variable
        num1 = int(location[0])
        num2 = int(location[1])
        #instantiate the vertical wall sprite with the coordinates from the file
        wall = VerticalWall([num1,num2])
        #add this wall to the walls group
        walls.add(wall)

    #initite a FOR loop for each line in the second file
    for line in file2:
        #store location as an array of the line of the file split at the comma
        location = line.strip().split(",")
        #take each item in the location array and store it as an integer variable
        num1 = int(location[0])
        num2 = int(location[1])
        #instantiate the horizontal wall sprite with the coordinates from the file
        wall = HorizontalWall([num1,num2])
        #add this wall to the walls group
        walls.add(wall)

    #set run to True
    run = True
    #initiate a while loop until run is no longer True
    while run:
        #initiate a for loop to detect events
        for event in pygame.event.get():
            #allows the user to quit the game
            if event.type == pygame.QUIT:
                run = False #sets run to False which breaks the loop
                pygame.quit() #closes the pygame window

        #fills the pygame window with black
        win.fill((0,0,0))
        #blits the fruit on to the display
        win.blit(fruit.surf, fruit.rect)
        #blits the scoreboard onto the display
        win.blit(scoreBoard.image,scoreBoard)
        #sets a FOR loop to go through each item in the walls array
        for wall in walls:
            win.blit(wall.surf, wall.rect) #blits the wall to the display
        #updates the display
        pygame.display.update()

        #stores the key that the user presses
        pressed_keys = pygame.key.get_pressed()
        #calls the update method of the player
        #with the key that the user presses as the parameter
        player.update(pressed_keys)

        #checks if the player collides with any of the walls
        if pygame.sprite.spritecollideany(player, walls):
            player.kill() #kills the player
            #blits the game over message to the screen
            win.blit(game_over.image, game_over)
            pygame.display.update() #updates the display
            run = False #sets run to False to break the game loop

        #checks if the player collides with any of the fruit
        if pygame.sprite.spritecollideany(player, all_fruit):
            fruit.kill() #kills the fruit
            fruit = Fruit() #instantiates another fruit
            all_fruit.add(fruit) #adds this fruit to the all_fruit group
            win.blit(fruit.surf, fruit.rect) #blits the fruit onto the display
            #calls the update method of the scoreborad and updates CurrentScore
            CurrentScore = scoreBoard.update(CurrentScore,12,"white",100,50)
            #calls the grow method of the player and updates length
            length = player.grow(length,"snake.png")
            pygame.display.update() #updates the display

    #detects if run is set to False
    if not run:
        sleep(2) #waits for 2 seconds
        pygame.quit() #closes the pygame window
