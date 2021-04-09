import pygame as pg
import random
import os
from settings import *


class Wall(pg.sprite.Sprite):

    def __init__(self,game,x,y):
        self.g = game
        self.groups = self.g.all_sprites, self.g.walls_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x *TILESIZE
        self.rect.y = y * TILESIZE