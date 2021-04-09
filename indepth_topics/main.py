# Pygame template - skeleton for a new pygame project
import pygame
import random
import math
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.left = 0
        self.rect.centery = HEIGHT / 2
        self.vx = 120

    def update(self,deltaTime):
        # # time based vs frame based
        # self.rect.x += self.vx * deltaTime
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0

        # pass
        self.vx,self.vy = 0,0
        # # 4 way movement
        # # keystate = pygame.key.get_pressed()
        # # if keystate[pygame.K_UP]:
        # #     self.vy = -5
        # # elif keystate[pygame.K_DOWN]:
        # #     self.vy = 5
        # # elif keystate[pygame.K_LEFT]:
        # #     self.vx = -5
        # # elif keystate[pygame.K_RIGHT]:
        # #     self.vx = 5
        # # self.rect.x += self.vx
        # # self.rect.y += self.vy
        #
        # 8 way movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.vy = -5
        if keystate[pygame.K_DOWN]:
            self.vy = 5
        if keystate[pygame.K_LEFT]:
            self.vx = -5
        if keystate[pygame.K_RIGHT]:
            self.vx = 5

        # need to explain pathagrium therium
        if self.vx != 0 and self.vy != 0:
            # self.vx *=.7071
            # self.vw /= 1.414
            #or / squroot of 2
            self.vx /= math.sqrt(2)
            self.vy /= math.sqrt(2)


        self.rect.x += self.vx
        self.rect.y += self.vy


# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')

TITLE = "Template"

WIDTH = 600  # width of our game window
HEIGHT = 600 # height of our game window
FPS = 60 # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# # initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# load game assets
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()

# create sprite groups
all_sprites = pygame.sprite.Group()

# create game objects
player = Player()

# add game objects to groups
all_sprites.add(player)

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    deltaTime = clock.tick(FPS) /1000
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update(deltaTime)
    # Render (draw)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()