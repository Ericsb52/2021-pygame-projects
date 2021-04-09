# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *



class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self,dx=0,dy=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.g.walls_group:
            if wall.x == self.x+dx and wall.y == self.y+dy:
                return True
        return false

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE