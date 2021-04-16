# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')


TITLE = "Template"

WIDTH = 513  # width of our game window
HEIGHT = 513 # height of our game window
FPS = 30 # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
LBLUE = (0,128,255)
DGREEN = (0,102,0)
DGREY = (96,96,96)
BROWN = (139,69,19)

FRICTION = -.1
# Grid settings
TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE
