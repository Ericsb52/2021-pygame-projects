# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2


class Mob(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites,game.enemy_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.mob_img
        self.rect=self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x,y)
        self.rect.center = self.pos
        self.rot = 0
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = MOB_HEALTH

    def update(self):
        self.rot = (self.g.player.pos - self.pos).angle_to(vec(1,0))
        self.image = pg.transform.rotate(self.g.mob_img,self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.acc = vec(MOB_SPEED,0).rotate(-self.rot)
        self.acc += self.vel *-1
        self.vel += self.acc *self.g.dt
        self.pos += self.vel*self.g.dt+0.5*self.acc*self.g.dt**2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self,self.g.walls_group,"x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.g.walls_group, "y")
        self.rect.center = self.hit_rect.center
        if self.health < 0 :
            self.kill()

    def draw_health(self):
        if self.health >60:
            col = GREEN
        elif self.health >30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width *self.health / MOB_HEALTH)
        self.health_bar = pg.Rect(0,0,width,7)
        if self.health < MOB_HEALTH:
            pg.draw.rect(self.image,col,self.health_bar)




