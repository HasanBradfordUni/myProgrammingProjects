#Pygame buttons
import pygame
import sys

class Button(pygame.sprite.Sprite):
    def __init__(self,color,locX,locY):
        super(Button, self).__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=(locX,locY,))

    def rotate(self):
        pygame.transform.rotate(self.surf, 90)

        
# initializing the constructor
pygame.init()
  
# screen resolution
res = (720,720)
  
# opens up a window
screen = pygame.display.set_mode(res)
  
# white color
color = (255,255,255)
  
# colors of the button
color_light = (170,170,170)
color_dark = (100,100,100)
color_red = (255,0,0)
color_blue = (0,0,255)
color_green = (0,255,0)
color_magenta = (255,0,255)
color_yellow = (255,255,0)
color_cyan = (0,255,255)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',25)
largefont = pygame.font.SysFont('Algerian',30,bold=True)
  
# rendering a text written in
# this font
text = smallfont.render('quit' , True , color)
text1 = largefont.render('Click this', True, color)

#Setting up button sprite
button1 = Button(color_green,500,500)

while True:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
            elif 50 <= mouse[0] <= 150 and 100 <= mouse[1] <= 200:
                button1.rotate()
                pygame.display.update()
                
                  
    # fills the screen with a color
    screen.fill((60,25,60))
      
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
    elif 50 <= mouse[0] <= 150 and 100 <= mouse[1] <= 200:
        pygame.draw.rect(screen,color_red,[50,100,100,100])
        screen.blit(button1.surf, button1.rect)
        pygame.display.update()
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
        pygame.draw.rect(screen,color_blue,[50,100,100,100])
      
    # superimposing the text onto our button
    screen.blit(text , (width/2+50,height/2))
    screen.blit(text1, (75,150))
      
    # updates the frames of the game
    pygame.display.update()
