import pygame as pg
from os import path
from settings import *



class Map:
    def __init__(self, filename):
        self.data = []
        with open(path.join(map_folder, filename), "rt") as f:
            for line in f:
                self.data.append(line.strip())
        self.tileWidth = len(self.data[0])
        self.tileHeight = len(self.data)
        self.width = self.tileWidth * TILESIZE
        self.height = self.tileHeight * TILESIZE

class Camera:
    def __init__(self,width,height):
        self.camera = pg.Rect(0,0,width,height)
        self.w = width
        self.h = height

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)

    def update(self,target):
        x = -target.rect.x +int(WIDTH/2)
        y =  -target.rect.y +int(HEIGHT/2)

        # limmit scrolling
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.w - WIDTH), x)
        y = max(-(self.h - HEIGHT), y)

        self.camera = pg.Rect(x,y,self.w,self.h)
