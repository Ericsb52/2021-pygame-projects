import pygame as pg
import random
from os import path
from peices import *
from board import *

# set up asset folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')


TITLE = "Game Title"

WIDTH = 600  # width of our game window
HEIGHT = 600 # height of our game window
FPS = 30 # frames per second

FONT_NAME = 'arial'

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (64,64,64)