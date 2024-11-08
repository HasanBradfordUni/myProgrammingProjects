import pygame

from time import sleep
from random import randint

from Starting_Objects import Text1
from Prem_Clubs import Liverpool

class prem_team_selection(object):

    def __init__(self):
        # initiate pygame
        pygame.init()

        # set the window up with title
        self.__win = pygame.display.set_mode((1500, 800))
        self.__winXY = pygame.display.get_window_size()
        pygame.display.set_caption("Football Tic-Tac-Toe")

        # Calculate where the middle of the screen is
        self.__winX = self.__winXY[0]
        self.__winY = self.__winXY[1]
        self.__midX = self.__winX / 2
        self.__midY = self.__winY / 2

        # instantiate sprites
        self.__locX1 = 175
        self.__locX2 = 1075
        self.__locY1 = 150
        self.__liverpool = Liverpool((self.__locX1, self.__locY1))
        self.__button1 = Text1((self.__locX2, self.__locY1), "Move badge", (100,100,100))

        # create sprite groups
        self.__all_sprites = pygame.sprite.Group()

        # add sprites to all_sprites
        self.__all_sprites.add(self.__liverpool)
        self.__all_sprites.add(self.__button1)


    def display(self):
        loc1 = self.__locX2 - 50
        loc2 = self.__locX2 + 50
        loc3 = self.__locY1 - 50
        loc4 = self.__locY1 + 50
        loc5 = self.__locX1 - 50
        loc6 = self.__locX1 + 50
        run = True
        # initiate a while loop until run is no longer True
        while run:
            # initiate a for loop to detect events
            for event in pygame.event.get():
                # allows the user to quit the game
                if event.type == pygame.QUIT:
                    run = False  # sets run to False which breaks the loop
                if event.type == pygame.KEYDOWN:  # checks if a keyboard key is pressed
                    if event.key == pygame.K_f:  # if the key is f
                        pygame.display.toggle_fullscreen()  # toggles fullscreen mode of the pygame window
                if event.type == pygame.MOUSEBUTTONDOWN:  # checks if the mouse is clicked
                    if loc1 <= mouse[0] <= loc2 and loc5 <= mouse[1] <= loc6:
                        coords = (randint(0,1400), randint(0,800))
                        self.__liverpool.setLocation(coords)

            # fills the pygame window with white
            self.__win.fill((0, 0, 0))

            mouse = pygame.mouse.get_pos()

            for sprite in self.__all_sprites:  # set a for loop to cycle through the whole list of sprites
                self.__win.blit(sprite.image, sprite.rect)  # blit each sprite on to the screen
            pygame.display.update()  # update the display with all sprites blitted on

        # detects if run is set to False
        if not run:
            sleep(2)  # waits for 2 seconds
            pygame.quit()  # closes the pygame window