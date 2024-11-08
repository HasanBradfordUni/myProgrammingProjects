import pygame
from pygame.locals import *

LIGHT = (53, 53, 53)
DARK = (220, 189, 194)
piecesDict = {"Pawn Black":"bP","Pawn White":"wP"}

class Board(object):
    def __init__(self):
        self.width = 8
        self.length = 8

    def highlightMoves(self, possibleMoves, squares):
        colour = (255,255,0)
        for x in range(0, len(possibleMoves)):
            for y in range(0, len(possibleMoves)):
                if possibleMoves[x][y]:                    
                    X = ((x+1)*100) + 200
                    Y = ((y+1)*100) + 100
                    square = Square(colour, (X, Y))
                    squares.add(square)
        return squares
        
class Square(pygame.sprite.Sprite):
    def __init__(self, colour, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(colour)
        self.location = location
        self.rect = self.surf.get_rect(center=(location))

    def getCoords(self):
        return self.location

class Piece(pygame.sprite.Sprite):
    def __init__(self, pieceType):
        pygame.sprite.Sprite.__init__(self)
        self._type = pieceType

    def get_type(self):
        return self._type

class Pawn(Piece):
    def __init__(self, pieceType, image_file, location, colour):
        super().__init__(pieceType)
        self.surf = pygame.Surface((75, 75))
        self.surf = pygame.image.load(image_file).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.__location = location
        self.rect = self.surf.get_rect(center=(location))
        self.__colour = colour

    def get_possibleMoves(self, piecePos, possibleMoves, moveNum1, moveNum2, capturing):
        pieceX = round(((piecePos[0] - 200) / 100) - 1)
        pieceY = round(((piecePos[1] - 100) / 100) - 1)
        possibleMoves[pieceX][pieceY] = False
        if self.__colour == "Black":
            if capturing:
                possibleMoves[pieceX-1][pieceY-1] = True
            elif moveNum2 == 1:
                possibleMoves[pieceX][pieceY-1] = True
                possibleMoves[pieceX][pieceY-2] = True
            else:
                possibleMoves[pieceX][pieceY-1] = True
        elif self.__colour == "White":
            if capturing:
                possibleMoves[pieceX+1][pieceY+1] = True
            elif moveNum1 == 1:
                possibleMoves[pieceX][pieceY+1] = True
                possibleMoves[pieceX][pieceY+2] = True
            else:
                possibleMoves[pieceX][pieceY+1] = True
        return possibleMoves

    def checkMove(self, moveFrom, moveWhere, capturing):
        X = moveWhere[0] - moveFrom[0]
        Y = moveWhere[1] - moveFrom[1]
        if self.__colour == "White":
            if not capturing:
                if -50 < X < 50 and 150 > Y > 50:
                    moveValid = True
                    captured = False     
                else:
                    moveValid = False
                    captured = False
            else:
                if -150 < X < 150 and 50 < Y < 150:
                    moveValid = True
                    captured = True
                else:
                    moveValid = False
                    captured = False
        elif self.__colour == "Black":
            if not capturing:
                if -50 < X < 50 and -150 < Y < -50:
                    moveValid = True
                    captured = False
                else:
                    moveValid = False
                    captured = False
            else:
                if -150 < X < 150 and -50 > Y > -150:
                    moveValid = True
                    captured = True
                else:
                    moveValid = False
                    captured = False
        else:
            moveValid = False
            captured = False
        return moveValid, captured

    def checkCapturing(self, piecePos, piecesArray):
        pieceX = round(((piecePos[0] - 200) / 100) - 1)
        pieceY = round(((piecePos[1] - 100) / 100) - 1)
        if self.__colour == "White":
            leftCapture = piecesArray[pieceX-1][pieceY+1]
            rightCapture = piecesArray[pieceX+1][pieceY+1]
        elif self.__colour == "Black":
            leftCapture = piecesArray[pieceX-1][pieceY-1]
            rightCapture = piecesArray[pieceX+1][pieceY-1]
        else:
            leftCapture = None
            rightCapture = None
        if leftCapture != None or rightCapture != None:
            capturing = True
        else:
            capturing = False
        return capturing
    
    def getCoords(self):
        return self.__location

    def getColour(self):
        return self.__colour

def draw(piecesArray):
    for x in range(0, board.width):
        for y in range(0, board.length):
            X = ((x+1)*100) + 200
            Y = ((y+1)*100) + 100
            if piecesArray[x][y] == "bP":
                b_pawn = Pawn("Pawn", "b_pawn.png", [X, Y], "Black")
                pieces.add(b_pawn)
            elif piecesArray[x][y] == "wP":
                w_pawn = Pawn("Pawn", "w_pawn.png", [X, Y], "White")
                pieces.add(w_pawn)
    return pieces

pygame.init()

win = pygame.display.set_mode((1300, 1000), pygame.RESIZABLE)
pygame.display.set_caption("Chest Chess")

colour1 = DARK
colour2 = LIGHT

board = Board()

squares = pygame.sprite.Group()
pieces = pygame.sprite.Group()
origSquares = pygame.sprite.Group()

piecesArray = []
for x in range(0, board.width):
    piecesRow = []
    for y in range(0, board.length):
        piecesRow.append(None)
    piecesArray.append(piecesRow)

piecesArray[3][0] = "wP"
piecesArray[3][7] = "bP"
piecesArray[4][0] = "wP"
piecesArray[4][7] = "bP"

for x in range(0, board.width):
    for y in range(0, board.length):
        if x % 2 == 0 and y % 2 == 0:
            colour = colour1
        elif x % 2 == 1 and y % 2 == 1:
            colour = colour1
        else:
            colour = colour2
        X = ((x+1)*100) + 200
        Y = ((y+1)*100) + 100
        square = Square(colour, (X, Y))
        squares.add(square)
        origSquares.add(square)

pieces = draw(piecesArray)

clicks = 0
moveNum1 = 1
moveNum2 = 1
playerTurn = "White"
turnValid = False

possibleMoves = []
origPossibleMoves = []
for x in range(0, board.width):
    possibleMovesRow = []
    origPossibleMovesRow = []
    for y in range(0, board.length):
        possibleMovesRow.append(False)
        origPossibleMovesRow.append(False)
    possibleMoves.append(possibleMovesRow)
    origPossibleMoves.append(origPossibleMovesRow)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            if clicks % 2 == 0:
                #possibleMoves = origPossibleMoves
                #squares = origSquares
                for piece in pieces:
                    coords = piece.getCoords()
                    mouseX = mouse[0]
                    mouseY = mouse[1]
                    coordsX = coords[0]
                    coordsY = coords[1]
                    pieceType = piece.get_type()
                    pieceColour = piece.getColour()
                    capturing = piece.checkCapturing(coords, piecesArray)
                    moveValid, captured = piece.checkMove(coords, mouse, capturing)
                    if moveValid and pieceColour == playerTurn:
                        turnValid = True
                        prevPieceX = round(((coordsX - 200) / 100) - 1)
                        prevPieceY = round(((coordsY - 100) / 100) - 1)
                        piece.kill()
                        piecesArray[prevPieceX][prevPieceY] = None
                        pieceX = round(((mouseX - 200) / 100) - 1)
                        pieceY = round(((mouseY - 100) / 100) - 1)
                        newPiece = piecesDict[str(pieceType)+" "+str(pieceColour)]
                        piecesArray[pieceX][pieceY] = newPiece
                        pieces = draw(piecesArray)
                        if captured:
                            piecesArray[pieceX][pieceY] = None
                        if pieceColour == "White":
                            moveNum1 += 1
                        elif pieceColour == "Black":
                            moveNum2 += 1
                    else:
                        turnValid = False
                if playerTurn == "White":
                    playerTurn = "Black"
                else:
                    playerTurn = "White"
            else:
                possibleMoves = origPossibleMoves
                squares = origSquares
                for piece in pieces:
                    coords = piece.getCoords()
                    mouseX = mouse[0]
                    mouseY = mouse[1]
                    coordsX = coords[0]
                    coordsY = coords[1]
                    #if (coordsX - 50) < mouseX < (coordsX + 50) and (coordsY - 50) < mouseY < (coordsY + 50):
                        #possibleMoves = piece.get_possibleMoves(coords, possibleMoves, moveNum1, moveNum2, False)
                #squares = board.highlightMoves(possibleMoves, squares)

    win.fill((0,255,0))
    
    mouse = pygame.mouse.get_pos()
    
    for square in squares:
        win.blit(square.surf, square.rect)
    for piece in pieces:
        win.blit(piece.surf, piece.rect)
    pygame.display.update()

if not run:
    pygame.quit()
