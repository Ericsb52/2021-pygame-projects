# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from Bullet import *
vec = pg.math.Vector2



class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.image = self.g.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0,0)
        self.pos = vec(x,y)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH


    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED,0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED /2,0).rotate(-self.rot)
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now -self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1,0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.g,pos,dir)
                self.vel = vec(-KICKBACK,0).rotate((-self.rot))


    def update(self):
        self.get_keys()
        self.pos+=self.vel *self.g.dt
        self.rot = (self.rot+self.rot_speed * self.g.dt)%360
        self.image = pg.transform.rotate(self.g.player_img,self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self,self.g.walls_group,"x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self,self.g.walls_group,"y")
        self.rect.center = self.hit_rect.center

