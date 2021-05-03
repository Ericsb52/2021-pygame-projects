import pygame as pg
import math

class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx = 0
        self.vy = 0

    def update(self,dt):
        self.vx,self.vy = 200 * dt,0



        keystate = pg.key.get_pressed()

        # sum = 0
        # for i in keystate:
        #     sum+=i
        #
        # if sum <=1:
        #     if keystate[pg.K_DOWN] :
        #         self.vy = 5
        #     elif keystate[pg.K_UP]:
        #         self.vy = -5
        #     elif keystate[pg.K_LEFT]:
        #         self.vx = -5
        #     elif keystate[pg.K_RIGHT]:
        #         self.vx = 5
        # if keystate[pg.K_DOWN]:
        #     self.vy = 5
        # if keystate[pg.K_UP]:
        #     self.vy = -5
        # if keystate[pg.K_LEFT]:
        #     self.vx = -5
        # if keystate[pg.K_RIGHT]:
        #     self.vx = 5

        # if self.vx !=0 and self.vy !=0:
        #     # self.vx /= 1.4142
        #     self.vy *= .7071
        #     self.vx /= math.sqrt(2)



        self.rect.x += self.vx
        self.rect.y += self.vy



WIDTH = 1000
HEIGHT = 800
FPS = 30
TITLE = "4 way vs 8 way movment"

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# # initialize pygame and create window
pg.init()
pg.mixer.init()  # for sound
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

# create sprite groups
all_sprites = pg.sprite.Group()

player =Player(25,HEIGHT/2)
all_sprites.add(player)
# Game Loop
running = True
while running:
    # keep loop running at the right speed
    dt = clock.tick(FPS)/1000
    print(dt)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
    # Update
    all_sprites.update(dt)
    # Render (draw)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()