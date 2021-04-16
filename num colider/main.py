# Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from sprites import *



class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()  # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pg.time.Clock()



    def new(self):
        """start a new game"""
        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.block_group = pg.sprite.Group()
        self.block_group2 = pg.sprite.Group()
        for i in range(2):
            self.block = Block(self,random.randint(0,5),random.randint(0,5))
            self.block_group.add(self.block)
            self.block_group.add(self.block)
            self.all_sprites.add(self.block)




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
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                for player in self.block_group:
                    # quiting game not program
                    if event.key == pg.K_ESCAPE:
                        playing = False
                    # player movment
                    if event.key == pg.K_LEFT :
                        player.acc.x =-1
                        player.dir = "LEFT"
                    if event.key == pg.K_RIGHT :
                        player.acc.x = 1
                        player.dir = "RIGHT"
                    if event.key == pg.K_UP :

                        player.dir = "UP"
                    if event.key == pg.K_DOWN :

                        player.dir = "DOWN"

    def update(self):
        # Game Loop - update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
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

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()
