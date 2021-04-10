import pygame
import random
import time
from pokemon import *
from player import *
from pokemon_list import *
pygame.init()


#Specific Pokemon Variables
pokemon_caught = []
pokemon_on_screen = 0


#Game & character variabls
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("PokeCatcher")
clock = pygame.time.Clock()
bg = pygame.image.load('bg.png')

def getPokemon():
    if(pokemon_on_screen < 3 and len(pokemon_list) > 0):
        clock.tick(5)
    #    pokemon_on_screen = pokemon_on_screen + 1
        pokemon_num = random.randint(0, len(pokemon_list)-1)
        x = random.randint(90 , 360)
        y =random.randint(90, 360)

        sprite = pokemon_list[pokemon_num]
        new_poke = pokemon(x, y , sprite)
        pokemon_list.pop(pokemon_num)

def redrawGameWindow():
    global walkCount
    win.blit(bg , (0 ,0))
    getPokemon()
    red.draw(win)
    pygame.display.update()

red = player(255,255, 64, 64)
run = True
while (run or len(pokemon_caught) == 151):
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
    pokemon_on_screen += 1
    redrawGameWindow()

pygame.quit()
