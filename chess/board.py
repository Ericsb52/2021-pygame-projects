from settings import *
import pygame as pg
vec = pg.math.Vector2

# Art created by
# JohnPablok's improved Cburnett chess set from OpenGameart.org

class Square(pg.sprite.Sprite):
    def __init__(self,game,x,y,pos):
        self.group = game.all_sprites,game.board_group
        pg.sprite.Sprite.__init__(self,self.group)
        self.g = game
        if pos % 2 == 0:
            self.image = self.g.board_imgs[0]
        else:
            self.image = self.g.board_imgs[1]
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.topleft = self.pos
        self.ocupied = False
        self.peice_name = []





