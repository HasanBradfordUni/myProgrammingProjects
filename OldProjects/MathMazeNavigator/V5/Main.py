#main program
import pygame
from tkinter import *

from time import sleep
from random import randint,random

from Player_class import Player
from Maze_objects import Wall, Cell, Empty, Key
from Information_objects import Scoreboard, LivesC, MovesC, Timer, SaveButton, LoadButton, UndoButton
from Starting_objects import Title, Controls, Play, Instructions, Quit
from Other_objects import controlsImage, instructionsImage, winScreen, loseScreen, SS_image, LS_image
from GameSave_class import GameSave
from HighScores_class import HighScores
from QS_objects import Text1, Button1, Button2, Button3, Button4, Button5

MAZE_HEIGHT = 10 
MAZE_WIDTH = 10
MAZE_CONSTANT = 25

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

#the 'get_questions' function which imports the questions from a file and returns them as a 2D array
def get_questions(fileName):
    questions = [] #initialises the variable 'questions' as an empty array
    for line in fileName: #runs a FOR loop through each line of the file
        newLine = line.strip("\n").split(",") #creates the array which will be appended to 'questions'
        questions.append(newLine) #appends the array stored in 'newLine' to 'questions'
    return questions #returns the 'questions' 2D array to the app class

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
            X = (MAZE_CONSTANT*x)+(midX-((MAZE_CONSTANT*MAZE_WIDTH) / 2)) #set the X coordinate to be 25x bigger than maze index
            Y = (MAZE_CONSTANT*y)+(midY-(MAZE_CONSTANT*MAZE_HEIGHT)) #set the Y coordinate to be 25x bigger than maze index
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

#Class for a Tkinter window called 'QuestionWindow'
class QuestionWindow(Tk):
    def __init__(self, questions, score):
        super().__init__() #uses the super construcor for 'Tk'

        #set the window attributes up
        self.geometry('2000x500')
        self.title('Questions')
        self.configure(bg="#12AAE6")

        #set the question up for the main label
        self.question = questions[0]
        thisQuestion = self.question[0]

        #set the multi-choice answers for the buttons
        answer1 = self.question[1]
        answer2 = self.question[2]
        answer3 = self.question[3]
        answer4 = self.question[4]

        #set some variables
        correctAnswer = answer1
        self.Score = StringVar()
        self.movesLeft = 0
        self.score = score
        self.status = "Incorrect!"

        #set the question text label up
        label1 = Label(self, text=thisQuestion, bg="#12AAE6")
        label1.config(font=('Helvetica bold',20))
        label1.grid(row=0,columnspan=2) #arrange using the grid method in row 0

        #set up the buttons for the answer choices
        number1 = Button(self, text=answer1, bg="#12AAE6", command=lambda: self.ansPressed(answer1, correctAnswer))
        number1.grid(row=1, column=0) #arrange using the grid method in row 1, col 0
        number2 = Button(self, text=answer2, bg="#12AAE6", command=lambda: self.ansPressed(answer2, correctAnswer))
        number2.grid(row=1, column=1) #arrange using the grid method in row 1, col 1
        number3 = Button(self, text=answer3, bg="#12AAE6", command=lambda: self.ansPressed(answer3, correctAnswer))
        number3.grid(row=2, column=0) #arrange using the grid method in row 2, col 0 
        number4 = Button(self, text=answer4, bg="#12AAE6", command=lambda: self.ansPressed(answer4, correctAnswer))
        number4.grid(row=2, column=1) #arrange using the grid method in row 2, col 1

        #set the score box as a disabled entry that only the program can update
        self.scoreBox = Entry(self, bg="#12AAE6", textvariable=self.Score)
        self.scoreBox.config(state= "disabled")
        self.scoreBox.grid(row=3, column=1) #arrange this using grid method in row 3, col 1

        self.Score.set(str(self.score))

        #set the score text label up
        label2 = Label(self, text="Score:", bg="#12AAE6")
        label2.config(font=('Helvetica bold',10))
        label2.grid(row=3, column=0) #arrange using the grid method in row 3, col 0

    def ansPressed(self, answer, correctAnswer):
        if answer == correctAnswer: #check if the answer the user chose is correct
            self.status = "Correct!" #if it is, set status to 'Correct!'
            self.score += 1 #increment the score by 1
        else: #otherwise
            self.status = "Incorrect!" #if it is, set status to 'Incorrect!'
            self.score -= 1  #decrement the score by 1
        self.Score.set(str(self.score)) #set the 'Score' text variable to be the attribute 'currentScore'
        self.destroy()

    def return_info(self):
        self.currentScore = self.score
        if self.status == "Correct!":
            self.movesLeft = 5
        else:
            self.movesLeft = 1
        return self.currentScore, self.movesLeft

class QuestionSelect_screen(screens):
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
        self.__locY1 = 150
        self.__locY2 = self.__midY - 200
        self.__locY3 = self.__midY - 50
        self.__locY4 = self.__midY + 100
        self.__locY5 = self.__midY + 250 
        self.__locY6 = self.__winY - 100
        self.__SyQD = Text1((self.__locX1,self.__locY1),"Select your Question Difficulty")
        self.__GCSE = Button1((self.__locX1,self.__locY2),"GCSE")
        self.__Easy = Button2((self.__locX1,self.__locY3),"Easy")
        self.__Medium = Button3((self.__locX1,self.__locY4),"Medium")
        self.__Hard = Button4((self.__locX1,self.__locY5),"Hard")
        self.__NS = Button5((self.__locX1,self.__locY6),"Ninson's specials")
        
        #add sprites to all_sprites
        self._all_sprites.add(self.__SyQD)
        self._all_sprites.add(self.__GCSE)
        self._all_sprites.add(self.__Easy)
        self._all_sprites.add(self.__Medium)
        self._all_sprites.add(self.__Hard)
        self._all_sprites.add(self.__NS)
        
    def display(self, qs_diff):

        #get location for buttons where mouse could be clicked
        loc1 = self.__locX1 - 100
        loc2 = self.__locX1 + 100
        loc3 = self.__locY5 - 50
        loc4 = self.__locY5 + 50
        loc5 = self.__locY2 - 50
        loc6 = self.__locY2 + 50
        loc7 = self.__locY3 - 50
        loc8 = self.__locY3 + 50
        loc9 = self.__locY4 - 50
        loc10 = self.__locY4 + 50
        loc11 = self.__locY6 - 50
        loc12 = self.__locY6 + 50
        
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
                    if loc1 <= mouse[0] <= loc2 and loc5 <= mouse[1] <= loc6:
                        qs_diff = "GCSE"
                        game.run_main(qs_diff)
                    if loc1 <= mouse[0] <= loc2 and loc7 <= mouse[1] <= loc8:
                        qs_diff = "Easy"
                        game.run_main(qs_diff)
                    if loc1 <= mouse[0] <= loc2 and loc9 <= mouse[1] <= loc10:
                        qs_diff = "Medium"
                        game.run_main(qs_diff)
                    if loc1 <= mouse[0] <= loc2 and loc3 <= mouse[1] <= loc4:
                        qs_diff = "Hard"
                        game.run_main(qs_diff)
                    if loc1 <= mouse[0] <= loc2 and loc11 <= mouse[1] <= loc12:
                        qs_diff = "NS"
                        game.run_main(qs_diff)

            #fills the pygame window with white
            self._win.fill((0,0,0))

            #stores the position of the mouse
            mouse = pygame.mouse.get_pos()

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class high_scores_screen2(Toplevel):
    def __init__(self, parent, score, name, movesBonus, questionsBonus, livesBonus):
        super().__init__(parent) #use the super constructor of hss1
        
        high_scores = HighScores() #instantiate the 'HighScores' class 

        scoreValid = None #set up the varaible to check if the score is valid as 'None'

        fileIn = open('high_scores.txt', 'r') #open the file that will be passed into the 'HighScores' class
        high_scores.get_scores(fileIn) #get the scores from the file
        fileIn.close() #close the file that was passed in

        if high_scores.check_score(score): #checks the score and if it returns True then...
            scoreValid = True #sets ScoreValid to True
            high_scores.add_score(name, score) #adds the score
            sortedNames = high_scores.sortNames() #sorts the names dictionary and returns it as an array of tuples
            sortedNames = sortedNames[::-1] #reverse it so it's in desending order
            fileOut = open('high_scores.txt', 'w') #opens the file which will be written to
            high_scores.saveScore(fileOut, sortedNames) #saves the name and score to the file
            fileOut.close() #closes the file that was written to
        else: #otherwise...
            scoreValid = False #sets scoreValid to False

        #set the window attributes up
        self.geometry('1650x1000')
        self.title('Maths Maze Navigator')
        self.configure(bg="#12AAE6")

        #set the main text label up and arrange using the grid method in row 0
        label1 = Label(self, text="High Scores", bg="#12AAE6")
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=0,columnspan=2)

        #set the textBox up which will display the highscores and arrange using grid method in row 1
        self.textBox = Text(self, background="#12AAE6")
        self.textBox.grid(row=1, columnspan=2)

        if scoreValid: #checks if the score is valid
            self.textBox.delete("1.0", END) #if it is clears the textBox
        else: #otherwise...
            sortedNames = high_scores.sortNames() #gets the sortedNames array
            sortedNames = sortedNames[::-1] #reverse it so it's in desending order

        self.textBox.delete("1.0", END) #clears the textBox anyway
        for num in range(1, len(sortedNames)+1): #uses a FOR loop to iterate over over the sortedNames array
            nameScore = sortedNames[num-1] #get the current name and score and stores it
            name = nameScore[0] #gets the name seperately
            score = nameScore[1] #gets the score seperately
            text = str(num)+"."+name+": "+str(score)+"\n" #creates the text which will be inserted into the textBox
            self.textBox.insert(END, text) #inserts the text into the textBox

        #set up a button which closes the window
        Button(self,text='More Info',bg="#12AAE6",command=lambda: self.displayInfo(movesBonus, questionsBonus, livesBonus)).grid(row=2, column=0)
        Button(self,text='Close',bg="#12AAE6",command=self.destroy).grid(row=2, column=1)

    def displayInfo(self, movesBonus, questionsBonus, livesBonus):
        text1 = f"Moves bonus: {movesBonus} \n"
        text2 = f"Questions bonus: {questionsBonus} \n"
        text3 = f"Lives bonus: {livesBonus} \n"
        text4 = "Completion bonus: 500 \n"
        self.textBox.insert(END, "\n")
        self.textBox.insert(END, text1) #inserts the text into the textBox
        self.textBox.insert(END, text2) #inserts the text into the textBox
        self.textBox.insert(END, text3) #inserts the text into the textBox
        self.textBox.insert(END, text4) #inserts the text into the textBox

class high_scores_screen1(Tk):
    def __init__(self, score, movesBonus, questionsBonus, livesBonus):
        super().__init__()
        
        #set the window attributes up
        self.geometry('1650x1000')
        self.title('Maths Maze Navigator')
        self.configure(bg="#12AAE6")

        text = f"Your score is: {score}"
        #set the main text label up and arrange using the grid method in row 0
        label1 = Label(self, text=text, bg="#12AAE6")
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=0,columnspan=2)

        #set up the secondary text label and arrange using the grid method in row 1, column 1
        label2 = Label(self, text="Enter name here:", bg="#12AAE6")
        label2.config(font=('Helvetica Bold',20))
        label2.grid(row=1,column=0)

        #set up the entry where the user will enter their name
        self.entry1 = Entry(self, bg="#12AAE6")
        self.entry1.grid(row=1, column=1) #arrange using grid method in row 1, column 1

        #set up the textBox and arrange using grid method in row 2
        self.textBox = Text(self, background="#12AAE6")
        self.textBox.grid(row=2, columnspan=2)

        #set up a button which opens the new window for the high scores
        Button(self,text='Submit score',bg="#12AAE6",command=lambda: self.open_window(score, movesBonus, questionsBonus, livesBonus)).grid(row=3, column=0)
        #set up a button which closes the window
        Button(self,text='Close',bg="#12AAE6",command=self.destroy).grid(row=3, column=1)

    #the method to open the new window and check entry
    def open_window(self, score, movesBonus, questionsBonus, livesBonus):
        name = self.entry1.get() #get the name from the entry
        if len(name) > 10 or len(name) < 2: #check if the name is valid
            #if it isn't, insert a suitable error message into the textBox
            text = "Error: Name has to be between 2 and 10 characters long!"
            self.textBox.delete("1.0", END)
            self.textBox.insert("1.0", text)
        else: #otherwise...
            hss2 = high_scores_screen2(self, score, name, movesBonus, questionsBonus, livesBonus) #calls the Tkinter window 'high_scores_screen2'
            hss2.grab_set() #makes it so that events can run in the tkinter window

class save_screen(screens):
    def __init__(self, maze, CurrentScore, lives, moves, Time):
        super().__init__()
        
        #initiate pygame
        pygame.init()
        
        #instantiate sprites
        self.SaveScreen = SS_image()
        
        #add sprites to all_sprites
        self._all_sprites.add(self.SaveScreen)

        #instantiate the 'GameSave' class
        self.__gameSave = GameSave(maze, CurrentScore, lives, moves, Time)

    def save(self, coords):
        file = open("mazeInfo.txt", 'w')
        self.__gameSave.writeToFile(file, coords)
        file.close()

    def display(self, qs_diff):
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
                    game.run_main(qs_diff)

            #fills the pygame window with white
            self._win.fill((0,0,0))

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

class load_screen(screens):
    def __init__(self, maze, CurrentScore, lives, moves, Time, playerPos, midX, midY):
        #set up attributes using passed parameters
        self.__savedMaze = maze
        self.__CurrentScore = CurrentScore
        self.__lives = lives
        self.__moves = moves
        self.__Time = Time
        self.__playerPos = playerPos
        self.__midX = midX
        self.__midY = midY

        super().__init__()
        
        #initiate pygame
        pygame.init()
        
        #instantiate sprites
        self.LoadScreen = LS_image()
        
        #add sprites to all_sprites
        self._all_sprites.add(self.LoadScreen)

    def display(self, qs_diff):
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
                    game.run_main(qs_diff)

            #fills the pygame window with white
            self._win.fill((0,0,0))

            for sprite in self._all_sprites: #set a for loop to cycle through the whole list of sprites
                self._win.blit(sprite.image, sprite.rect) #blit each sprite on to the screen
            pygame.display.update() #update the display with all sprites blitted on
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

    def loadMaze(self, maze, midX, midY):
        all_sprites = pygame.sprite.Group()
        walls = pygame.sprite.Group()
        cells = pygame.sprite.Group()
        #set up a FOR loop for the rows of the maze
        for x in range(0, MAZE_HEIGHT):
            for y in range(0, MAZE_WIDTH): #set up a nested FOR loop for the maze columns
                X = (MAZE_CONSTANT*x)+(midX-((MAZE_CONSTANT*MAZE_WIDTH) / 2)) #set the X coordinate to be 25x bigger than maze index
                Y = (MAZE_CONSTANT*y)+(midY-(MAZE_CONSTANT*MAZE_HEIGHT)) #set the Y coordinate to be 25x bigger than maze index
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
        return walls, cells, all_sprites

    def loadGame(self, all_sprites, MAZE_HEIGHT, MAZE_WIDTH):
        self._new_sprites = all_sprites

        pixelX = (MAZE_CONSTANT*int(self.__playerPos[1]))+(self.__midX-((MAZE_CONSTANT*MAZE_WIDTH) / 2))
        pixelY = (MAZE_CONSTANT*int(self.__playerPos[4]))+(self.__midY-(MAZE_CONSTANT*MAZE_HEIGHT))
        player = Player("Player.png",[pixelX, pixelY])

        self.__locX1 = self.__midX - 250
        self.__locX2 = self.__midX - 100
        self.__locX3 = self.__midX + 100
        self.__locX4 = self.__midX + 250
        self.__locY = self.__midY + (self.__midY / 2)
        self.__scoreBoard = Scoreboard(15,"white",100,150,self.__locX1,self.__locY)
        self.__livesCounter = LivesC(15,"white",100,150,self.__locX2,self.__locY)
        self.__livesCounter.set(self.__lives,15,"white",100,150)
        self.__movesCounter = MovesC(15,"white",100,150,self.__locX3,self.__locY)
        self.__movesCounter.update(self.__moves,15,"white",100,150)
        self.__timer = Timer(15,"white",100,150,self.__locX4,self.__locY)
        self.__timer.update(self.__Time,15,"white",100,150)

        self._new_sprites.add(player)
        self._new_sprites.add(self.__scoreBoard)
        self._new_sprites.add(self.__livesCounter)
        self._new_sprites.add(self.__movesCounter)
        self._new_sprites.add(self.__timer)

        return self._new_sprites, player, self.__moves, self.__Time
    

class win_screen(screens):
    def __init__(self):
        super().__init__()
        
        #initiate pygame
        pygame.init()
        
        #instantiate sprites
        self.WinScreen = winScreen()
        
        #add sprites to all_sprites
        self._all_sprites.add(self.WinScreen)

    def display(self, currentScore, movesBonus, questionsBonus, livesBonus):
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
                    hss1 = high_scores_screen1(currentScore, movesBonus, questionsBonus, livesBonus) #calls the Tkinter window 'high_scores_screen1'
                    hss1.mainloop() #makes it so that events can run in the tkinter window

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

        #get location for buttons where mouse could be clicked
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
                        game.run_qss()
                    if loc7 <= mouse[0] <= loc8 and loc3 <= mouse[1] <= loc4:
                        game.run_instructions()
                    if loc9 <= mouse[0] <= loc0 and loc3 <= mouse[1] <= loc4:
                        run = False

            #fills the pygame window with white
            self._win.fill((0,0,0))

            #stores the position of the mouse
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
        self.__player = Player("Player.png",[800,275])
        self.__locX1 = self.__midX - 250
        self.__locX2 = self.__midX - 100
        self.__locX3 = self.__midX + 100
        self.__locX4 = self.__midX + 250
        self.__locY = self.__midY + (self.__midY / 2)
        self.__locY1 = self.__midY - (self.__midY / 1.5)
        self.__scoreBoard = Scoreboard(15,"white",100,150,self.__locX1,self.__locY)
        self.__livesCounter = LivesC(15,"white",100,150,self.__locX2,self.__locY)
        self.__movesCounter = MovesC(15,"white",100,150,self.__locX3,self.__locY)
        self.__timer = Timer(15,"white",100,150,self.__locX4,self.__locY)
        self.__saveButton = SaveButton((self.__locX3,self.__locY1))
        self.__loadButton = LoadButton((self.__locX4,self.__locY1))
        self.__undoButton = UndoButton((self.__locX2,self.__locY1))

        #Set variables for Scoreboard, Lives counter, Moves counter and Timer
        self.__CurrentScore = 0
        self.__lives = 3
        self.__moves = 0
        self.__movesLeft = 5
        self.__Time = 0
        self.__coords = [0, 1]
        self.__file = None

        #instantiate the 'GameSave' class
        self.__gameSave = GameSave(maze, self.__CurrentScore, self.__lives, self.__moves, self.__Time)

        #set up the moves queue which will be used to undo moves
        self.movesQueue = []
        
        #create sprite groups
        self.__walls = pygame.sprite.Group()
        self.__cells = pygame.sprite.Group()

        #add sprites to all_sprites
        self._all_sprites.add(self.__scoreBoard)
        self._all_sprites.add(self.__livesCounter)
        self._all_sprites.add(self.__movesCounter)
        self._all_sprites.add(self.__timer)
    
    def display(self, qs_diff):
        #call the function to generate the maze and 'catch' the 2 variables it returns
        keys, visited = generate_maze(self.__maze_height, self.__maze_width, self.__maze, self.__walls,
                             self.__cells, self._all_sprites, self.__midX, self.__midY)

        #choose which file to get questions from
        if qs_diff == "GCSE":
            self.__file = open("GCSE_qs.txt", mode='r')
        elif qs_diff == "Easy":
            self.__file = open("Easy_qs.txt", mode='r')
        elif qs_diff == "Medium":
            self.__file = open("Medium_qs.txt", mode='r')
        elif qs_diff == "Hard":
            self.__file = open("Hard_qs.txt", mode='r')
        elif qs_diff == "NS":
            self.__file = open("NS_qs.txt", mode='r')
        else:
            print("An error has occured!")

        #get location for buttons where mouse could be clicked
        loc1 = self.__locX3 - 50
        loc2 = self.__locX3 + 50
        loc3 = self.__locX4 - 50
        loc4 = self.__locX4 + 50
        loc5 = self.__locY1 - 50
        loc6 = self.__locY1 - 20
        loc7 = self.__locX2 - 50
        loc8 = self.__locX2 - 10

        #set up necessary variables
        self.score = 0
        questions = get_questions(self.__file)
        self.calls = 0
        self.crashes = 0
        self.devMode = False
        self.moveUndone = False

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
                    if event.key == pygame.K_l:
                        self.devMode = True
                if event.type == pygame.MOUSEBUTTONUP: #checks if a keyboard key is pressed
                    pygame.time.set_timer(event, 1000) #sets a timer for 1 second
                    self.__Time += 1 #increments the 'Time' variable by 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if loc1 <= mouse[0] <= loc2 and loc5 <= mouse[1] <= loc6:
                        #save the game and call the 'save_screen' display method after instantiating it
                        SS = save_screen(self.__maze, self.__CurrentScore, self.__lives, self.__moves, self.__Time)
                        SS.save(self.__coords)
                        SS.display(qs_diff)
                    if loc3 <= mouse[0] <= loc4 and loc5 <= mouse[1] <= loc6:
                        #load the game and call the 'load_screen' display method after instantiating it
                        file = open("mazeInfo.txt", 'r')
                        maze, CurrentScore, lives, moves, Time, playerPos = self.__gameSave.loadMaze(file, self.__maze_height, self.__maze_width)
                        LS = load_screen(maze, CurrentScore, lives, moves, Time, playerPos, self.__midX, self.__midY)
                        self.__walls, self.__cells, self._all_sprites = LS.loadMaze(self.__maze, self.__midX, self.__midY)
                        self._all_sprites, self.__player, self.__moves, self.__Time = LS.loadGame(self._all_sprites, self.__maze_height, self.__maze_width)
                        LS.display(qs_diff)
                    if loc7 <= mouse[0] <= loc8 and loc5 <= mouse[1] <= loc6:
                        #call the 'undoMove' method of 'pygame_window' to undo the move
                        self.moveUndone = True

            #calls the maths question if 'movesLeft' is 0 or less and 'calls' is 10 or less
            if self.__movesLeft <= 0:
                if self.calls < 10:
                    self.open_question(questions)
                    self.calls += 1 #increment calls by 1
                else: #otherwise adds 100 moves as last question has been reached
                    self.__movesLeft += 100

            #fills the pygame window with white
            self._win.fill((0,0,0))

            if self.moveUndone:
                self.moveUndone = False
                if len(self.movesQueue) > 0:
                    self.lastMove = self.undoMove()
                    print(self.lastMove)
                    self.__player = Player("Player.png",self.lastMove)
                    self._win.blit(self.__player.surf, self.__player.rect) 
                    pygame.display.update() #updates the display
                    self.__movesLeft += 1
                else:
                    print("No move to undo")    

            #stores the key that the user presses
            pressed_keys = pygame.key.get_pressed()

            #stores the position of the mouse
            mouse = pygame.mouse.get_pos()

            for sprite in self._all_sprites: #set a FOR loop to cycle through the whole list of sprites
                self._win.blit(sprite.surf, sprite.rect) #blit each sprite on to the screen
            self._win.blit(self.__saveButton.image, self.__saveButton.rect)
            self._win.blit(self.__loadButton.image, self.__loadButton.rect)
            self._win.blit(self.__undoButton.image, self.__undoButton.rect)
            self._win.blit(self.__player.surf, self.__player.rect)
            pygame.display.update() #update the display with all sprites blitted on

            #calls the move method of the player with the key that the user presses as the parameter
            self.__moves, self.__movesLeft = self.__player.move(pressed_keys, self.__moves, self.__movesLeft)
            playerCoords = self.__player.getCoords()
            self.__movesCounter.update(self.__movesLeft,15,"white",100,150) #calls the update method of the 'movesCounter'
            self.__timer.update(self.__Time,15,"white",100,150) #update the timer

            #checks if the player collides with any of the walls
            if pygame.sprite.spritecollideany(self.__player, self.__walls):
                if not self.devMode:
                    self.__player.kill() #if it does then despawn the player
                    self.__player = Player("Player.png",[800,275]) #re-instantiate the player
                    self._win.blit(self.__player.surf, self.__player.rect) #respawn the player
                    self.crashes += 1 #increments 'crashes' by 1
                    if self.crashes % 5 == 0: #checks if the crashes is a multiple of 5                   
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
                    #respawn the player on top of the cell and update 'coords'
                    cellLoc = cell.getLocation()
                    if not self.moveUndone:
                        player = Player("Player.png",cellLoc)
                        self._win.blit(player.surf, player.rect) 
                        pygame.display.update() #updates the display
                    if self.checkQueue(cellLoc):
                        if len(self.movesQueue) == 5: #if the queue reaches max size...
                            first = self.movesQueue[0] #get the first item from the queue
                            self.movesQueue.remove(first) #remove the first item from the queue
                        self.movesQueue.append(cellLoc) #append the new playerCoords to the 'movesQueue'
                    self.__coords = self.__gameSave.calcPlayerPos(cellLoc, MAZE_HEIGHT, MAZE_WIDTH, self.__midX, self.__midY)
                    X = self.__coords[0]
                    Y = self.__coords[1]
                    visited[Y][X] = True

            #checks if the player collides with the keys
            if pygame.sprite.spritecollideany(self.__player, keys):
                self.movesBonus = 1500 - (MAZE_CONSTANT * self.__moves) 
                self.questionsBonus = self.score * MAZE_CONSTANT
                self.livesBonus = self.__lives * MAZE_CONSTANT
                self.__CurrentScore = 500 + self.movesBonus + self.questionsBonus + self.livesBonus #if it does calculate the score
                self.__scoreBoard.update(self.__CurrentScore,15,"white",100,150) #calls the update method of the 'scoreBoard'
                sleep(2) #sleeps the program for 2 seconds
                game.run_win(self.__CurrentScore, self.movesBonus, self.questionsBonus, self.livesBonus) #run the win screen from its display method in game
                
        #detects if run is set to False
        if not run:
            sleep(2) #waits for 2 seconds
            pygame.quit() #closes the pygame window

    def open_question(self, questions):
        window = QuestionWindow(questions, self.score) #if it is, calls the window for next question
        window.mainloop() #allows events to happen within the window object
        question = questions[0] #get the first question from the array
        questions.remove(question) #remove the previous question from the questions array
        self.score, self.__movesLeft = window.return_info() #gets the new score and movesLeft from 'window'

    def undoMove(self):
        lastMove = self.movesQueue[len(self.movesQueue)-1] #get the last item from the queue
        self.movesQueue.remove(lastMove) #remove the last item from the queue
        print("Move undone successfully")
        return lastMove

    def checkQueue(self, cellLoc):
        moveSafe = True
        for num in range(0, len(self.movesQueue)):
            if self.movesQueue[num] == cellLoc:
                moveSafe = False
            else:
                moveSafe = True
        return moveSafe

#set up the game class
class Game(object):
    #set the constructor method with 3 parameters
    def __init__(self, MAZE_HEIGHT, MAZE_WIDTH, maze, qs_diff):
        self.__qs_diff = qs_diff
        #set the 'display' attributes to the various classes
        self.display1 = start_screen()
        self.display2 = pygame_window(MAZE_HEIGHT, MAZE_WIDTH, maze)
        self.display3 = controls_screen()
        self.display4 = instructions_screen()
        self.display5 = win_screen()
        self.display6 = lose_screen()
        self.display7 = QuestionSelect_screen()

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
    def run_main(self, qs_diff):
        self.display2.display(qs_diff) #call the display method of the class assigned to 'display2'

    #set up the run_win method which will call the display method of the 'win_screen' class
    def run_win(self, currentScore, movesBonus, questionsBonus, livesBonus):
        self.display5.display(currentScore, movesBonus, questionsBonus, livesBonus) #call the display method of the class assigned to 'display5'

    #set up the run_lose method which will call the display method of the 'lose_screen' class
    def run_lose(self):
        self.display6.display() #call the display method of the class assigned to 'display6'

    #set up the run_qss method which will call the display method of the 'QuestionSelect_screen' class
    def run_qss(self):
        self.display7.display(self.__qs_diff) #call the display method of the class assigned to 'display7'

#set up an if statement for the main part of the program
if __name__ == "__main__":
    qs_diff = ""
    game = Game(MAZE_HEIGHT, MAZE_WIDTH, maze, qs_diff) #instantiate the game class
    game.run_start() #call the run method of the game class
