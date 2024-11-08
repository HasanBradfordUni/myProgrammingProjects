#shapes drawer
import pygame
from time import sleep

class Shape(object):
    def __init__(self, lineColour, fillColour):
        self._lineColour = lineColour
        self._fillColour = fillColour
        self._type = "None"

    def setLineColour(self, colour):
        self._lineColour = colour

    def setLineColour(self, colour):
        self._lineColour = colour

class Rectangle(Shape):
    def __init__(self, length, width, lineColour, fillColour, win):
        super().__init__(lineColour, fillColour)
        if fillColour == "red":
            self._fillColour = (255,0,0)
        if fillColour == "green":
            self._fillColour = (0,255,0)
        if fillColour == "blue":
            self._fillColour = (0,0,255)
        self.__length = length
        self.__width = width
        self.surf = win
        self.rect = pygame.Rect((75, 75, self.__length, self.__width))

    def draw(self):
        pygame.draw.rect(self.surf, self._fillColour, self.rect)

    def getTopLeft(self):
        return self.rect.topleft

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

class Circle(Shape):
    def __init__(self, radius, centre, lineColour, fillColour, win):
        super().__init__(lineColour, fillColour)
        if fillColour == "red":
            self._fillColour = (255,0,0)
        if fillColour == "green":
            self._fillColour = (0,255,0)
        if fillColour == "blue":
            self._fillColour = (0,0,255)
        self.__radius = radius
        self.__centre = centre
        self.surf = win

    def draw(self):
        pygame.draw.circle(self.surf, self._fillColour, self.__centre, self.__radius)

    def getCentre(self):
        return self.__centre

    def getRadius(self):
        return self.__radius

if __name__ == "__main__":
    pygame.init()

    win = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Shapes drawer")

    win.fill((255,255,255))
    
    shape1 = Shape("black", "red")
    rectangle = Rectangle(12, 7, "black", "red", win)
    print(rectangle.getTopLeft())
    circle = Circle(15, [50, 50], "black", "blue", win)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        rectangle.draw()
        pygame.display.update()
        sleep(1)
        circle.draw()
        pygame.display.update()

    pygame.quit()
