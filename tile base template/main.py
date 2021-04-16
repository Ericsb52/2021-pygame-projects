# Pygame template - skeleton for a new pygame project
import sys

import pygame as pg
import random
from os import path
from settings import *
from player import *
from wall import *
from tilemap import *
from Mobs import *

def draw_player_health(surf,x,y,pct):
    if pct < 0:
        pct = 0
    BAR_LEN = 100
    BAR_H = 25
    fill = pct *BAR_LEN
    outline = pg.Rect(x,y,BAR_LEN,BAR_H)
    fill_rect = pg.Rect(x,y,fill,BAR_H)
    if pct > .60:
        col = GREEN
    elif pct > .30:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,WHITE,outline,2)

class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # key repeat rate
        pg.key.set_repeat(250,150)
        self.loadData()

    def loadData(self):
        self.map = TiledMap(path.join(map_folder,"map1tiled.tmx"))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder,WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img,(TILESIZE,TILESIZE))
        self.mob_img = pg.image.load(path.join(img_folder,MOB_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder,BULLET_IMG))
        self.bullet_img = pg.transform.scale(self.bullet_img,(10,10))




    def new(self):
        """start a new game"""
        self.debug = False
        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.walls_group = pg.sprite.Group()
        self.bullet_group = pg.sprite.Group()


        # # create map
        # for row, tiles in enumerate(self.map.data):
        #     for col,tile in enumerate(tiles):
        #         if tile == "1":
        #             Wall(self,col,row)
        #         if tile =="p":
        #             self.player = Player(self, col, row)
        #         if tile == "m":
        #             mob = Mob(self,col,row)

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "player":
                self.player=Player(self,tile_object.x,tile_object.y)
            if tile_object.name == "wall":
                self.obstacale = Obstacle(self,tile_object.x,tile_object.y,tile_object.width,
                                          tile_object.height)
            if tile_object.name =="enemy":
                Mob(self,tile_object.x,tile_object.y)

        #create camera
        self.camera = Camera(self.map.width,self.map.height)




        self.run()



    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()



    def events(self):
        # Game Loop - events

        for event in pg.event.get():
            # check for closing window clicking x
            if event.type == pg.QUIT:
                self.quit()
                # checking keyboard inputs
            if event.type == pg.KEYDOWN:
                # quiting game not program
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                if event.key == pg.K_F1:
                    self.debug = not self.debug


    def update(self):
        # Game Loop - update
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.groupcollide(self.enemy_group,self.bullet_group,False,True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0,0)

        hits = pg.sprite.spritecollide(self.player,self.enemy_group,False,collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DMG
            hit.vel = vec(0,0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos+=vec(MOB_KNOCKBACK,0).rotate(-hits[0].rot)

    def draw(self):
        # Game Loop - draw
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img,self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            if isinstance(sprite,Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image,self.camera.apply(sprite))
            if self.debug:
                pg.draw.rect(self.screen,BLUE,self.camera.apply_rect(sprite.hit_rect),1)

        if self.debug:
            self.draw_grid()
            for wall in self.walls_group:
                pg.draw.rect(self.screen, BLUE, self.camera.apply_rect(wall.rect), 1)
        # *after* drawing everything, flip the display
        # draw hud
        draw_player_health(self.screen,10,10,self.player.health/PLAYER_HEALTH)

        pg.display.flip()

    def draw_grid(self):
        for x in range (0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,DGREY,(x,0),(x,HEIGHT))
        for y in range (0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,DGREY,(0,y),(WIDTH,y))

    def show_start_screen(self):
        pass

    def show_GO_screen(self):
        pass

    def quit(self):
        pg.quit()
        sys.exit()

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
