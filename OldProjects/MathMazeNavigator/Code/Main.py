#main program
import pygame
from time import sleep
from Player_class import Player

#initiate pygame
pygame.init()

#set the window up with title
win = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Maths Maze Navigator")

#instantiate sprites
player = Player("Player.png")

run = True
#initiate a while loop until run is no longer True
while run:
    #initiate a for loop to detect events
    for event in pygame.event.get():
        #allows the user to quit the game
        if event.type == pygame.QUIT:
            run = False #sets run to False which breaks the loop

    #fills the pygame window with white
    win.fill((255,255,255))
    #blits the player on to the display
    win.blit(player.surf, player.rect)
    #updates the display
    pygame.display.update()

    #stores the key that the user presses
    pressed_keys = pygame.key.get_pressed()
    #calls the update method of the player
    #with the key that the user presses as the parameter
    player.move(pressed_keys)

#detects if run is set to False    
if not run:
    sleep(2) #waits for 2 seconds
    pygame.quit() #closes the pygame window
