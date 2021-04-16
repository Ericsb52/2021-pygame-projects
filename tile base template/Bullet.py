# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2



class Bullet(pg.sprite.Sprite):

    def __init__(self,game,pos,dir):
        self.groups = game.all_sprites,game.bullet_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(pos)
        self.rect.center = self.pos
        self.spread = random.uniform(-GUN_SPREAD,GUN_SPREAD)
        self.vel = dir.rotate(self.spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel *self.g.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self,self.g.walls_group):
            self.kill()
        if pg.time.get_ticks() -self.spawn_time > BULLET_LIFETIME:
            self.kill()




