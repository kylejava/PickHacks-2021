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
seconds = 60
font = pygame.font.SysFont("comicsans", 30, True)
run = False
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("PokeCatcher")
clock = pygame.time.Clock()
bg = pygame.image.load('bg.png')
image = pygame.image.load('main_character/D1.png')
logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (300,150))

def getPokemon():

    if(pokemon_on_screen < 3 and len(pokemon_list) > 0):
    #    pokemon_on_screen = pokemon_on_screen + 1
        pokemon_num = random.randint(0, len(pokemon_list)-1)
        x = random.randint(90 , 360)
        y =random.randint(90, 360)
        sprite = pokemon_list[pokemon_num]
        new_poke = pokemon(x, y , sprite)
        pokemon_list.pop(pokemon_num)
        return new_poke

def updateTimer():

    text = font.render("Time: " + str(seconds//50 * 1), 1, (255,255,255))
    win.blit(text, (350,00))

def redrawGameWindow():
    global walkCount
    win.blit(bg , (0 ,0))
    updateTimer()
    red.draw(win)
    text = font.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (0, 0))
    poke.draw(win)
    poke2.draw(win)
    poke3.draw(win)
    pygame.display.update()


while(run == False):
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
    win.blit(bg , (0 ,0))
    win.blit(image, (220, 300))
    win.blit(logo, (100, 100))
    keys = pygame.key.get_pressed()
    pygame.display.update()
    if keys[pygame.K_RETURN]:
        run = True


red = player(random.randint(90 , 360),random.randint(90 , 360), 64, 64)
win.blit(image, (red.x, red.y))
poke = getPokemon()
poke2 = getPokemon()
poke3 = getPokemon()
pygame.display.update()
while (run and (seconds//50*1 != 59)):
    clock.tick(27)
    for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False


    if((poke.x -32 < red.x and red.x < poke.x + 32) or (poke.x + 32 < red.x and red.x < poke.x-32)):
        if((poke.y -32 < red.y and red.y < poke.y + 32) or (poke.y + 32 < red.y and red.y < poke.y-32)):
            score += 10
            pokemon_caught += 1
            pokemon_on_screen -= 1
            poke.update()


    if((poke2.x -32 < red.x and red.x < poke2.x + 32) or (poke2.x + 32 < red.x and red.x < poke2.x-32)):
        if((poke2.y -32 < red.y and red.y < poke2.y + 32) or (poke2.y + 32 < red.y and red.y < poke2.y-32)):
            score += 10
            pokemon_caught += 1
            pokemon_on_screen -= 1
            poke2.update()


    if((poke3.x -32 < red.x and red.x < poke3.x + 32) or (poke3.x + 32 < red.x and red.x < poke3.x-32)):
        if((poke3.y -32 < red.y and red.y < poke3.y + 32) or (poke3.y + 32 < red.y and red.y < poke3.y-32)):
            score += 10
            pokemon_caught += 1
            pokemon_on_screen -= 1
            poke3.update()
    


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
    seconds += 1
    pokemon_on_screen += 1

print("Congratulations!")
print("Score: " + str(score))
print("Pokemon Caught: " + str(pokemon_caught))
pygame.quit()
