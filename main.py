import pygame
import random
import threading
import time
from pokemon import *
from player import *
from pokemon_list import *
pygame.init()


#Specific Pokemon Variables
pokemon_caught = 0
pokemon_on_screen = 0


#Game & character variabls
score = 0
run = False
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("PokeCatcher")
clock = pygame.time.Clock()
bg = pygame.image.load('bg.png')
image = pygame.image.load('main_character/D1.png')

def getPokemon():

    if(pokemon_on_screen < 1 and len(pokemon_list) > 0):
    #    pokemon_on_screen = pokemon_on_screen + 1
        pokemon_num = random.randint(0, len(pokemon_list)-1)
        x = random.randint(90 , 360)
        y =random.randint(90, 360)
        print(pokemon_num)
        sprite = pokemon_list[pokemon_num]
        new_poke = pokemon(x, y , sprite)
        pokemon_list.pop(pokemon_num)
        return new_poke


def redrawGameWindow():
    global walkCount
    win.blit(bg , (0 ,0))
    red.draw(win)
    poke.draw(win)
    pygame.display.update()


while(run == False):
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
    win.blit(bg , (0 ,0))
    win.blit(image, (220, 200))
    keys = pygame.key.get_pressed()
    pygame.display.update()
    if keys[pygame.K_RETURN]:
        run = True


red = player(random.randint(90 , 360),random.randint(90 , 360), 64, 64)
win.blit(image, (red.x, red.y))
poke = getPokemon()
while (run):
    clock.tick(27)
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False


    if((poke.x -32 < red.x and red.x < poke.x + 32) or (poke.x + 32 < red.x and red.x < poke.x-32)):
        if((poke.y -32 < red.y and red.y < poke.y + 32) or (poke.y + 32 < red.y and red.y < poke.y-32)):
            score += 10
            pokemon_caught += 1
            poke.update()


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
    pokemon_on_screen += 1


print("Score: " + str(score))
print("Pokemon Caught: " + str(pokemon_caught))
pygame.quit()
