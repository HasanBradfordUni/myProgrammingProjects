import pygame
from pygame.locals import *

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)

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

    def move(self, moveFrom, moveWhere):
        X = moveWhere[0] - moveFrom[0]
        Y = moveWhere[1] - moveFrom[1]
        self.rect.move_ip(X, Y)

class Pawn(Piece):
    def __init__(self, pieceType, image_file, location):
        super().__init__(pieceType)
        self.surf = pygame.Surface((75, 75))
        self.surf = pygame.image.load(image_file).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(location))

    def checkMove(moveFrom, moveWhere, capturing):
        X = moveWhere[0] - moveFrom[0]
        Y = moveWhere[1] - moveFrom[1]
        if not capturing:
            if X < 100 and 150 > Y > 0:
                moveValid = True
            else:
                moveValid = False
        else:
            if 50 < X < 150 and 50 < Y < 150:
                moveValid = True
            else:
                moveValid = False
        return moveValid

    def getCoords(self):
        return self.location

pygame.init()

win = pygame.display.set_mode((1300, 1000), pygame.RESIZABLE)
pygame.display.set_caption("Chest Chess")

colour1 = BLACK
colour2 = WHITE

board = Board()
w_pawn = Pawn("Pawn", "w_pawn.png", [600, 200])
b_pawn = Pawn("Pawn", "b_pawn.png", [600, 900])

squares = pygame.sprite.Group()
pieces = pygame.sprite.Group()
origSquares = pygame.sprite.Group()

pieces.add(w_pawn)
pieces.add(b_pawn)

pawnMoves = []
for x in range(0, board.width):
    movesRow = []
    for y in range(0, board.length):
        movesRow.append(False)
    pawnMoves.append(movesRow)
        
pawnMoves[3][6] = True
pawnMoves[3][5] = True

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

clicks = 0

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            if clicks % 2 == 0:
                squares = origSquares
            else:
                squares = board.highlightMoves(possibleMoves, squares)

    win.fill((0,255,0))
    
    mouse = pygame.mouse.get_pos()

    possibleMoves = pawnMoves
    
    for square in squares:
        win.blit(square.surf, square.rect)
    for piece in pieces:
        win.blit(piece.surf, piece.rect)
    pygame.display.update()

if not run:
    pygame.quit()
