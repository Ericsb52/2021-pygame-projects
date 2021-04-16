# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class Block(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.g = game
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.dir ="idle"
        self.pos = vec(x,y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self,dx=0,dy=0):
        self.acc.x += dx
        self.acc.y += dy



    def collide_with_bounds(self):
        pass

    def update(self):
        # apply friction
        self.acc.x += self.vel.x * FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        self.rect.topleft = self.pos