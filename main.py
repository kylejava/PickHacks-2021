import pygame
from functions import *
pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("PokeCatcher")
clock = pygame.time.Clock()
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png')]
walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'), pygame.image.load('U4.png')]
walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png')]
bg = pygame.image.load('bg.png')
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


def redrawGameWindow():
    global walkCount
    win.blit(bg , (0 ,0))
    red.draw(win)

    pygame.display.update()


red = player(255,255, 64, 64)

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if(red.x > 30):
            red.x -= red.vel
            red.left = True
            red.right = False
            red.standing = False
    elif keys[pygame.K_RIGHT]:
        if(red.x < (500 - 90)):
            red.x += red.vel
            red.right = True
            red.left = False
            red.standing = False
    elif  keys[pygame.K_UP]:
            if(red.y > 30):
                red.y -= red.vel
                red.up = True
                red.right = False
                red.left = False
                red.down = False
                red.standing = False
    elif  keys[pygame.K_DOWN]:
            if(red.y < (500 - 150)):
                red.y += red.vel
                red.up = False
                red.right = False
                red.left = False
                red.down = True
                red.standing = False
    else:
        red.standing = True

    redrawGameWindow()

pygame.quit()
