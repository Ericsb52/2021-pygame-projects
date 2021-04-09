# Pygame template - skeleton for a new pygame project
import pygame
import random
from os import path

# set up asset folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')
map_folder = path.join(game_folder,"maps")

true = True
false = False

# game window settings
TITLE = "Template"
WIDTH = 1024  # width of our game window
HEIGHT = 768 # height of our game window
FPS = 30 # frames per second

# Colors (R, G, B)
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

# Grid settings
TILESIZE = 32
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE



