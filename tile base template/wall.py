import pygame as pg
import random
import os
from settings import *


class Wall(pg.sprite.Sprite):

    def __init__(self,game,x,y):
        self.g = game
        self.groups = self.g.all_sprites, self.g.walls_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = self.g.wall_img

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x *TILESIZE
        self.rect.y = y * TILESIZE


class Obstacle(pg.sprite.Sprite):

    def __init__(self,game,x,y,w,h,):
        self.g = game
        self.groups = self.g.walls_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y