import pygame as pg
import random
from os import path



# set up asset folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')


TITLE = "Chess"
tilesize = 80

WIDTH = tilesize *10 # width of our game window
HEIGHT = tilesize *10 # height of our game window
FPS = 30 # frames per second

FONT_NAME = 'arial'


# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (64,64,64)
LIGHTGREY = (224,224,224)