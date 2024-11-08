#main program
import pygame

from time import sleep
from random import randint,random

from Player_class import Player
from Maze_objects import Wall, Cell, Empty, Key
from Information_objects import Scoreboard, LivesC, MovesC, Timer
from Starting_objects import Title, Controls, Play, Instructions, Quit
from Other_objects import controlsImage, instructionsImage, winScreen, loseScreen
from GameSave_class import GameSave

MAZE_HEIGHT = 10 
MAZE_WIDTH = 10

maze = []

class screens(object):
    def __init__(self):
        #set the window up with title
        self._win = pygame.display.set_mode((1900, 1000), pygame.RESIZABLE)
        self._winXY = pygame.display.get_window_size()
        pygame.display.set_caption("Maths Maze Navigator")

        #create sprite groups
        self._all_sprites = pygame.sprite.Group()

    def display():
        pass

def surroundingCells(maze, rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == True):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == True):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == True):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == True):
        s_cells += 1

    return s_cells

def create_paths(maze, MAZE_HEIGHT, MAZE_WIDTH):
    starting_height = int(random()*MAZE_HEIGHT)
    starting_width = int(random()*MAZE_WIDTH)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == MAZE_HEIGHT-1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == MAZE_WIDTH-1):
        starting_width -= 1

    maze[starting_height][starting_width] = True

    wallCoords = []
    wallCoords.append([starting_height - 1, starting_width])
    wallCoords.append([starting_height, starting_width - 1])
    wallCoords.append([starting_height, starting_width + 1])
    wallCoords.append([starting_height + 1, starting_width])

    maze[starting_height-1][starting_width] = False
    maze[starting_height][starting_width - 1] = False
    maze[starting_height][starting_width + 1] = False
    maze[starting_height + 1][starting_width] = False

    while (wallCoords):
      # Pick a random wall
      rand_wall = wallCoords[int(random()*len(wallCoords))-1]

      # Check if it is a left wall
      if (rand_wall[1] != 0):
          if (maze[rand_wall[0]][rand_wall[1]-1] == 'None' and maze[rand_wall[0]][rand_wall[1]+1] == True):
              # Find the number of surrounding cells
              s_cells = surroundingCells(maze, rand_wall)

              if (s_cells < 2):
                  # Denote the new path
                  maze[rand_wall[0]][rand_wall[1]] = True

                  # Mark the new walls
                  # Upper cell
                  if (rand_wall[0] != 0):
                      if (maze[rand_wall[0]-1][rand_wall[1]] != True):
                          maze[rand_wall[0]-1][rand_wall[1]] = False
                      if ([rand_wall[0]-1, rand_wall[1]] not in wallCoords):
                          wallCoords.append([rand_wall[0]-1, rand_wall[1]])


                  # Bottom cell
                  if (rand_wall[0] != MAZE_HEIGHT-1):
                      if (maze[rand_wall[0]+1][rand_wall[1]] != True):
                          maze[rand_wall[0]+1][rand_wall[1]] = False
                      if ([rand_wall[0]+1, rand_wall[1]] not in wallCoords):
                          wallCoords.append([rand_wall[0]+1, rand_wall[1]])

                  # Leftmost cell
                  if (rand_wall[1] != 0):    
                      if (maze[rand_wall[0]][rand_wall[1]-1] != True):
                          maze[rand_wall[0]][rand_wall[1]-1] = False
                      if ([rand_wall[0], rand_wall[1]-1] not in wallCoords):
                          wallCoords.append([rand_wall[0], rand_wall[1]-1])


              # Delete wall
              for wall in wallCoords:
                  if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                      wallCoords.remove(wall)

              continue

      #Check if it is an upper wall
      if (rand_wall[0] != 0):
          if (maze[rand_wall[0]-1][rand_wall[1]] == 'None' and maze[rand_wall[0]+1][rand_wall[1]] == True):

              s_cells = surroundingCells(maze, rand_wall)
              if (s_cells < 2):
                  # Denote the new path
                  maze[rand_wall[0]][rand_wall[1]] = True

                  # Mark the new walls
                  # Upper cell
                  if (rand_wall[0] != 0):
                      if (maze[rand_wall[0]-1][rand_wall[1]] != True):
                          maze[rand_wall[0]-1][rand_wall[1]] = False
                      if ([rand_wall[0]-1, rand_wall[1]] not in wallCoords):
                          wallCoords.append([rand_wall[0]-1, rand_wall[1]])

                  # Leftmost cell
                  if (rand_wall[1] != 0):
                      if (maze[rand_wall[0]][rand_wall[1]-1] != True):
                          maze[rand_wall[0]][rand_wall[1]-1] = False
                      if ([rand_wall[0], rand_wall[1]-1] not in wallCoords):
                          wallCoords.append([rand_wall[0], rand_wall[1]-1])

                  # Rightmost cell
                  if (rand_wall[1] != MAZE_WIDTH-1):
                      if (maze[rand_wall[0]][rand_wall[1]+1] != True):
                          maze[rand_wall[0]][rand_wall[1]+1] = False
                      if ([rand_wall[0], rand_wall[1]+1] not in wallCoords):
                          wallCoords.append([rand_wall[0], rand_wall[1]+1])

              # Delete wall
              for wall in wallCoords:
                  if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                      wallCoords.remove(wall)

              continue

      # Check the bottom wall
      if (rand_wall[0] != MAZE_HEIGHT-1):
          if (maze[rand_wall[0]+1][rand_wall[1]] == 'None' and maze[rand_wall[0]-1][rand_wall[1]] == True):

              s_cells = surroundingCells(maze, rand_wall)
              if (s_cells < 2):
                  # Denote the new path
                  maze[rand_wall[0]][rand_wall[1]] = True

                  # Mark the new walls
                  if (rand_wall[0] != MAZE_HEIGHT-1):
                      if (maze[rand_wall[0]+1][rand_wall[1]] != True):
                          maze[rand_wall[0]+1][rand_wall[1]] = False
                      if ([rand_wall[0]+1, rand_wall[1]] not in wallCoords):
                          wallCoords.append([rand_wall[0]+1, rand_wall[1]])
                  if (rand_wall[1] != 0):
                      if (maze[rand_wall[0]][rand_wall[1]-1] != True):
                          maze[rand_wall[0]][rand_wall[1]-1] = False
                      if ([rand_wall[0], rand_wall[1]-1] not in wallCoords):
                          wallCoords.append([rand_wall[0], rand_wall[1]-1])
                  if (rand_wall[1] != MAZE_WIDTH-1):
                      if (maze[rand_wall[0]][rand_wall[1]+1] != True):
                          maze[rand_wall[0]][rand_wall[1]+1] = False
                      if ([rand_wall[0], rand_wall[1]+1] not in wallCoords):
                          wallCoords.append([rand_wall[0], rand_wall[1]+1])

              # Delete wall
              for wall in wallCoords:
                  if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                      wallCoords.remove(wall)


              continue

      # Check the right wall
      if (rand_wall[1] != MAZE_WIDTH-1):
          if (maze[rand_wall[0]][rand_wall[1]+1] == 'None' and maze[rand_wall[0]][rand_wall[1]-1] == True):

              s_cells = surroundingCells(maze, rand_wall)
              if (s_cells < 2):
                  # Denote the new path
                  maze[rand_wall[0]][rand_wall[1]] = True

                  # Mark the new walls
                  if (rand_wall[1] != MAZE_WIDTH-1):
                      if (maze[rand_wall[0]][rand_wall[1]+1] != True):
                          maze[rand_wall[0]][rand_wall[1]+1] = False
                      if ([rand_wall[0], rand_wall[1]+1] not in wallCoords):
                          wallCoords.append([rand_wall[0], rand_wall[1]+1])
                  if (rand_wall[0] != MAZE_HEIGHT-1):
                      if (maze[rand_wall[0]+1][rand_wall[1]] != True):
                          maze[rand_wall[0]+1][rand_wall[1]] = False
                      if ([rand_wall[0]+1, rand_wall[1]] not in wallCoords):
                          wallCoords.append([rand_wall[0]+1, rand_wall[1]])
                  if (rand_wall[0] != 0):    
                      if (maze[rand_wall[0]-1][rand_wall[1]] != True):
                          maze[rand_wall[0]-1][rand_wall[1]] = False
                      if ([rand_wall[0]-1, rand_wall[1]] not in wallCoords):
                          wallCoords.append([rand_wall[0]-1, rand_wall[1]])

              # Delete wall
              for wall in wallCoords:
                  if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                      wallCoords.remove(wall)

              continue

      # Delete the wall from the list anyway
      for wall in wallCoords:
          if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
              wallCoords.remove(wall)
    
    return maze

def generate_maze(MAZE_HEIGHT, MAZE_WIDTH, maze, walls, cells, all_sprites, midX, midY):
    visited = [] #set up an empty array for the cells the player has visited
    #set up a FOR loop for the rows of the maze and visited
    for x in range(0, MAZE_HEIGHT): #initiates a FOR loop for the maze/visited rows
        visitedRow = [] #initialise the 'visitedRow' as an empty array
        mazeRow = [] #initialise the 'mazeRow' as an empty array
        for y in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze/visited columns
            mazeRow.append("None") #append the value which will be used for empty sections of the maze
            visitedRow.append(False) #append the value which will be used for cells the player hasn't visited yet
        maze.append(mazeRow) #append the 'mazeRow' full of 'None' strings to 'maze'
        visited.append(visitedRow) #append the 'visitedRow' full of 'False' booleans to 'visited'

    #calls the 'create_paths' function which returns the 'maze' array
    maze = create_paths(maze, MAZE_HEIGHT, MAZE_WIDTH)

    #set up a FOR loop for the rows of the maze
    for i in range(0, MAZE_HEIGHT):
        for j in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze columns
            if (maze[i][j] == 'None'): #use an IF statement to check if an item in 'maze' is 'None'
                maze[i][j] = False #if it is 'None' sets it to False for the walls of the maze

    #sets the entrance and exit of the maze
    maze[0][1] = 'None'
    maze[MAZE_WIDTH-1][MAZE_WIDTH-2] = 'None'

    #set up a FOR loop for the rows of the maze
    for x in range(0, MAZE_HEIGHT):
        for y in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze columns
            X = (25*x)+(midX-((25*MAZE_WIDTH) / 2)) #set the X coordinate to be 25x bigger than maze index
            Y = (25*y)+(midY-(25*MAZE_HEIGHT)) #set the Y coordinate to be 25x bigger than maze index
            if maze[x][y] == False: #check if maze index is a wall
                wall = Wall([X,Y]) #set up a wall sprite with X and Y as the location
                walls.add(wall) #add it to the 'walls' group
                all_sprites.add(wall) #add it to the 'all_sprites' group
            elif maze[x][y] == True:  #check if maze index is a cell
                cell = Cell([X,Y]) #set up a cell sprite with X and Y as the location
                cells.add(cell) #add it to the 'cells' group
                all_sprites.add(cell) #add it to the 'all_sprites' group
            else: #otherwise:
                empty = Empty([X,Y]) #set up an empty sprite with X and Y as the location
                all_sprites.add(empty) #adds it to the 'all_sprites' group
                if x == (MAZE_WIDTH-1): #if it is the exit of the maze
                    keys = pygame.sprite.Group() #create a sprite group for keys
                    key = Key("Key.png", [X,Y]) #set up a key sprite with X and Y as the location
                    all_sprites.add(key) #adds it to the 'all_sprites' group
                    keys.add(key) #adds it to the 'keys' group
                    return keys, visited #returns the 'keys' group to the 'pygame_window' class and also visited 2D array  

class win_screen(screens):
    def __init__(self):
        super().__init__()
        
        #initiate pygame
        pygame.init()
        
        #instantiate sprites
        self.WinScreen = winScreen()
        
        #add sprites to all_sprites
        self._all_sprites.add(self.WinScreen)

    def display(self):
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

            #fills the pygame window with white
            self._win.fill((0,0,0))

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class lose_screen(screens):
    def __init__(self):
        super().__init__()
        
        #initiate pygame
        pygame.init()
        
        #instantiate sprites
        self.LoseScreen = loseScreen()
        
        #add sprites to all_sprites
        self._all_sprites.add(self.LoseScreen)

    def display(self):
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

            #fills the pygame window with white
            self._win.fill((0,0,0))

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class controls_screen(screens):
    def __init__(self):
        super().__init__()
        
        #initiate pygame
        pygame.init()

        #instantiate sprites
        self.__controls_image = controlsImage()
        
        #add sprites to all_sprites
        self._all_sprites.add(self.__controls_image)
    
    def display(self):
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.run_main()

            #fills the pygame window with white
            self._win.fill((0,0,0))

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class instructions_screen(screens):
    def __init__(self):
        super().__init__()
        
        #initiate pygame
        pygame.init()
        
        #instantiate sprites
        self.__instructions_image = instructionsImage()

        #add sprites to all_sprites
        self._all_sprites.add(self.__instructions_image)
    
    def display(self):
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
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    game.run_main()

            #fills the pygame window with white
            self._win.fill((0,0,0))

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class start_screen(screens):
    def __init__(self):
        super().__init__()
        
        #initiate pygame
        pygame.init()

        #Calculate where the middle of the screen is
        self.__winX = self._winXY[0]
        self.__winY = self._winXY[1]
        self.__midX = self.__winX / 2
        self.__midY = self.__winY / 2
        
        #instantiate sprites
        self.__locX1 = self.__midX
        self.__locX2 = 400
        self.__locX3 = self.__midX - 200
        self.__locX4 = self.__midX + 200
        self.__locX5 = self.__winX - 400
        self.__locY1 = self.__midY - (self.__midY / 2)
        self.__locY2 = self.__midY + (self.__midY / 2)
        self.__title = Title((self.__locX1,self.__locY1),"Welcome to Maths Maze Navigator")
        self.__controls = Controls((self.__locX2,self.__locY2),"Controls")
        self.__play = Play((self.__locX3,self.__locY2),"Play game")
        self.__instructions = Instructions((self.__locX4,self.__locY2),"How to play")
        self.__quit = Quit((self.__locX5,self.__locY2),"Quit!")
        
        #add sprites to all_sprites
        self._all_sprites.add(self.__title)
        self._all_sprites.add(self.__controls)
        self._all_sprites.add(self.__play)
        self._all_sprites.add(self.__instructions)
        self._all_sprites.add(self.__quit)
        
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
                        game.run_controls()
                    if loc5 <= mouse[0] <= loc6 and loc3 <= mouse[1] <= loc4:
                        game.run_main()
                    if loc7 <= mouse[0] <= loc8 and loc3 <= mouse[1] <= loc4:
                        game.run_instructions()
                    if loc9 <= mouse[0] <= loc0 and loc3 <= mouse[1] <= loc4:
                        run = False

            #fills the pygame window with white
            self._win.fill((0,0,0))

            mouse = pygame.mouse.get_pos()

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class pygame_window(screens):
    def __init__(self, MAZE_HEIGHT, MAZE_WIDTH, maze):
        super().__init__()
        
        #assign parameters to variables
        self.__maze_height = MAZE_HEIGHT
        self.__maze_width = MAZE_WIDTH
        self.__maze = maze
        
        #initiate pygame
        pygame.init() 

        #Calculate where the middle of the screen is
        self.__winX = self._winXY[0]
        self.__winY = self._winXY[1]
        self.__midX = self.__winX / 2
        self.__midY = self.__winY / 2
        
        #instantiate sprites
        self.__player = Player("Player.png",[600,300])
        self.__locX1 = self.__midX - 250
        self.__locX2 = self.__midX - 100
        self.__locX3 = self.__midX + 100
        self.__locX4 = self.__midX + 250
        self.__locY = self.__midY + (self.__midY / 2)
        self.__scoreBoard = Scoreboard(15,"white",100,150,self.__locX1,self.__locY)
        self.__livesCounter = LivesC(15,"white",100,150,self.__locX2,self.__locY)
        self.__movesCounter = MovesC(15,"white",100,150,self.__locX3,self.__locY)
        self.__timer = Timer(15,"white",100,150,self.__locX4,self.__locY)

        #Set variables for Scoreboard, Lives counter, Moves counter and Timer
        self.__CurrentScore = 0
        self.__lives = 300
        self.__moves = 0
        self.__Time = 0

        #instantiate the 'GameSave' class
        gameSave = GameSave(maze, self.__CurrentScore, self.__lives, self.__moves, self.__Time)
        
        #create sprite groups
        self.__walls = pygame.sprite.Group()
        self.__cells = pygame.sprite.Group()

        #add sprites to all_sprites
        self._all_sprites.add(self.__player)
        self._all_sprites.add(self.__scoreBoard)
        self._all_sprites.add(self.__livesCounter)
        self._all_sprites.add(self.__movesCounter)
        self._all_sprites.add(self.__timer)
    
    def display(self):
        #call the function to generate the maze and 'catch' the 2 variables it returns
        keys, visited = generate_maze(self.__maze_height, self.__maze_width, self.__maze, self.__walls,
                             self.__cells, self._all_sprites, self.__midX, self.__midY)

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
                        pygame.display.toggle_fullscreen()
                if event.type == pygame.MOUSEBUTTONUP: #checks if a keyboard key is pressed
                    pygame.time.set_timer(event, 1000)#sets a timer for 1 second
                    self.__Time += 1

            #fills the pygame window with white
            self._win.fill((0,0,0))

            #stores the key that the user presses
            pressed_keys = pygame.key.get_pressed()

            for sprite in self._all_sprites: #set a FOR loop to cycle through the whole list of sprites
                self._win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on

            #calls the move method of the player with the key that the user presses as the parameter
            self.__moves = self.__player.move(pressed_keys, self.__moves)
            self.__movesCounter.update(self.__moves,15,"white",100,150) #calls the update method of the 'movesCounter'
            self.__timer.update(self.__Time,15,"white",100,150) #update the timer

            #checks if the player collides with any of the walls
            if pygame.sprite.spritecollideany(self.__player, self.__walls):
                self.__player.kill() #if it does then despawn the player
                #calls the update method of the 'livesCounter'
                self.__lives = self.__livesCounter.update(self.__lives,15,"white",100,150) 
                
            #checks if the lives has gone below 0
            if self.__lives < 0:
                game.run_lose() #if it has then runs the lose end screen

            #store the cell that the player collides with as 'thisCell'
            thisCell = pygame.sprite.spritecollideany(self.__player, self.__cells)

            #run a FOR loop through all the cells
            for cell in self.__cells:
                if thisCell == cell: #check if the current cell is 'thisCell'
                    #respawn the player on top of the cell
                    player = Player("Player.png",cell.getLocation())
                    
                    self._win.blit(player.surf, player.rect) 
                    pygame.display.update() #updates the display

            #checks if the player collides with the keys
            if pygame.sprite.spritecollideany(self.__player, keys):
                self.__CurrentScore = 1000 - (25 * self.__moves) #if it does calculate the score
                self.__scoreBoard.update(self.__CurrentScore,15,"white",100,150) #calls the update method of the 'scoreBoard'
                sleep(2) #sleeps the program for 2 minutes
                game.run_win() #runs the win end screen
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window
    
#set up the game class
class Game(object):
    #set the constructor method with 3 parameters
    def __init__(self, MAZE_HEIGHT, MAZE_WIDTH, maze):
        #set the 'display' attributes to the various classes
        self.display1 = start_screen()
        self.display2 = pygame_window(MAZE_HEIGHT, MAZE_WIDTH, maze)
        self.display3 = controls_screen()
        self.display4 = instructions_screen()
        self.display5 = win_screen()
        self.display6 = lose_screen()

    #set up the run_start method which will call the display method of the 'start_screen' class
    def run_start(self):
        self.display1.display() #call the display method of the class assigned to 'display1'

    #set up the run_controls method which will call the display method of the 'controls_screen' class
    def run_controls(self):
        self.display3.display() #call the display method of the class assigned to 'display3'

    #set up the run_instructions method which will call the display method of the 'instructions_screen' class
    def run_instructions(self):
        self.display4.display() #call the display method of the class assigned to 'display4'

    #set up the run_main method which will call the display method of the 'pygame_window' class
    def run_main(self):
        self.display2.display() #call the display method of the class assigned to 'display2'

    #set up the run_win method which will call the display method of the 'win_screen' class
    def run_win(self):
        self.display5.display() #call the display method of the class assigned to 'display5'

    #set up the run_lose method which will call the display method of the 'lose_screen' class
    def run_lose(self):
        self.display6.display() #call the display method of the class assigned to 'display6'

#set up an if statement for the main part of the program
if __name__ == "__main__":
    game = Game(MAZE_HEIGHT, MAZE_WIDTH, maze) #instantiate the game class
    game.run_start() #call the run method of the game class
    screen = screens() #set up the base class for the other screens
