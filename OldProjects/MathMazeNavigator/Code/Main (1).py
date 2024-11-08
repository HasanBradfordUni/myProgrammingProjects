#main program
import pygame
from time import sleep
from Player_class import Player
from Maze_objects import Wall, Cell, Empty

MAZE_HEIGHT = 10 
MAZE_WIDTH = 10

maze = []

def generate_maze(MAZE_HEIGHT, MAZE_WIDTH, maze, walls, cells):
    for x in range(0, MAZE_HEIGHT):
        mazeRow = []
        for y in range(0, MAZE_WIDTH):
            mazeRow.append("None")
        maze.append(mazeRow)

    for i in range(0, MAZE_HEIGHT):
        for j in range(0, MAZE_WIDTH):
            if (maze[i][j] == 'None'):
                maze[i][j] = False

    maze[3][4] = True
    maze[6][7] = True
    maze[8][8] = True

    for x in range(0, MAZE_HEIGHT):
        for y in range(0, MAZE_WIDTH):
            X = (25*x)+5
            Y = (25*y)+5
            if maze[x][y] == False:
                wall = Wall([X,Y])
                walls.add(wall)
            elif maze[x][y] == True:
                cell = Cell([X,Y])
                cells.add(cell)
            else:
                empty = Empty([X,Y])

def pygame_window(MAZE_HEIGHT, MAZE_WIDTH, maze):
    #initiate pygame
    pygame.init()

    #set the window up with title
    win = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Maths Maze Navigator")

    #instantiate sprites
    player = Player("Player.png")

    #create sprite groups
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    cells = pygame.sprite.Group()

    #add player to all_sprites
    all_sprites.add(player)
    
    #call the function to generate the maze
    generate_maze(MAZE_HEIGHT, MAZE_WIDTH, maze, walls, cells)

    run = True
    #initiate a while loop until run is no longer True
    while run:
        #initiate a for loop to detect events
        for event in pygame.event.get():
            #allows the user to quit the game
            if event.type == pygame.QUIT:
                run = False #sets run to False which breaks the loop

        #fills the pygame window with white
        win.fill((0,0,0))
        #blits the player on to the display
        win.blit(player.surf, player.rect)
        #updates the display
        pygame.display.update()

        #stores the key that the user presses
        pressed_keys = pygame.key.get_pressed()
        #calls the update method of the player
        #with the key that the user presses as the parameter
        player.move(pressed_keys)

        for cell in cells:
            win.blit(cell.surf, cell.rect)
        for wall in walls:
            win.blit(wall.surf, wall.rect)
        pygame.display.update()
        
    #detects if run is set to False    
    if not run:
        sleep(2) #waits for 2 seconds
        pygame.quit() #closes the pygame window
    
#set up the game class
class game(object):
    #set the constructor method with 5 parameters
    def __init__(self, MAZE_HEIGHT, MAZE_WIDTH, maze):
        #set the 'display1' attribute to the pygame window procedure
        self.display1 = pygame_window(MAZE_HEIGHT, MAZE_WIDTH, maze)

#set up an if statement for the main part of the program
if __name__ == "__main__":
    game(MAZE_HEIGHT, MAZE_WIDTH, maze) #instantiate the game class
