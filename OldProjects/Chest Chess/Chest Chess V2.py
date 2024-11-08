import pygame

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)

class Board(object):
    def __init__(self):
        self.width = 8
        self.length = 8

    def draw(self):
        pass

class Square(pygame.sprite.Sprite):
    def __init__(self, colour, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(colour)
        self.rect = self.surf.get_rect(center=(location))

pygame.init()

win = pygame.display.set_mode((1300, 1000), pygame.RESIZABLE)
pygame.display.set_caption("Chest Chess")

colour1 = BLACK
colour2 = WHITE

board = Board()

squares = pygame.sprite.Group()

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

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((0,255,0))
    
    for square in squares:
        win.blit(square.surf, square.rect)
    pygame.display.update()

if not run:
    pygame.quit()
