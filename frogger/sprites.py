# Pygame template - skeleton for a new pygame project
import pygame as pg
import random as r


from settings import *

class Road(pg.sprite.Sprite):
    def __init__(self,game,y):
        super(Road, self).__init__()
        self.g = game
        self.image = pg.Surface((WIDTH, 128))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = y

class Grass(pg.sprite.Sprite):
    def __init__(self,game,y):
        super(Grass, self).__init__()
        self.g = game
        self.image = pg.Surface((WIDTH, 32))
        self.image.fill(DGREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = y

class Curb(pg.sprite.Sprite):
    def __init__(self,game,y):
        super(Curb, self).__init__()
        self.g = game
        self.image = pg.Surface((WIDTH, 32))
        self.image.fill(DGREY)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = y

class Dirt(pg.sprite.Sprite):
    def __init__(self,game,y):
        super(Dirt, self).__init__()
        self.g = game
        self.image = pg.Surface((WIDTH, 32))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = y

class Water(pg.sprite.Sprite):
    def __init__(self,game,y):
        super(Water, self).__init__()
        self.g = game
        self.image = pg.Surface((WIDTH, 32))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = y







class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.g = game
        self.image = pg.Surface((28, 28))
        self.image.fill(GREEN)
        # self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT-2

    def update(self):
        pass
        # self.rect.x += 5
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0