#Football chess
from random import *
from time import sleep

class Board():
    def __init__(self, array, width, length):
        self.__array = array
        self.__width = width
        self.__length = length

    def set_array(self, array):
        self.__array = array

    def draw(self):
        colLabels = []
        rowLabels = []
        for x in range(0, self.__width+1):
            for y in range(0, self.__length+1):
                if x == 0 and y == 0:
                    print(" ")
                if x == 0 and 0 <= y <= 8:
                    if y == 0:
                        print(" ", end= " |  ")
                    else:
                        rowLabel = y
                        rowLabels.append(rowLabel)
                        print(rowLabel, end="  |  ")
                if y == 0 and x != 0:
                    colLabel = chr((x+96))
                    colLabels.append(colLabel)
                    print(colLabel, end=" | ")
                if x != 0 and y != 0:
                    piece = self.__array[x-1][y-1]
                    if piece == None:
                        piece = "   "
                    if (x,y) == (1,4) or (x,y) == (1,5):
                        print(":"+piece+":", end=" | ")
                    elif (x,y) == (8,4) or (x,y) == (8,5):
                        print(";"+piece+";", end=" | ")
                    else:
                        print(piece, end=" | ")
            print()
        print()
        return colLabels, rowLabels

    def get_array(self):
        return self.__array

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

class Player():
    def __init__(self, playerNum, score, playerTurn):
        self.__playerNum = playerNum
        self.__score = score
        self.__playerTurn = playerTurn

    def get_move(self):
        gameOver = False
        moveFrom = input("Enter the coordinates of the piece you want to move - enter 'g0' to exit: ")
        moveTo = input("Enter the coordinates of where you want to move to: ")
        if moveFrom == "g0":
            gameOver = True
        return moveFrom, moveTo, gameOver

    def check_move(self, moveFrom, moveTo, colLabels, rowLabels):
        moveValid = True
        if len(moveFrom) != 2 or len(moveTo) != 2:
            moveValid = False
        try:
            rowFrom = int(moveFrom[1])
        except:
            print("Invalid input")
            rowFrom = 0
        try:
            rowTo = int(moveTo[1])
        except:
            print("Invalid input")
            rowTo = 0
        if (moveFrom[0] not in colLabels) or (rowFrom not in rowLabels) or (moveTo[0] not in colLabels) or (rowTo not in rowLabels):
            moveValid = False
        return moveValid

    def set_score(self, score):
        self.__score = score

    def set_playerTurn(self, playerTurn):
        self.__playerTurn = playerTurn

    def get_score(self):
        return self.__score

    def get_playerNum(self):
        return self.__playerNum

    def get_playerTurn(self):
        return self.__playerTurn

def initialisePieces(width, length):
    piecesArray = []
    for x in range(0, width):
        piecesRow = []
        for y in range(0, length):
            piecesRow.append(None)
        piecesArray.append(piecesRow)
    piecesArray[0][0] = "cdm"
    piecesArray[0][1] = "rb"
    piecesArray[0][2] = "cb"
    piecesArray[0][3] = "gk"
    piecesArray[0][5] = "cb"
    piecesArray[0][6] = "lb"
    piecesArray[0][7] = "cm"
    piecesArray[1][2] = "lw"
    piecesArray[1][3] = "cam"
    piecesArray[1][4] = "st"
    piecesArray[1][5] = "rw"
    piecesArray[6][2] = "LW"
    piecesArray[6][3] = "ST"
    piecesArray[6][4] = "CAM"
    piecesArray[6][5] = "RW"
    piecesArray[7][0] = "CDM"
    piecesArray[7][1] = "RB"
    piecesArray[7][2] = "CB"
    piecesArray[7][4] = "GK"
    piecesArray[7][5] = "CB"
    piecesArray[7][6] = "LB"
    piecesArray[7][7] = "CM"
    return piecesArray

def menu():
    print("1. New Game")
    print("2. How to play")
    print("3. About this game")
    print("4. Quit\n")
    return [1, 2, 3, 4]

def get_choice():
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Choice not valid - please enter again!")
        choice = get_choice()
    return choice

def check_choice(choice, options):
    choiceValid = False
    if choice in options:
        choiceValid = True
    else:
        choiceValid = False
        print("Choice not valid - please enter again!")
        choice = get_choice()
    return choiceValid, choice

def view_valid_moves():
    file = open("ValidMoves.txt", 'r')
    for line in file:
        print(line)

def check_move_valid(piece, player1Turn, player2Turn):
    moveValid = False
    if player1Turn and piece.lower() == piece:
        moveValid = True
    elif player2Turn and piece.upper() == piece:
        moveValid = True
    else:
        moveValid = False
    return moveValid

def getPiece(moveFrom, array):
    moveFromX = ord(moveFrom[0]) - 97
    moveFromY = int(moveFrom[1]) - 1
    piece = array[moveFromX][moveFromY]
    return piece

def CDM_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))
    
    possibleMoves.append((0,1))
    possibleMoves.append((0,-1))
    possibleMoves.append((0,2))
    possibleMoves.append((0,-2))
    
    for x in range(size):
        if player2Turn:
            possibleMoves.append((x,0))
        elif player1Turn:
            possibleMoves.append((-x,0))
            
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                elif player1Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def RB_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))

    if player2Turn:
        possibleMoves.append((-1,1))
    elif player1Turn:        
        possibleMoves.append((1,1))
    
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                elif player1Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def CB_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))

    if player2Turn:
        possibleMoves.append((-1,0))
    elif player1Turn:        
        possibleMoves.append((1,0))

    for x in range(size):
        if player2Turn:
            possibleMoves.append((x,0))
        elif player1Turn:
            possibleMoves.append((-x,0))
            
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                elif player1Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def LW_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))

    if player2Turn:
        possibleMoves.append((1,1))
        possibleMoves.append((1,-1))
    elif player1Turn:        
        possibleMoves.append((-1,1))
        possibleMoves.append((-1,-1))
    
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                elif player1Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def ST_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))

    for x in range(size):
        possibleMoves.append((x,0))
        possibleMoves.append((-x,0))
        
    for y in range(size):
        possibleMoves.append((0,y))
        possibleMoves.append((0,-y))
        
    for x in range(size):
        for y in range(size):
            if x == y:
                possibleMoves.append((-x,-y))
                possibleMoves.append((-x,y))
                possibleMoves.append((x,-y))
                possibleMoves.append((x,y))
                
    if moveDif in possibleMoves:
        return True
    else:
        return False

def GK_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))
    print(moveDif)

    possibleMoves.append((1,0))
    possibleMoves.append((-1,0))
    possibleMoves.append((0,1))
    possibleMoves.append((0,-1))
    possibleMoves.append((-1,-1))
    possibleMoves.append((-1,1))
    possibleMoves.append((1,-1))
    possibleMoves.append((1,1))
    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def CAM_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))
    
    possibleMoves.append((0,1))
    possibleMoves.append((0,-1))
    possibleMoves.append((0,2))
    possibleMoves.append((0,-2))
    
    for x in range(size):
        if player2Turn:
            possibleMoves.append((-x,0))
        elif player1Turn:
            possibleMoves.append((x,0))
            
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                elif player1Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def RW_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))

    if player2Turn:
        possibleMoves.append((1,1))
        possibleMoves.append((1,-1))
    elif player1Turn:        
        possibleMoves.append((-1,1))
        possibleMoves.append((-1,-1))
    
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                elif player1Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def LB_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))

    if player2Turn:
        possibleMoves.append((-1,-1))
    elif player1Turn:        
        possibleMoves.append((1,-1))
    
    for x in range(size):
        for y in range(size):
            if x == y:
                if player2Turn:
                    possibleMoves.append((x,-y))
                    possibleMoves.append((x,y))
                elif player1Turn:
                    possibleMoves.append((-x,-y))
                    possibleMoves.append((-x,y))
                    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def CM_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn):
    possibleMoves = []
    
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))
    print(moveDif)

    possibleMoves.append((1,0))
    possibleMoves.append((-1,0))
    possibleMoves.append((0,1))
    possibleMoves.append((0,-1))
    possibleMoves.append((-1,-1))
    possibleMoves.append((-1,1))
    possibleMoves.append((1,-1))
    possibleMoves.append((1,1))

    possibleMoves.append((2,0))
    possibleMoves.append((-2,0))
    possibleMoves.append((0,2))
    possibleMoves.append((0,-2))
    possibleMoves.append((-2,-2))
    possibleMoves.append((-2,2))
    possibleMoves.append((2,-2))
    possibleMoves.append((2,2))

    possibleMoves.append((3,0))
    possibleMoves.append((-3,0))
    possibleMoves.append((0,3))
    possibleMoves.append((0,-3))
    possibleMoves.append((-3,-3))
    possibleMoves.append((-3,3))
    possibleMoves.append((3,-3))
    possibleMoves.append((3,3))
    
    if moveDif in possibleMoves:
        return True
    else:
        return False

def move(moveFrom, moveTo, array, player1Turn, player2Turn):
    moveFromX = ord(moveFrom[0]) - 97
    moveFromY = int(moveFrom[1]) - 1
    moveToX = ord(moveTo[0]) - 97
    moveToY = int(moveTo[1]) - 1
    print(moveFromX, moveFromY)
    print(moveToX, moveToY)
    piece = array[moveFromX][moveFromY]
    piece2 = array[moveToX][moveToY]
    piece2 = piece2.upper()
    size = len(array)
    moveValid = False
    player1Capture = False
    player2Capture = False
    match piece.upper():
        case "CDM":
            print("\nCDM piece selected...")
            sleep(1)
            moveValid = CDM_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "RB":
            print("\nRB piece selected...")
            sleep(1)
            moveValid = RB_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "CB":
            print("\nCB piece selected...")
            sleep(1)
            moveValid = CB_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "LW":
            print("\nLW piece selected...")
            sleep(1)
            moveValid = LW_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "ST":
            print("\nST piece selected...")
            sleep(1)
            moveValid = ST_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "GK":
            print("\nGK piece selected...")
            sleep(1)
            moveValid = GK_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "CAM":
            print("\nCAM piece selected...")
            sleep(1)
            moveValid = CAM_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "RW":
            print("\nRW piece selected...")
            sleep(1)
            moveValid = RW_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "LB":
            print("\nLB piece selected...")
            sleep(1)
            moveValid = LB_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "CM":
            print("\nCM piece selected...")
            sleep(1)
            moveValid = CM_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
        case "CAP":
            print("\nCAP piece selected...")
            sleep(1)
            moveValid = CAP_moves(moveFromX, moveFromY, moveToX, moveToY, size, player1Turn, player2Turn)
    if moveValid:
        array[moveFromX][moveFromY] = None
        array[moveToX][moveToY] = piece
        if piece2 != None:
            if player1Turn:
                player1Capture = True
            elif player2Turn:
                player2Capture = True
    else:
        print("\nThat move is not valid (piece specific)!\n")
    return array, moveValid, player1Capture, player2Capture, piece2

def getScores(piecesArray):
    scoresDict = {}
    nums = [3,2,1,7,2,4,3,5,6,3]
    num = 0
    for row in piecesArray:
        for piece in range(0, len(row)):
            try:
                pieceLetter = row[piece].upper()
                scoresKeys = scoresDict.keys()
                if pieceLetter not in scoresKeys:
                    scoresDict[pieceLetter] = nums[num]
                    num += 1
            except:
                "No piece exists in that square"
    return scoresDict

def new_game():
    width = 8
    length = 8
    piecesArray = initialisePieces(width, length)
    scorePerPieceCapture = getScores(piecesArray)
    array = setup_array(width, length)
    board = Board(array, width, length)
    array = setup_pieces(array, piecesArray)
    board.set_array(array)
    colLabels, rowLabels = board.draw()
    turnNum = randint(1, 2)
    player1Turn = False
    player2Turn = False
    if turnNum == 1:
        player1Turn = True
    else:
        player2Turn = True
    player1 = Player(1, 0, player1Turn)
    player2 = Player(2, 0, player2Turn)
    player1Turn = player1.get_playerTurn()
    player2Turn = player2.get_playerTurn()
    gameOver = False
    while not gameOver:
        if player1Turn:
            print("\nPlayer 1 turn!\n")
            moveFrom, moveTo, gameOver = player1.get_move()
            if not gameOver:
                moveValid = player1.check_move(moveFrom, moveTo, colLabels, rowLabels)
                while not moveValid:
                    print("\nThat is not a valid move!")
                    print("Please try again... \n")
                    moveFrom, moveTo, gameOver = player1.get_move()
                    moveValid = player1.check_move(moveFrom, moveTo, colLabels, rowLabels)
                else:
                    piece = getPiece(moveFrom, array)
                    moveValid1 = check_move_valid(piece, player1Turn, player2Turn)
                    while not moveValid1:
                        print("\nThat is not your piece!")
                        print("Please try again... \n")
                        moveFrom, moveTo, gameOver = player1.get_move()
                        piece = getPiece(moveFrom, array)
                        moveValid = player1.check_move(moveFrom, moveTo, colLabels, rowLabels)
                        moveValid1 = check_move_valid(piece, player1Turn, player2Turn)
                    else:
                        array, moveValid2, player1Capture, player2Capture, piece2 = move(moveFrom, moveTo, array, player1Turn, player2Turn)
                        while not moveValid2:
                            moveFrom, moveTo, gameOver = player1.get_move()
                            piece = getPiece(moveFrom, array)
                            moveValid = player1.check_move(moveFrom, moveTo, colLabels, rowLabels)
                            moveValid1 = check_move_valid(piece, player1Turn, player2Turn)
                            array, moveValid2, player1Capture, player2Capture, piece2 = move(moveFrom, moveTo, array, player1Turn, player2Turn)
                        else:
                            board.set_array(array)
                            colLabels, rowLabels = board.draw()
                            player1Score = player1.get_score()
                            if player1Capture:
                                player1.set_score(player1Score+scorePerPieceCapture[piece2])
                            player1Score = player1.get_score()
                            print("Player 1 - Your score is now:",player1Score)
            else:
                print("\nYou decided to quit the game...")
                quit()
            player1.set_playerTurn(False)
            player2.set_playerTurn(True)
            player1Turn = player1.get_playerTurn()
            player2Turn = player2.get_playerTurn()
        else:
            print("\nPlayer 2 turn!\n")
            moveFrom, moveTo, gameOver = player2.get_move()
            if not gameOver:
                moveValid = player2.check_move(moveFrom, moveTo, colLabels, rowLabels)
                while not moveValid:
                    print("\nThat is not a valid move!")
                    print("Please try again... \n")
                    moveFrom, moveTo, gameOver = player2.get_move()
                    moveValid = player2.check_move(moveFrom, moveTo, colLabels, rowLabels)
                else:
                    piece = getPiece(moveFrom, array)
                    moveValid1 = check_move_valid(piece, player1Turn, player2Turn)
                    while not moveValid1:
                        print("\nThat is not your piece!")
                        print("Please try again... \n")
                        moveFrom, moveTo, gameOver = player1.get_move()
                        piece = getPiece(moveFrom, array)
                        moveValid = player2.check_move(moveFrom, moveTo, colLabels, rowLabels)
                        moveValid1 = check_move_valid(piece, player1Turn, player2Turn)
                    else:
                        array, moveValid2, player1Capture, player2Capture, piece2 = move(moveFrom, moveTo, array, player1Turn, player2Turn)
                        while not moveValid2:
                            moveFrom, moveTo, gameOver = player1.get_move()
                            piece = getPiece(moveFrom, array)
                            moveValid = player2.check_move(moveFrom, moveTo, colLabels, rowLabels)
                            moveValid1 = check_move_valid(piece, player1Turn, player2Turn)
                            array, moveValid2, player1Capture, player2Capture, piece2 = move(moveFrom, moveTo, array, player1Turn, player2Turn)
                        else:
                            board.set_array(array)
                            colLabels, rowLabels = board.draw()
                            player2Score = player2.get_score()
                            if player2Capture:
                                player2.set_score(player2Score+scorePerPieceCapture[piece2])
                            player2Score = player2.get_score()
                            print("Player 2 - Your score is now:",player2Score)
            else:
                print("\nYou decided to quit the game...")
                quit()
            player2.set_playerTurn(False)
            player1.set_playerTurn(True)
            player1Turn = player1.get_playerTurn()
            player2Turn = player2.get_playerTurn()
    
def how_to_play():
    print("\nA prompt will be shown on screen (a user input)")
    print("The user will enter the coordinates of the piece thay want to move")
    print("The user will then enter the coordinates of where to move to")
    print("The piece will then move if it is a valid move")
    print("Points are gain for captures and also if your goalkeeper is in the goal")
    print("The game will end when either player's goalkeeper gets captured")
    print("Valid moves are provided below: \n")
    view_valid_moves()
    main()

def about_game():
    print("\nThis game is a spin off of chess")
    print("It is football themed and the pieces are players in a starting 11")
    print("Each piece is noted by their position letter\n")
    main()

def setup_array(width, length):
    array = []
    for x in range(0, width):
        row = []
        for y in range(0, length):
            row.append(None)
        array.append(row)
    return array

def setup_pieces(array, piecesArray):
    for x in range(0, len(array)):
        for y in range(0, len(array)):
            if piecesArray[x][y] != None:
                array[x][y] = piecesArray[x][y]
    return array
    
def main():
    options = menu()
    choice = get_choice()
    choiceValid, choice = check_choice(choice, options)
    if choiceValid:
        match choice:
            case 1:
                new_game()
            case 2:
                how_to_play()
            case 3:
                about_game()
            case _:
                quit()

if __name__ == "__main__":
    main()
