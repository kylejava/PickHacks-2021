import pygame

class pokemon(object):
    def __init__(self, x, y, pokemon_sprite):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.sprite = pygame.image.load(pokemon_sprite)

    def draw(self, win):
        win.blit
