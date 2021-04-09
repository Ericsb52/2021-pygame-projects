# Pygame template - skeleton for a new pygame project
import pygame as pg
import random as r

from settings import *
from sprites import *
from wall import *
from tilemap import *

class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()

        # create game objects
        self.player = Player(self)
        self.road_right = Road(self,HEIGHT - 96)
        self.road_left = Road(self,HEIGHT - 288)

        # add game objects to groups
        self.all_sprites.add(self.player)
        self.player_group.add(self.player)

        self.all_sprites.add(self.road_right)
        self.all_sprites.add(self.road_left)

        #start running game loop
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
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_GO_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
