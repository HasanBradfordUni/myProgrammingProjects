import random, sys

class Player(object): #This is the object for the player class.
    """The Player Class"""
    def __init__(self, name, currentSpace, stunned): #Players are initialised with a set name and current space.
        self.name = name
        self.currentSpace = currentSpace
        self.stunned = stunned
    def moveForward(self, roll): #This moves the player by the number that they rolled.
        if self.currentSpace + roll <= 100: #This checks if the player is able to move by the rolled number without exceeding 100.
            self.currentSpace += roll
            print("You are now on space " + str(self.currentSpace) + "!")
            input()
            if self.currentSpace == 100: #This checks if the player's position is equal to 100.
                winDisplay()
        else:
            print("You cannot move this amount of spaces! You remain on space " + str(self.currentSpace) + "!")
            input()

def winDisplay(): #This is run if a player has won the game.
    print("You have won the game! Congratulations to all!")
    input()
    exit()

def displayMenu(): #This is run upon starting the program.
    print("1.New game \n2.How to play \n3.Quit program \nPlease select your choice! ")

def displayDifficultyMenu():
    print("\n1.Easy \n2.Normal \n3.Hard \n4.Custom \nPlease select the game difficulty! ")

def displayGameMenu(): #This is run every turn.
    print("1.Roll dice \n2.Exit game \nPlease select your choice! ")

def printInstructions(): #This is run if the user decides to select 'How to play'.
    print("\nSnakes and ladders is a dice board game in which players are required to roll a dice and then move their counter, depending on the number rolled from the dice, across the board upwards in a turn-based order in order to attempt to get to the last space at the end of the board before any other player does. The ladders and the snakes are randomly distributed around the board and if any player, after rolling the dice, lands on the bottom of a ladder, they are moved upwards, giving them an advantage on how many spaces are left in order to win the game over other players. However, if the space that’s landed on is the head of a snake, instead, the player is moved downwards and therefore putting them at a disadvantage over the other players.")
    input()
    displayMenu()
    
def checkChoice(choice): #This checks if the choice given is valid.
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Please select a valid choice! \n")
    else:
        if choice == "1":
            "Display difficulty menu"
        elif choice == "2":
            printInstructions()
            choice = input()
            checkChoice(choice)
        else:
            exit()

def checkDifficultyChoice(choice):
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        choice = input("Please select a valid choice! \n")
    else:
        if choice == "1":
            print("\nYou have selected easy mode!")
        elif choice == "2":
            print("\nYou have selected normal mode!")
        elif choice == "3":
            print("\nYou have selected hard mode!")
        else:
            print("\nYou have selected a custom difficulty mode!")
        return choice

def checkCustomDifficultyChoice(numOfLadders, numOfSnakes, numOfBonusRollSpaces, numOfLions):
    while True:
        try:
            numOfLadders = int(numOfLadders)
            numOfSnakes = int(numOfSnakes)
            numOfBonusRollSpaces = int(numOfBonusRollSpaces)
            numOfLions = int(numOfLions)
            break
        except:
            print("\nPlease select valid choices!")
            numOfLadders = input("Enter the number of ladders: ")
            numOfSnakes = input("Enter the number of snakes: ")
            numOfBonusRollSpaces = input("Enter the number of bonus roll spaces: ")
            numOfLions = input("Enter the number of lions: ")
    return numOfLadders, numOfSnakes, numOfBonusRollSpaces, numOfLions

def checkGameChoice(gameChoice): #This checks if the choice given in game is valid.
    while gameChoice != "1" and gameChoice != "2":
        gameChoice = input("Please select a valid choice! \n")
    else:
        if gameChoice == "2":
            answer = input("Are you sure you want to exit?(Yes/No) \n")
            while answer != "Yes" and answer != "yes" and answer != "No" and answer != "no":
                answer = input("Please select a valid answer!(Yes/No) \n")
            if answer == "Yes" or answer == "yes":
                exit()
            else:
                displayGameMenu()
                gameChoice = input()
                checkGameChoice(gameChoice)

def ladderCheck(currentTurn): #This is run each turn to check if the players position is equal to a ladder's position.
    if currentTurn == "Player 1":
        current = 0
        found = False
        while current < len(ladders) and found == False: #Running a linear search here.
            if ladders[current] == player1.currentSpace:
                found = True
                player1.currentSpace += 10
                print("Nice! You landed on a ladder! You went up 10 spaces and you are now on space " + str(player1.currentSpace) + "!")
                input()
            current = current + 1
    elif currentTurn == "Player 2":
        current = 0
        found = False
        while current < len(ladders) and found == False: #Running a linear search here.
            if ladders[current] == player2.currentSpace:
                found = True
                player2.currentSpace += 10
                print("Nice! You landed on a ladder! You went up 10 spaces and you are now on space " + str(player2.currentSpace) + "!")
                input()
            current = current + 1

def ladderSort(ladders): #Using bubble sort to sort the ladder spaces list into ascending order.
    laddersLen = len(ladders)
    for x in range(laddersLen-1):
        for y in range(laddersLen-x-1):
            if ladders[y] > ladders[y+1]:
                ladders[y], ladders[y+1] = ladders[y+1], ladders[y]
    return ladders

def snakeCheck(currentTurn): #This is run each turn to check if the players position is equal to a snake's position.
    if currentTurn == "Player 1":
        current = 0
        found = False
        while current < len(snakes) and found == False: #Running a linear search here.
            if snakes[current] == player1.currentSpace:
                found = True
                player1.currentSpace -= 10
                print("Ouch! You landed on a snake! You went down 10 spaces and you are now on space " + str(player1.currentSpace) + "!")
                input()
            current = current + 1
    elif currentTurn == "Player 2":
        current = 0
        found = False
        while current < len(snakes) and found == False: #Running a linear search here.
            if snakes[current] == player2.currentSpace:
                found = True
                player2.currentSpace -= 10
                print("Ouch! You landed on a snake! You went down 10 spaces and you are now on space " + str(player2.currentSpace) + "!")
                input()
            current = current + 1

def snakeSort(snakes): #Using bubble sort to sort the snake spaces list into ascending order.
    snakesLen = len(snakes)
    for x in range(snakesLen-1):
        for y in range(snakesLen-x-1):
            if snakes[y] > snakes[y+1]:
                snakes[y], snakes[y+1] = snakes[y+1], snakes[y]
    return snakes

def bonusRollSpaceCheck(currentTurn):
    if currentTurn == "Player 1":
        current = 0
        found = False
        while current < len(bonusRollSpaces) and found == False: #Running a linear search here.
            if bonusRollSpaces[current] == player1.currentSpace:
                found == True
                roll = 6
                print("Great! You landed on a bonus roll space!")
                input()
                bonusRoll(roll, currentTurn)
            current = current + 1
    elif currentTurn == "Player 2":
        current = 0
        found = False
        while current < len(bonusRollSpaces) and found == False: #Running a linear seach here.
            if bonusRollSpaces[current] == player2.currentSpace:
                found == True
                roll = 6
                print("Great! You landed on a bonus roll space!")
                input()
                bonusRoll(roll, currentTurn)
            current = current + 1

def bonusRoll(roll, currentTurn): #This is run each turn but only outputs anything if the number rolled is equal to 6.
    while roll == 6:
        print(currentTurn + str(" gets to roll the dice again!"))
        input()
        roll = random.randint(1,6)
        print(currentTurn + str(" rolled a ") + str(roll) + str("!"))
        if currentTurn == "Player 1":
            player1.moveForward(roll)
            ladderCheck(currentTurn)
            snakeCheck(currentTurn)
            bonusRollSpaceCheck(currentTurn)
            lionCheck(currentTurn)
        if currentTurn == "Player 2":
            player2.moveForward(roll)
            ladderCheck(currentTurn)
            snakeCheck(currentTurn)
            bonusRollSpaceCheck(currentTurn)
            lionCheck(currentTurn)

def bonusRollSpaceSort(bonusRollSpaces): #Using bubble sort to sort the bonus roll spaces list into ascending order.
    bonusRollSpacesLen = len(bonusRollSpaces)
    for x in range(bonusRollSpacesLen-1):
        for y in range(bonusRollSpacesLen-x-1):
            if bonusRollSpaces[y] > bonusRollSpaces[y+1]:
                bonusRollSpaces[y], bonusRollSpaces[y+1] = bonusRollSpaces[y+1], bonusRollSpaces[y]
    return bonusRollSpaces

def lionSort(lions): #Using bubble sort to sort the lion spaces list into ascending order.
    lionsLen = len(lions)
    for x in range(lionsLen-1):
        for y in range(lionsLen-x-1):
            if lions[y] > lions[y+1]:
                lions[y], lions[y+1] = lions[y+1], lions[y]
    return lions

def lionCheck(currentTurn):
    if currentTurn == "Player 1":
        current = 0
        found = False
        while current < len(lions) and found == False: #Running a linear search here.
            if lions[current] == player1.currentSpace:
                found == True
                player1.stunned = True
                roll = 0
                print("Yikes! You landed on a lion! You miss your next turn!")
                input()
                bonusRoll(roll, currentTurn)
            current = current + 1
    elif currentTurn == "Player 2":
        current = 0
        found = False
        while current < len(lions) and found == False: #Running a linear seach here.
            if lions[current] == player2.currentSpace:
                found == True
                player2.stunned = True
                roll = 0
                print("Yikes! You landed on a lion! You miss your next turn!")
                input()
                bonusRoll(roll, currentTurn)
            current = current + 1

def probe(space, availableSpaces, difference, spaceType, count): #The probing method which tries to space out the spaces between the ladder and snake spaces.
    count += 1
    thisCount = count % 2
    while difference < 5:
        if thisCount == 0:
            space += 1
        elif thisCount == 1:
            space -= 1
        difference += 1
    while space not in availableSpaces:
        if spaceType == "ladder":
            space = random.randint(1,89)
        if spaceType == "snake":
            space = random.randint(11,99)
            availableSpaces.remove(square)
            availableSpaces.remove(square - 10)
        else:
            space = random.randint(1,99)
            availableSpaces.remove(square)
    return square, count, availableSpaces


def checkArrays(array, availableSpaces, spaceType): #This checks to see if the ladder spaces, snake spaces, bonus roll spaces and lion spaces lists need probing and sees whether or not they can be probed or not.
    count = 0
    for num in range(0, len(array)):
        try:
            difference = array[num] - array[num-1]
            space = array[num]
            space, count, availableSpaces = probe(square, availableSpaces, difference, spaceType, count)
            array[num] = space
        except:
            "Cannot probe space!"
    return array, availableSpaces

def startGame(): #Initially deciding the player turn order.
    turnDecision = random.randint(1,2)
    if turnDecision == 1:
        turnOrder = [player1.name, player2.name]
    else:
        turnOrder = [player2.name, player1.name]
    print("\n" + turnOrder[0] + " gets to start first! \n")
    while True: #This is run and looped when the user starts the game.
        currentTurn = turnOrder[0]
        if currentTurn == "Player 1": #Checking if player is stunned.
            if player1.stunned == True:
                player1.stunned = False
                print(currentTurn, "is currently stunned and cannot move this turn!")
                input()
                turnOrder.append(currentTurn)
                turnOrder.remove(currentTurn)
                currentTurn = turnOrder[0]
        elif currentTurn == "Player 2": #Checking if player is stunned.
            if player2.stunned == True:
                player2.stunned = False
                print(currentTurn, "is currently stunned and cannot move this turn!")
                input()
                turnOrder.append(currentTurn)
                turnOrder.remove(currentTurn)
                currentTurn = turnOrder[0]
        print("Player 1's current space:", player1.currentSpace, "\nPlayer 2's current space:", player2.currentSpace, "\nLadders:", ladders, "\nSnakes:", snakes, "\nBonus Roll Spaces:", bonusRollSpaces, "\nLions:", lions)
        print("\nIt is " + str(currentTurn) + str("'s turn to roll the dice!"))
        displayGameMenu()
        gameChoice = input()
        checkGameChoice(gameChoice)
        roll = random.randint(1,6)
        print(str("\n") + currentTurn + str(" rolled a ") + str(roll) + str("!"))
        if currentTurn == "Player 1":
            player1.moveForward(roll)
            ladderCheck(currentTurn)
            snakeCheck(currentTurn)
            bonusRollSpaceCheck(currentTurn)
            lionCheck(currentTurn)
            bonusRoll(roll, currentTurn)
        if currentTurn == "Player 2":
            player2.moveForward(roll)
            ladderCheck(currentTurn)
            snakeCheck(currentTurn)
            bonusRollSpaceCheck(currentTurn)
            lionCheck(currentTurn)
            bonusRoll(roll, currentTurn)
        turnOrder.append(currentTurn)
        turnOrder.remove(turnOrder[0])
        

#Main Program

player1 = Player("Player 1", 0, False) #Setting the initial player's name, current space and if they are stunned or not.
player2 = Player("Player 2", 0, False)
availableSpaces = []
ladders = []
snakes = []
bonusRollSpaces = []
lions = []

displayMenu()
choice = input()
checkChoice(choice)
displayDifficultyMenu()
choice = input()
difficultyChoice = checkDifficultyChoice(choice)

if difficultyChoice == "1":
    numOfLadders = 7
    numOfSnakes = 3
    numOfBonusRollSpaces = 7
    numOfLions = 3
elif difficultyChoice == "2":
    numOfLadders = 5
    numOfSnakes = 5
    numOfBonusRollSpaces = 5
    numOfLions = 5
elif difficultyChoice == "3":
    numOfLadders = 3
    numOfSnakes = 7
    numOfBonusRollSpaces = 3
    numOfLions = 7
else:
    numOfLadders = input("Enter the number of ladders: ")
    numOfSnakes = input("Enter the number of snakes: ")
    numOfBonusRollSpaces = input("Enter the number of bonus roll spaces: ")
    numOfLions = input("Enter the number of lions: ")
    numOfLadders, numOfSnakes, numOfBonusRollSpaces, numOfLions = checkCustomDifficultyChoice(numOfLadders, numOfSnakes, numOfBonusRollSpaces, numOfLions)

for generateSpaces in range(1,101): #This generates the number of spaces on the board.
    availableSpaces.append(generateSpaces)

for ladderGeneration in range(numOfLadders): #This randomises and selects the ladder space numbers and places them onto the board.
    ladderSelect = random.randint(1,89)
    while True:
        try:
            availableSpaces.remove(ladderSelect)
            availableSpaces.remove(ladderSelect + 10)
            break
        except:
            ladderSelect = random.randint(1,89)
    ladders.append(ladderSelect)
for snakeGeneration in range(numOfSnakes): #This randomises and selects the snake space numbers and places them onto the board.
    snakeSelect = random.randint(11,99)
    while True:
        try:
            availableSpaces.remove(snakeSelect)
            availableSpaces.remove(snakeSelect - 10)
            break
        except:
            snakeSelect = random.randint(11,99)
    snakes.append(snakeSelect)
for bonusRollSpaceGeneration in range(numOfBonusRollSpaces): #This randomises and selects the bonus roll space numbers and places them onto the board.
    bonusRollSpaceSelect = random.randint(1,99)
    while True:
        try:
            availableSpaces.remove(bonusRollSpaceSelect)
            break
        except:
            bonusRollSpaceSelect = random.randint(1,99)
    bonusRollSpaces.append(bonusRollSpaceSelect)
for lionGeneration in range(numOfLions): #This randomises and selects the lion space numbers and places them onto the board.
    lionSelect = random.randint(1,99)
    while True:
        try:
            availableSpaces.remove(lionSelect)
            break
        except:
            lionSelect = random.randint(1,99)
    lions.append(lionSelect)

ladderProbeOutput = checkArrays(ladders, availableSpaces, "ladders")
snakeProbeOutput = checkArrays(snakes, availableSpaces, "snakes")
bonusRollSpaceProbeOutput = checkArrays(bonusRollSpaces, availableSpaces, "bonusRollSpaces")
lionProbeOutput = checkArrays(lions, availableSpaces, "lions")

ladders = ladderProbeOutput[0]
snakes = snakeProbeOutput[0]
bonusRollSpaces = bonusRollSpaceProbeOutput[0]
lions = lionProbeOutput[0]

ladders = ladderSort(ladders)
snakes = snakeSort(snakes)
bonusRollSpaces = bonusRollSpaceSort(bonusRollSpaces)
lions = lionSort(lions)

startGame()
