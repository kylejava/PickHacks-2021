import pygame
walkRight = [pygame.image.load('main_character/R1.png'), pygame.image.load('main_character/R2.png'), pygame.image.load('main_character/R3.png'), pygame.image.load('main_character/R4.png')]
walkLeft = [pygame.image.load('main_character/L1.png'), pygame.image.load('main_character/L2.png'), pygame.image.load('main_character/L3.png'), pygame.image.load('main_character/L4.png')]
walkUp = [pygame.image.load('main_character/U1.png'), pygame.image.load('main_character/U2.png'), pygame.image.load('main_character/U3.png'), pygame.image.load('main_character/U4.png')]
walkDown = [pygame.image.load('main_character/D1.png'), pygame.image.load('main_character/D2.png'), pygame.image.load('main_character/D3.png'), pygame.image.load('main_character/D4.png')]
class player(object):
    def __init__(self, x ,y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount  + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount%4] , (self.x , self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount%4] , (self.x , self.y))
                self.walkCount+=1
            elif self.down:
                win.blit(walkDown[self.walkCount%4] , (self.x , self.y))
                self.walkCount+=1
            elif self.up:
                win.blit(walkUp[self.walkCount%4] , (self.x , self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0] , (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0] , (self.x, self.y))
            elif self.down:
                win.blit(walkDown[0] , (self.x, self.y))
            elif self.up:
                win.blit(walkUp[0] , (self.x, self.y))
