#Main program
import pygame

from time import sleep

from Starting_Objects import Title, OnePlayer, TwoPlayer, Instructions, Quit, Text1
from Prem_Clubs import *

#set up a class for the start screen
class start_screen(object):
    def __init__(self):
        #initiate pygame
        pygame.init()

        #set the window up with title
        self.__win = pygame.display.set_mode((1500, 800))
        self.__winXY = pygame.display.get_window_size()
        pygame.display.set_caption("Football Tic-Tac-Toe")

        #Calculate where the middle of the screen is
        self.__winX = self.__winXY[0]
        self.__winY = self.__winXY[1]
        self.__midX = self.__winX / 2
        self.__midY = self.__winY / 2
        
        #instantiate sprites
        self.__locX1 = self.__midX
        self.__locX2 = 200
        self.__locX3 = self.__midX - 200
        self.__locX4 = self.__midX + 150
        self.__locX5 = self.__winX - 200
        self.__locY1 = self.__midY - (self.__midY / 2)
        self.__locY2 = self.__midY + (self.__midY / 2)
        self.__title = Title((self.__locX1,self.__locY1),"Football Tic-Tac-Toe")
        self.__onePlayer = OnePlayer((self.__locX2,self.__locY2))
        self.__twoPlayer = TwoPlayer((self.__locX3,self.__locY2))
        self.__instructions = Instructions((self.__locX4,self.__locY2))
        self.__quit = Quit((self.__locX5,self.__locY2))
        
        #create sprite groups
        self.__all_sprites = pygame.sprite.Group()
        
        #add sprites to all_sprites
        self.__all_sprites.add(self.__title)
        self.__all_sprites.add(self.__onePlayer)
        self.__all_sprites.add(self.__twoPlayer)
        self.__all_sprites.add(self.__instructions)
        self.__all_sprites.add(self.__quit)
    
    def display(self):
        loc1 = self.__locX2 - 100
        loc2 = self.__locX2 + 100
        loc3 = self.__locY2 - 50
        loc4 = self.__locY2 + 50
        loc5 = self.__locX3 - 100
        loc6 = self.__locX3 + 100
        loc7 = self.__locX4 - 100
        loc8 = self.__locX4 + 100
        loc9 = self.__locX5 - 100
        loc0 = self.__locX5 + 100
        run = True
        #initiate a while loop until run is no longer True
        while run:
            #initiate a for loop to detect events
            for event in pygame.event.get():
                #allows the user to quit the game
                if event.type == pygame.QUIT:
                    run = False #sets run to False which breaks the loop
                if event.type == pygame.KEYDOWN: #checks if a keyboard key is pressed
                    if event.key == pygame.K_f: #if the key is f
                        pygame.display.toggle_fullscreen() #toggles fullscreen mode of the pygame window
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is clicked
                    if loc1 <= mouse[0] <= loc2 and loc3 <= mouse[1] <= loc4:
                        print()
                    if loc5 <= mouse[0] <= loc6 and loc3 <= mouse[1] <= loc4:
                        game.run_ACS()
                    if loc7 <= mouse[0] <= loc8 and loc3 <= mouse[1] <= loc4:
                        game.run_game()
                    if loc9 <= mouse[0] <= loc0 and loc3 <= mouse[1] <= loc4:
                        run = False

            #fills the pygame window with white
            self.__win.fill((0,0,0))

            mouse = pygame.mouse.get_pos()

            for sprite in self.__all_sprites: #set a for loop to cycle through the whole list of sprites
                self.__win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window


class club_category_screen(object):
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
        self.__locX1 = self.__midX
        self.__locX2 = 200
        self.__locX3 = self.__midX - 200
        self.__locX4 = self.__midX + 150
        self.__locX5 = self.__winX - 200
        self.__locY1 = self.__midY - (self.__midY / 2)
        self.__locY2 = self.__midY + (self.__midY / 2)
        self.__title = Title((self.__locX1, self.__locY1), "Choose a category of club")
        self.__premClubs = Text1((self.__locX2,self.__locY2), "Prem Clubs", (187, 108, 157))
        self.__EflClubs = Text1((self.__locX3,self.__locY2), "EFL Clubs", (148, 165, 146))
        self.__UclClubs = Text1((self.__locX4,self.__locY2), "UCL Clubs", (78, 109, 97))
        self.__quit = Quit((self.__locX5, self.__locY2))

        # create sprite groups
        self.__all_sprites = pygame.sprite.Group()

        # add sprites to all_sprites
        self.__all_sprites.add(self.__title)
        self.__all_sprites.add(self.__premClubs)
        self.__all_sprites.add(self.__EflClubs)
        self.__all_sprites.add(self.__UclClubs)
        self.__all_sprites.add(self.__quit)

    def display(self):
        loc1 = self.__locX2 - 100
        loc2 = self.__locX2 + 100
        loc3 = self.__locY2 - 50
        loc4 = self.__locY2 + 50
        loc5 = self.__locX3 - 100
        loc6 = self.__locX3 + 100
        loc7 = self.__locX4 - 100
        loc8 = self.__locX4 + 100
        loc9 = self.__locX5 - 100
        loc0 = self.__locX5 + 100
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
                    if loc1 <= mouse[0] <= loc2 and loc3 <= mouse[1] <= loc4:
                        game.run_PTS()
                    if loc5 <= mouse[0] <= loc6 and loc3 <= mouse[1] <= loc4:
                        print()
                    if loc7 <= mouse[0] <= loc8 and loc3 <= mouse[1] <= loc4:
                        print()
                    if loc9 <= mouse[0] <= loc0 and loc3 <= mouse[1] <= loc4:
                        run = False

            # fills the pygame window with white
            self.__win.fill((0, 0, 0))

            mouse = pygame.mouse.get_pos()

            for sprite in self.__all_sprites:  # set a for loop to cycle through the whole list of sprites
                self.__win.blit(sprite.surf, sprite.rect)  # blit each sprite on to the screen
            pygame.display.update()  # update the display with all sprites blitted on

        # detects if run is set to False
        if not run:
            sleep(2)  # waits for 2 seconds
            pygame.quit()  # closes the pygame window

class aspect_chooser_screen(object):
    def __init__(self):
        #initiate pygame
        pygame.init()

        #set the window up with title
        self.__win = pygame.display.set_mode((1500, 800))
        self.__winXY = pygame.display.get_window_size()
        pygame.display.set_caption("Football Tic-Tac-Toe")

        #Calculate where the middle of the screen is
        self.__winX = self.__winXY[0]
        self.__winY = self.__winXY[1]
        self.__midX = self.__winX / 2
        self.__midY = self.__winY / 2
        
        #instantiate sprites
        self.__locX1 = self.__midX
        self.__locX2 = 200
        self.__locX3 = self.__midX - 200
        self.__locX4 = self.__midX + 150
        self.__locX5 = self.__winX - 200
        self.__locY1 = self.__midY - (self.__midY / 2)
        self.__locY2 = self.__midY + (self.__midY / 2)
        self.__title = Title((self.__locX1,self.__locY1),"Choose category for aspect of board")
        self.__club = Text1((self.__locX2,self.__locY2), "Club", (122, 149, 166))
        self.__nation = Text1((self.__locX3,self.__locY2), "Nation", (34, 150, 143))
        self.__cardType = Text1((self.__locX4,self.__locY2), "Card Type", (53, 148, 114))
        self.__quit = Quit((self.__locX5,self.__locY2))
        
        #create sprite groups
        self.__all_sprites = pygame.sprite.Group()
        
        #add sprites to all_sprites
        self.__all_sprites.add(self.__title)
        self.__all_sprites.add(self.__club)
        self.__all_sprites.add(self.__nation)
        self.__all_sprites.add(self.__cardType)
        self.__all_sprites.add(self.__quit)
    
    def display(self):
        loc1 = self.__locX2 - 100
        loc2 = self.__locX2 + 100
        loc3 = self.__locY2 - 50
        loc4 = self.__locY2 + 50
        loc5 = self.__locX3 - 100
        loc6 = self.__locX3 + 100
        loc7 = self.__locX4 - 100
        loc8 = self.__locX4 + 100
        loc9 = self.__locX5 - 100
        loc0 = self.__locX5 + 100
        run = True
        #initiate a while loop until run is no longer True
        while run:
            #initiate a for loop to detect events
            for event in pygame.event.get():
                #allows the user to quit the game
                if event.type == pygame.QUIT:
                    run = False #sets run to False which breaks the loop
                if event.type == pygame.KEYDOWN: #checks if a keyboard key is pressed
                    if event.key == pygame.K_f: #if the key is f
                        pygame.display.toggle_fullscreen() #toggles fullscreen mode of the pygame window
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is clicked
                    if loc1 <= mouse[0] <= loc2 and loc3 <= mouse[1] <= loc4:
                        game.run_CCS()
                    if loc5 <= mouse[0] <= loc6 and loc3 <= mouse[1] <= loc4:
                        print()
                    if loc7 <= mouse[0] <= loc8 and loc3 <= mouse[1] <= loc4:
                        print()
                    if loc9 <= mouse[0] <= loc0 and loc3 <= mouse[1] <= loc4:
                        run = False

            #fills the pygame window with white
            self.__win.fill((0,0,0))

            mouse = pygame.mouse.get_pos()

            for sprite in self.__all_sprites: #set a for loop to cycle through the whole list of sprites
                self.__win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class prem_team_selection(object):
    def __init__(self):
        #initiate pygame
        pygame.init()

        #set the window up with title
        self.__win = pygame.display.set_mode((1500, 800))
        self.__winXY = pygame.display.get_window_size()
        pygame.display.set_caption("Football Tic-Tac-Toe")

        #Calculate where the middle of the screen is
        self.__winX = self.__winXY[0]
        self.__winY = self.__winXY[1]
        self.__midX = self.__winX / 2
        self.__midY = self.__winY / 2
        
        #instantiate sprites
        self.__locX1 = 175
        self.__locX2 = 475
        self.__locX3 = 775
        self.__locX4 = 1075
        self.__locX5 = 1375
        self.__locY1 = 150
        self.__locY2 = 450
        self.__locY3 = 300
        self.__locY4 = 600
        self.__arsenal = Arsenal((self.__locX1,self.__locY1))
        self.__astonVilla = AstonVilla((self.__locX2,self.__locY1))
        self.__bournemouth = Bournemouth((self.__locX3,self.__locY1))
        self.__brentford = Brentford((self.__locX4,self.__locY1))
        self.__brighton = Brighton((self.__locX5,self.__locY1))
        self.__burnley = Burnley((self.__locX1, self.__locY3))
        self.__chelsea = Chelsea((self.__locX2, self.__locY3))
        self.__crystalPalace = CrystalPalace((self.__locX3, self.__locY3))
        self.__everton = Everton((self.__locX4, self.__locY3))
        self.__fulham = Fulham((self.__locX5, self.__locY3))
        self.__liverpool = Liverpool((self.__locX1, self.__locY2))
        self.__luton = Luton((self.__locX2, self.__locY2))
        self.__manchesterCity = ManchesterCity((self.__locX3, self.__locY2))
        self.__manchesterUnited = ManchesterUnited((self.__locX4, self.__locY2))
        self.__newcastle = Newcastle((self.__locX5, self.__locY2))
        self.__forest = Forest((self.__locX1, self.__locY4))
        self.__sheffieldUtd = SheffieldUtd((self.__locX2, self.__locY4))
        self.__tottenham = Tottenham((self.__locX3, self.__locY4))
        self.__westHam = WestHam((self.__locX4, self.__locY4))
        self.__wolves = Wolves((self.__locX5, self.__locY4))
        
        #create sprite groups
        self.__all_sprites = pygame.sprite.Group()
        
        #add sprites to all_sprites
        self.__all_sprites.add(self.__arsenal)
        self.__all_sprites.add(self.__astonVilla)
        self.__all_sprites.add(self.__bournemouth)
        self.__all_sprites.add(self.__brentford)
        self.__all_sprites.add(self.__brighton)
        self.__all_sprites.add(self.__burnley)
        self.__all_sprites.add(self.__chelsea)
        self.__all_sprites.add(self.__crystalPalace)
        self.__all_sprites.add(self.__everton)
        self.__all_sprites.add(self.__fulham)
        self.__all_sprites.add(self.__liverpool)
        self.__all_sprites.add(self.__luton)
        self.__all_sprites.add(self.__manchesterCity)
        self.__all_sprites.add(self.__manchesterUnited)
        self.__all_sprites.add(self.__newcastle)
        self.__all_sprites.add(self.__forest)
        self.__all_sprites.add(self.__sheffieldUtd)
        self.__all_sprites.add(self.__tottenham)
        self.__all_sprites.add(self.__westHam)
        self.__all_sprites.add(self.__wolves)
    
    def display(self):
        loc1 = self.__locX2 - 50
        loc2 = self.__locX2 + 50
        loc3 = self.__locY1 - 50
        loc4 = self.__locY1 + 50
        loc5 = self.__locX3 - 50
        loc6 = self.__locX3 + 50
        loc7 = self.__locX4 - 50
        loc8 = self.__locX4 + 50
        loc9 = self.__locX5 - 50
        loc0 = self.__locX5 + 50
        loc11 = self.__locX1 - 50
        loc12 = self.__locX1 + 50
        loc13 = self.__locY2 - 50
        loc14 = self.__locY2 + 50
        loc15 = self.__locY3 - 50
        loc16 = self.__locY3 + 50
        loc17 = self.__locY4 - 50
        loc18 = self.__locY4 + 50
        run = True
        #initiate a while loop until run is no longer True
        while run:
            #initiate a for loop to detect events
            for event in pygame.event.get():
                #allows the user to quit the game
                if event.type == pygame.QUIT:
                    run = False #sets run to False which breaks the loop
                if event.type == pygame.KEYDOWN: #checks if a keyboard key is pressed
                    if event.key == pygame.K_f: #if the key is f
                        pygame.display.toggle_fullscreen() #toggles fullscreen mode of the pygame window
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is clicked
                    if loc1 <= mouse[0] <= loc2 and loc3 <= mouse[1] <= loc4:
                        print("Aston Villa")
                    elif loc5 <= mouse[0] <= loc6 and loc3 <= mouse[1] <= loc4:
                        print("Bournemouth")
                    elif loc7 <= mouse[0] <= loc8 and loc3 <= mouse[1] <= loc4:
                        print("Brentford")
                    elif loc9 <= mouse[0] <= loc0 and loc3 <= mouse[1] <= loc4:
                        print("Brighton")
                    elif loc11 <= mouse[0] <= loc12 and loc3 <= mouse[1] <= loc4:
                        print("Arsenal")
                    elif loc1 <= mouse[0] <= loc2 and loc15 <= mouse[1] <= loc16:
                        print("Chelsea")
                    elif loc5 <= mouse[0] <= loc6 and loc15 <= mouse[1] <= loc16:
                        print("Crystal Palace")
                    elif loc7 <= mouse[0] <= loc8 and loc15 <= mouse[1] <= loc16:
                        print("Everton")
                    elif loc9 <= mouse[0] <= loc0 and loc15 <= mouse[1] <= loc16:
                        print("Fulham")
                    elif loc11 <= mouse[0] <= loc12 and loc15 <= mouse[1] <= loc16:
                        print("Burnley")
                    elif loc1 <= mouse[0] <= loc2 and loc13 <= mouse[1] <= loc14:
                        print("Luton Town")
                    elif loc5 <= mouse[0] <= loc6 and loc13 <= mouse[1] <= loc14:
                        print("Manchester City")
                    elif loc7 <= mouse[0] <= loc8 and loc13 <= mouse[1] <= loc14:
                        print("Manchester United")
                    elif loc9 <= mouse[0] <= loc0 and loc13 <= mouse[1] <= loc14:
                        print("Newcastle United")
                    elif loc11 <= mouse[0] <= loc12 and loc13 <= mouse[1] <= loc14:
                        print("Liverpool")
                    elif loc1 <= mouse[0] <= loc2 and loc17 <= mouse[1] <= loc18:
                        print("Sheffield United")
                    elif loc5 <= mouse[0] <= loc6 and loc17 <= mouse[1] <= loc18:
                        print("Tottenham Hotspur")
                    elif loc7 <= mouse[0] <= loc8 and loc17 <= mouse[1] <= loc18:
                        print("West Ham")
                    elif loc9 <= mouse[0] <= loc0 and loc17 <= mouse[1] <= loc18:
                        print("Wolves")
                    elif loc11 <= mouse[0] <= loc12 and loc17 <= mouse[1] <= loc18:
                        print("Nottingham Forest")
                    else:
                        print("No club selected")

            #fills the pygame window with white
            self.__win.fill((0,0,0))

            mouse = pygame.mouse.get_pos()

            for sprite in self.__all_sprites: #set a for loop to cycle through the whole list of sprites
                self.__win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class game_screen():
    def __init__(self):
        # Initialize pygame and create a window
        pygame.init()

        # set the window up with title
        self.window = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption("Football Tic-Tac-Toe")

        # Define some colors and fonts
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.font = pygame.font.SysFont("Arial", 32)

        # Define the board as a list of lists
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        # Define the turn variable to keep track of whose turn it is
        self.turn = "X"

        # Define the winner variable to store the winner of the game
        self.winner = None

    # Define a function to draw the board on the window
    def draw_board(self):
        # Fill the window with white color
        self.window.fill(self.white)
        # Draw the grid lines
        pygame.draw.line(self.window, self.black, (100, 0), (100, 300), 5)
        pygame.draw.line(self.window, self.black, (200, 0), (200, 300), 5)
        pygame.draw.line(self.window, self.black, (0, 100), (300, 100), 5)
        pygame.draw.line(self.window, self.black, (0, 200), (300, 200), 5)
        # Draw the X and O symbols on the board
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "X":
                    pygame.draw.line(self.window, self.red, (j * 100 + 25, i * 100 +
                                               25), ((j + 1) * 100 - 25, (i + 1) * 100 - 25), 10)
                    pygame.draw.line(self.window, self.red, ((j + 1) * 100 - 25, i * 100
                                               + 25), (j * 100 + 25, (i + 1) * 100 - 25), 10)
                elif self.board[i][j] == "O":
                    pygame.draw.circle(self.window, self.blue, (j * 100 + 50, i * 100 +
                                                  50), 40, 10)

    # Define a function to check if there is a winner or a tie
    def check_winner(self):
        # Check the rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                winner = self.board[i][0]
        # Check the columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] is not None:
                winner = self.board[0][j]
        # Check the diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            winner = self.board[0][2]
            # Check if the board is full
        if None not in self.board[0] and None not in self.board[1] and None not in self.board[2]:
            winner = "Tie"

    # Define a function to display the winner or the tie message
    def display_winner(self):
        # Create a text surface with the winner or the tie message
        text = ""
        if self.winner == "X":
            text = self.font.render("X wins!", True, self.red)
        elif self.winner == "O":
            text = self.font.render("O wins!", True, self.blue)
        elif self.winner == "Tie":
            text = self.font.render("It's a tie!", True, self.black)
        # Get the rectangle of the text surface
        text_rect = text.get_rect()
        # Center the text surface on the window
        text_rect.center = (150, 150)
        # Blit the text surface on the window
        self.window.blit(text, text_rect)

    def display(self):
        # Main game loop
        while True:
            # Handle the events
            for event in pygame.event.get():
                # If the user clicks the close button, quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                # If the user clicks the mouse, handle the input
                if event.type == pygame.MOUSEBUTTONDOWN and self.winner is None:
                    # Get the mouse position
                    x, y = pygame.mouse.get_pos()
                    # Convert the mouse position to grid coordinates
                    row = y // 100
                    col = x // 100
                    # If the grid cell is empty, place the symbol and switch the turn
                    if self.board[row][col] is None:
                        self.board[row][col] = self.turn
                        if self.turn == "X":
                            self.turn = "O"
                        else:
                            self.turn = "X"
                    # Check if there is a winner or a tie
                    self.check_winner()
            # Draw the board on the window
            self.draw_board()
            # If there is a winner or a tie, display the message
            if self.winner is not None:
                self.display_winner()
            # Update the display
            pygame.display.update()


class Game(object):
    def __init__(self):
        self.display1 = start_screen()
        self.display2 = prem_team_selection()
        self.display3 = aspect_chooser_screen()
        self.display4 = club_category_screen()
        self.display5 = game_screen()

    #set up the run_start method which will call the display method of the 'start_screen' class
    def run_start(self):
        self.display1.display() #call the display method of the class assigned to 'display1'

    #set up the run_PTS method which will call the display method of the 'prem_team_selection' class
    def run_PTS(self):
        self.display2.display() #call the display method of the class assigned to 'display2'

    #set up the run_ACS method which will call the display method of the 'aspect_chooser_screen' class
    def run_ACS(self):
        self.display3.display() #call the display method of the class assigned to 'display3'

    def run_CCS(self):
        self.display4.display() #call the display method of the class assigned to 'display3'

    def run_game(self):
        self.display5.display()

    """#set up the run_controls method which will call the display method of the 'controls_screen' class
    def run_instructions(self):
        self.display4.display() #call the display method of the class assigned to 'display4'

    #set up the run_controls method which will call the display method of the 'instructions_screen' class
    def run_main(self):
        self.display2.display() #call the display method of the class assigned to 'display2'"""

#set up an if statement for the main part of the program
if __name__ == "__main__":
    game = Game() #instantiate the game class
    game.run_start() #call the 'run_start' method of the game class

