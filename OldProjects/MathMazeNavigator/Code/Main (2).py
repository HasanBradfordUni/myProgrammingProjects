#main program
import pygame

from time import sleep
from random import randint,random

from Player_class import Player
from Maze_objects import Wall, Cell, Empty

MAZE_HEIGHT = 10 
MAZE_WIDTH = 10

maze = []

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

def generate_maze(MAZE_HEIGHT, MAZE_WIDTH, maze, walls, cells, all_sprites):
    #set up a FOR loop for the rows of the maze
    for x in range(0, MAZE_HEIGHT):
        mazeRow = [] #initialise the 'mazeRow' as an empty array
        for y in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze columns
            mazeRow.append("None") #append the value which will be used for empty sections of the maze  
        maze.append(mazeRow) #append the 'mazeRow' full of 'None' strings to 'maze'

    #calls the 'create_paths' function which returns the 'maze' array
    maze = create_paths(maze, MAZE_HEIGHT, MAZE_WIDTH)

    #set up a FOR loop for the rows of the maze
    for i in range(0, MAZE_HEIGHT):
        for j in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze columns
            if (maze[i][j] == 'None'): #use an IF statement to check if an item in 'maze' is 'None'
                maze[i][j] = False #if it is 'None' sets it to False for the walls of the maze

    #sets the entrance and exit of the maze
    maze[0][1] = 'None'
    maze[9][8] = 'None'

    #set up a FOR loop for the rows of the maze
    for x in range(0, MAZE_HEIGHT):
        for y in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze columns
            X = (25*x)+500 #set the X coordinate to be 25x bigger than maze index and 500 to right
            Y = (25*y)+100 #set the Y coordinate to be 25x bigger than maze index and 100 down
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

class pygame_window(object):
    def __init__(self, MAZE_HEIGHT, MAZE_WIDTH, maze):
        #assign arguments to variables
        self.__maze_height = MAZE_HEIGHT
        self.__maze_width = MAZE_WIDTH
        self.__maze = maze
        
        #initiate pygame
        pygame.init()

        #set the window up with title
        self.__win = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Maths Maze Navigator")

        #instantiate sprites
        self.__player = Player("Player.png",[500,100])

        #create sprite groups
        self.__all_sprites = pygame.sprite.Group()
        self.__walls = pygame.sprite.Group()
        self.__cells = pygame.sprite.Group()

        #add player to all_sprites
        self.__all_sprites.add(self.__player)
    
    def display(self):
        #call the function to generate the maze
        generate_maze(self.__maze_height, self.__maze_width, self.__maze, self.__walls, self.__cells, self.__all_sprites)

        run = True
        #initiate a while loop until run is no longer True
        while run:
            #initiate a for loop to detect events
            for event in pygame.event.get():
                #allows the user to quit the game
                if event.type == pygame.QUIT:
                    run = False #sets run to False which breaks the loop

            #fills the pygame window with white
            self.__win.fill((0,0,0))

            #stores the key that the user presses
            pressed_keys = pygame.key.get_pressed()

            for sprite in self.__all_sprites: #set a for loop to cycle through the whole list of sprites
                self.__win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on

            #calls the move method of the player
            #with the key that the user presses as the parameter
            self.__player.move(pressed_keys)

            if pygame.sprite.spritecollideany(self.__player, self.__walls):
                self.__player.kill()
                run = False
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window
    
#set up the game class
class Game(object):
    #set the constructor method with 3 parameters
    def __init__(self, MAZE_HEIGHT, MAZE_WIDTH, maze):
        #set the 'display1' attribute to the pygame window class
        self.display1 = pygame_window(MAZE_HEIGHT, MAZE_WIDTH, maze)

    #set up the run method which will call the display method of the 'pygame_window' class
    def run(self):
        self.display1.display() #call the display method of the class assigned to 'display1'

#set up an if statement for the main part of the program
if __name__ == "__main__":
    game = Game(MAZE_HEIGHT, MAZE_WIDTH, maze) #instantiate the game class
    game.run() #call the run method of the game class
