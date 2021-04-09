# Pygame template - skeleton for a new pygame project
import sys

import pygame as pg
import random
from os import path
from settings import *
from player import *
from wall import *
from tilemap import *



class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # key repeat rate
        pg.key.set_repeat(250,150)
        self.loadData()

    def loadData(self):
        self.map = Map("map.txt")




    def new(self):
        """start a new game"""
        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.walls_group = pg.sprite.Group()

        # create game objects

        # create map
        for row, tiles in enumerate(self.map.data):
            for col,tile in enumerate(tiles):
                if tile == "1":
                    Wall(self,col,row)
                if tile =="p":
                    self.player = Player(self, col, row)

        # create camera
        self.camera = Camera(self.map.width, self.map.height)



        self.run()



    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
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
                # player movment
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def update(self):
        # Game Loop - update
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # *after* drawing everything, flip the display
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
