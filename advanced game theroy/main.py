import pygame as pg
import math

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.vx,self.vy = 0,0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vy = -5
        elif keystate[pg.K_DOWN]:
            self.vy = 5
        elif keystate[pg.K_LEFT]:
            self.vx = -5
        elif keystate[pg.K_RIGHT]:
            self.vx = 5

        # explain the pathagrium therium
        if self.vx != 0 and self.vy != 0:
            self.vx /= 1.414
        #     or
            self.vy *= .7071
            # or
            self.vx *= math.sqrt(2)

        self.rect.x += self.vx
        self.rect.y += self.vy


WIDTH = 1000
HEIGHT = 800
FPS = 60
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

# create game objects
player = Player()

# add game objects to groups
all_sprites.add(player)

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
    # Update
    all_sprites.update()
    # Render (draw)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()