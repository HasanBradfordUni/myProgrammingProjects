import pygame

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
background_color = WHITE
(width, height) = (200, 300)

running = True

def main():
    global running, screen
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TUFF")
    screen.fill(background_color)
    pygame.display.update()
    
    while running:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                draw_circle()
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

def get_pos():
    pos = pygame.mouse.get_pos()
    return (pos)

def draw_circle():
    pos=get_pos()
    pygame.draw.circle(screen, BLUE, pos, 20)


if __name__ == '__main__':
    main()
