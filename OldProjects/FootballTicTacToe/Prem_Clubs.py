#Prem Clubs
import pygame

class PremClubs(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100,100))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(location))
        self.__location = location

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.rect = self.surf.get_rect(center=(location))
class Arsenal(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Arsenal.png').convert()

class AstonVilla(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/AstonVilla.png').convert()

class Bournemouth(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Bournemouth.png').convert()

class Brentford(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Brentford.png').convert()

class Brighton(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Brighton.png').convert()

class Burnley(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Burnley.png').convert()

class Chelsea(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Chelsea.png').convert()

class CrystalPalace(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/CrystalPalace.png').convert()

class Everton(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        self.image = pygame.image.load('./ClubPNGs/Everton.png').convert()

class Fulham(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Fulham.png').convert()

class Liverpool(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Liverpool.png').convert()

class Luton(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Luton.png').convert()

class ManchesterCity(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/ManchesterCity.png').convert()

class ManchesterUnited(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/ManchesterUnited.png').convert()

class Newcastle(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Newcastle.png').convert()

class Forest(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Forest.png').convert()

class SheffieldUtd(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/SheffieldUtd.png').convert()

class Tottenham(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Tottenham.png').convert()

class WestHam(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/WestHam.png').convert()

class Wolves(PremClubs):
    #define the constructor method of the class
    def __init__(self, location):
        super().__init__(location)
        #set up the UndoButton as a rectangle in the specified paret of the screen
        self.image = pygame.image.load('./ClubPNGs/Wolves.png').convert()
