import pygame
from pygame.locals import *

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
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
                    squares.append(square)
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
        self.location = location
        self.rect = self.surf.get_rect(center=(location))
        self.colour = colour

    def get_possibleMoves(self, piecePos, possibleMoves, moveNum1, moveNum2, capturing):
        pieceX = round(((piecePos[0] - 200) / 100) - 1)
        pieceY = round(((piecePos[1] - 100) / 100) - 1)
        if self.colour == "Black":
            if capturing:
                possibleMoves[pieceX-1][pieceY-1] = True
            elif moveNum2 == 1:
                possibleMoves[pieceX][pieceY-1] = True
                possibleMoves[pieceX][pieceY-2] = True
            else:
                possibleMoves[pieceX][pieceY-1] = True
        elif self.colour == "White":
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
        if self.colour == "White":
            if not capturing:
                if -50 < X < 50 and 150 > Y > 50:
                    moveValid = True
                else:
                    moveValid = False
            else:
                if -150 < X < 150 and 50 < Y < 150:
                    moveValid = True
                else:
                    moveValid = False
        elif self.colour == "Black":
            if not capturing:
                if -50 < X < 50 and -150 < Y < -50:
                    moveValid = True
                else:
                    moveValid = False
            else:
                if -150 < X < 150 and -50 > Y > -150:
                    moveValid = True
                else:
                    moveValid = False
        else:
            moveValid = False
        return moveValid
    
    def getCoords(self):
        return self.location

    def getColour(self):
        return self.colour

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

colour1 = BLACK
colour2 = WHITE

board = Board()

squares = []
pieces = pygame.sprite.Group()

piecesArray = []
for x in range(0, board.width):
    piecesRow = []
    for y in range(0, board.length):
        piecesRow.append(None)
    piecesArray.append(piecesRow)

piecesArray[3][0] = "wP"
piecesArray[3][7] = "bP"

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
        squares.append(square)

pieces = draw(piecesArray)

clicks = 0
moveNum1 = 1
moveNum2 = 1
playerTurn = "White"

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
            if clicks % 2 == 1:
                for piece in pieces:
                    coords = piece.getCoords()
                    mouseX = mouse[0]
                    mouseY = mouse[1]
                    coordsX = coords[0]
                    coordsY = coords[1]
                    pieceColour = piece.getColour() 
                    if pieceColour == playerTurn:
                        possibleMoves = piece.get_possibleMoves(coords, possibleMoves, moveNum1, moveNum2, False)
                        squares = board.highlightMoves(possibleMoves, squares)
            else:
                last = len(squares) - 1
                squares.remove(squares[last])
                if moveNum1 == 1 or moveNum2 == 1:
                    last = len(squares) - 1
                    squares.remove(squares[last])
                for piece in pieces:
                    coords = piece.getCoords()
                    mouseX = mouse[0]
                    mouseY = mouse[1]
                    coordsX = coords[0]
                    coordsY = coords[1]
                    pieceType = piece.get_type()
                    pieceColour = piece.getColour()  
                    if piece.checkMove(coords, mouse, False) and pieceColour == playerTurn:
                        prevPieceX = round(((coordsX - 200) / 100) - 1)
                        prevPieceY = round(((coordsY - 100) / 100) - 1)
                        piece.kill()
                        piecesArray[prevPieceX][prevPieceY] = None
                        pieceX = round(((mouseX - 200) / 100) - 1)
                        pieceY = round(((mouseY - 100) / 100) - 1)
                        newPiece = piecesDict[str(pieceType)+" "+str(pieceColour)]
                        piecesArray[pieceX][pieceY] = newPiece
                        pieces = draw(piecesArray)
                        if pieceColour == "White":
                            moveNum1 += 1
                        elif pieceColour == "Black":
                            moveNum2 += 1
                    else:
                        print("It isn't your turn!")
                if playerTurn == "White":
                    playerTurn = "Black"
                else:
                    playerTurn = "White"

    win.fill((0,255,0))
    
    mouse = pygame.mouse.get_pos()

    possibleMoves = origPossibleMoves
    
    for square in squares:
        win.blit(square.surf, square.rect)
    for piece in pieces:
        win.blit(piece.surf, piece.rect)
    pygame.display.update()

if not run:
    pygame.quit()
