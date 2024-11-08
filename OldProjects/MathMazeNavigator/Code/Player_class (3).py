#Player class
import pygame

#Importing the commands of the keys that the user will press
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #set up the sprite's surf
        self.surf = pygame.image.load(image_file).convert()
        self.surf.set_colorkey((0, 0, 255), RLEACCEL)
        #set up the player as a rectangle in the specified part of the screen
        self.rect = self.surf.get_rect(center=(location))

    def move(self, pressed_keys, moves, movesLeft):
        #if up or w is pressed:
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -10) #moves player up by 10
            moves += 1 #increments moves by 1
            movesLeft -= 1 #decrements 'movesLeft' by 1
        #if down or s is pressed:
        if pressed_keys[K_DOWN] or pressed_keys[K_s]: 
            self.rect.move_ip(0, 10) #moves player down by 10
            moves += 1 #increments moves by 1
            movesLeft -= 1 #decrements 'movesLeft' by 1
        #if left or a is pressed:
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-10, 0) #moves player left by 10
            moves += 1 #increments moves by 1
            movesLeft -= 1 #decrements 'movesLeft' by 1
        #if right or d is pressed:
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(10, 0) #moves player right by 10
            moves += 1 #increments moves by 1
            movesLeft -= 1 #decrements 'movesLeft' by 1

        #following 8 lines stop player from moving off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1920:
            self.rect.right = 1920
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 1080:
            self.rect.bottom = 1080

        return moves, movesLeft


