#Game Save class
import pygame

class GameSave(object):
    #the constructor method of the class including all the information needed for game loading as the parameters
    def __init__(self, maze, CurrentScore, lives, moves, Time):
        #set up all the attributes of the class using the arguments provided
        self.__savedMaze = maze 
        self.__CurrentScore = CurrentScore
        self.__lives = lives
        self.__moves = moves
        self.__Time = Time

    #method to calculate the player's position in the maze with 5 parameters
    def calcPlayerPos(self, mazePos, MAZE_HEIGHT, MAZE_WIDTH, midX, midY):
        #uses a complex calculation to work out the X and Y values
        #this is the inverse operation to the one used when generating the maze
        X = (mazePos[0] - (midX - 12.5*MAZE_WIDTH)) / 25
        Y = (mazePos[1] - (midY - 25*MAZE_HEIGHT)) / 25
        self.__coords = [int(X),int(Y)]
        return self.__coords #returns these coordinates which are to be written to the file

    #method to write info to 'mazeInfo' file with 3 parameters
    def writeToFile(self, fileName, coords):
        #writes the attributes to the file
        for item in self.__savedMaze: #uses a FOR loop that iterates across the 'savedMaze' 2D array
            fileName.write(str(item)+"\n")
        fileName.write(str(self.__CurrentScore)+"\n")
        fileName.write(str(self.__lives)+"\n")
        fileName.write(str(self.__moves)+"\n")
        fileName.write(str(self.__Time)+"\n")
        fileName.write(str(coords)) #writes the passed coordinates to the file

    #method to load info from the file when loading the maze back with 3 parameters
    def loadMaze(self, fileName, MAZE_HEIGHT, MAZE_WIDTH):
        fileLines = [] #sets up an empty array for the output of the file
        maze = [] #resets the maze array
        for line in fileName: #uses a FOR loop that iterates across the file
            fileLines.append(line) #appends each line of the file to the output array
        for num in range(0, len(fileLines)): #uses a FOR loop that iterates across the 'fileLines' array
            if num < MAZE_HEIGHT: #checks if the line number is less than 'MAZE_HEIGHT'
                maze.append(fileLines[num]) #if it is, appends the line to maze
            elif MAZE_HEIGHT <= num < (MAZE_HEIGHT + 1): #checks if the line is the one after 
                CurrentScore = int(fileLines[num]) #if it is sets its integer value to 'CurrentScore'
            elif (MAZE_HEIGHT + 1) <= num < (MAZE_HEIGHT + 2): #checks if the line is the one after 
                lives = int(fileLines[num]) #if it is sets its integer value to 'lives'
            elif (MAZE_HEIGHT + 2) <= num < (MAZE_HEIGHT + 3): #checks if the line is the one after
                moves = int(fileLines[num]) #if it is sets its integer value to 'moves'
            elif (MAZE_HEIGHT + 3) <= num < (MAZE_HEIGHT + 4): #checks if the line is the one after
                Time = int(fileLines[num]) #if it is sets its integer value to 'Time'
            else: #checks if the line is any other one
                playerPos = fileLines[num] #if it is sets its value to 'playerPos'
        return maze, CurrentScore, lives, moves, Time, playerPos #returns all of these values to the 'Main' program
        
