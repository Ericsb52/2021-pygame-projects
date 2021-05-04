from settings import *
import pygame as pg
vec = pg.math.Vector2

class Pawn(pg.sprite.Sprite):

    def __init__(self,game,x,y,color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        self.first_move = True
        if color == "white":
            self.image = self.g.w_pawn
            self.g.white_group.add(self)
        else:
            self.image = self.g.b_pawn
            self.g.black_group.add(self)
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.pos = vec(self.rect.centerx,self.rect.centery)
        self.old_pos = vec(self.rect.centerx,self.rect.centery)
        self.held = False

    def show_avalable_moves(self):
        pass


    def place_peice(self,x,y):

        self.old_pos = vec(x,y)
        self.held = False
        self.g.switch_turn()

    def update(self):

        if self.held == True:
            self.pos = self.g.mouse_pos
        else:
            self.pos = self.old_pos


        self.rect.center=self.pos




class King(pg.sprite.Sprite):

    def __init__(self,game,x,y,color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        if color == "white":
            self.image = self.g.w_king
            self.g.white_group.add(self)
        else:
            self.image = self.g.b_king
            self.g.black_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.pos = self.rect.center
        self.old_pos = self.rect.center
        self.held = False

    def show_avalable_moves(self):
        pass

    def place_peice(self, x, y):

        self.old_pos = vec(x, y)

        self.held = False

        self.g.switch_turn()

    def update(self):

        if self.held == True:
            self.pos = self.g.mouse_pos
        else:
            self.pos = self.old_pos

        self.rect.center = self.pos


class Queen(pg.sprite.Sprite):

    def __init__(self,game,x,y,color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        if color == "white":
            self.image = self.g.w_queen
            self.g.white_group.add(self)
        else:
            self.image = self.g.b_queen
            self.g.black_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.pos = self.rect.center
        self.old_pos = self.rect.center
        self.held = False

    def show_avalable_moves(self):
        pass

    def place_peice(self, x, y):

        self.old_pos = vec(x, y)

        self.held = False

        self.g.switch_turn()
    def update(self):

        if self.held == True:
            self.pos = self.g.mouse_pos
        else:
            self.pos = self.old_pos

        self.rect.center = self.pos


class Bishop(pg.sprite.Sprite):

    def __init__(self,game,x,y,color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        if color == "white":
            self.image = self.g.w_bishop
            self.g.white_group.add(self)
        else:
            self.image = self.g.b_bishop
            self.g.black_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.pos = self.rect.center
        self.old_pos = self.rect.center
        self.held = False

    def show_avalable_moves(self):
        pass

    def place_peice(self, x, y):

        self.old_pos = vec(x, y)

        self.held = False

        self.g.switch_turn()
    def update(self):

        if self.held == True:
            self.pos = self.g.mouse_pos
        else:
            self.pos = self.old_pos

        self.rect.center = self.pos


class Knight(pg.sprite.Sprite):

    def __init__(self,game,x,y,color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        if color == "white":
            self.image = self.g.w_knight
            self.g.white_group.add(self)
        else:
            self.image = self.g.b_knight
            self.g.black_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.pos = self.rect.center
        self.old_pos = self.rect.center
        self.held = False

    def show_avalable_moves(self):
        pass

    def place_peice(self, x, y):

        self.old_pos = vec(x, y)

        self.held = False

        self.g.switch_turn()

    def update(self):

        if self.held == True:
            self.pos = self.g.mouse_pos
        else:
            self.pos = self.old_pos

        self.rect.center = self.pos


class Rook(pg.sprite.Sprite):

    def __init__(self,game,x,y,color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.g = game
        if color == "white":
            self.image = self.g.w_rook
            self.g.white_group.add(self)
        else:
            self.image = self.g.b_rook
            self.g.black_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.center=(x,y)
        self.pos = self.rect.center
        self.old_pos = self.rect.center
        self.held = False

    def show_avalable_moves(self):
        pass

    def place_peice(self, x, y):

        self.old_pos = vec(x, y)

        self.held = False

        self.g.switch_turn()
    def update(self):

        if self.held == True:
            self.pos = self.g.mouse_pos
        else:
            self.pos = self.old_pos

        self.rect.center = self.pos

