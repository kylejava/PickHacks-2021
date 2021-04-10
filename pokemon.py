import pygame
import random
from pokemon_list import *
class pokemon(object):
    def __init__(self, x, y, pokemon_sprite):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        sprite = pygame.image.load(pokemon_sprite)
        self.sprite = pygame.transform.scale(sprite, (64,64))

    def draw(self, win):
        win.blit(self.sprite,(self.x, self.y))

    def update(self):
        self.x = random.randint(90 , 360)
        self.y =random.randint(90, 360)
        pokemon_num = random.randint(0, len(pokemon_list)-1)
        sprite = pygame.image.load(pokemon_list[pokemon_num])
        self.sprite = pygame.transform.scale(sprite, (64,64))
