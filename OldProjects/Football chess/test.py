for num in range(1, 1-3, -1):
    print(num)

def checkMovePath(array, moveFromX, moveFromY, moveToX, moveToY):
    pathClear = True
    moveDif = ((moveToX - moveFromX),(moveToY - moveFromY))
    print(moveDif)
    stepX = 1
    stepY = 1
    print(moveDif[0])
    print(moveDif[1])
    if moveDif[0] < 0 and moveDif[1] >= 0:
        stepY = -1
    elif moveDif[1] < 0 and moveDif[0] >= 0:
        stepX = -1
    elif moveDif[0] < 0 and moveDif[1] < 0:
        stepX = -1
        stepY = -1
    else:
        stepX = 1
        stepY = 1
    print(stepX)
    print(stepY)
    if moveDif[0] == 0:
        for x in range(moveFromX+1, moveFromX+moveDif[1], stepX):
            print(moveFromX, moveFromY+x-2, array[moveFromX][moveFromY+x-2], sep=",")
            if array[moveFromX][moveFromY+x-2] != None:
                pathClear = False
                break
    elif moveDif[1] == 0:
        for y in range(moveFromY+1, moveFromY+moveDif[0], stepY):
            print(moveFromX+y-4, moveFromY, array[moveFromX+y-4][moveFromY], sep=",")
            if array[moveFromX+y-4][moveFromY] != None:
                pathClear = False
                break
    else:
        for x in range(moveFromX+1, moveFromX+moveDif[1]+1, stepX):
            for y in range(moveFromY+1, moveFromY+moveDif[0]+1, stepY):
                print(y-1, x-1, array[y-1][x-1], sep=",")
                if x == y:
                    if array[y-1][x-1] != None:
                        pathClear = False
                        break
    return pathClear

def move(moveFrom, moveTo, array, player1Turn, player2Turn):
    moveFromX = ord(moveFrom[0]) - 97
    moveFromY = int(moveFrom[1]) - 1
    print(moveFromX, moveFromY)
    moveToX = ord(moveTo[0]) - 97
    moveToY = int(moveTo[1]) - 1
    print(moveToX, moveToY)
    piece = array[moveFromX][moveFromY]
    print(piece)
    pathClear = checkMovePath(array, moveFromX, moveFromY, moveToX, moveToY)
    print(pathClear)

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

array = initialisePieces(8,8)
moveFrom = input("Enter the coordinates of the piece you want to move - enter 'g0' to exit: ")
moveTo = input("Enter the coordinates of where you want to move to: ")
move(moveFrom,moveTo,array,True,False)
while moveFrom != "g0":
    moveFrom = input("Enter the coordinates of the piece you want to move - enter 'g0' to exit: ")
    moveTo = input("Enter the coordinates of where you want to move to: ")
    move(moveFrom,moveTo,array,True,False)

