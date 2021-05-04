from mouse import Pointer
from settings import *
import pygame as pg
from peices import *
from board import *

class Game(object):

    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        pg.mouse.set_visible(False)
        self.white_turn = True
        self.turn = "white"
        self.can_click_mouse = True
        self.mouse_pos = vec(0, 0)
        self.click_timer = pg.time.get_ticks()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.clock = pg.time.Clock()
        self.peice_held = []
        self.loadData()

    def loadData(self):
        self.mouse_img = pg.image.load(path.join(img_folder, "fingerpointer.png")).convert()
        self.mouse_img = pg.transform.scale(self.mouse_img, (50, 50))
        self.board_imgs = []
        self.board_img_white = pg.image.load(path.join(img_folder,"square_gray_light.png"))
        self.board_img_white = pg.transform.scale(self.board_img_white,(tilesize,tilesize-1))
        self.board_imgs.append(self.board_img_white)
        self.board_img_black = pg.image.load(path.join(img_folder, "square_gray_dark.png"))
        self.board_img_black = pg.transform.scale(self.board_img_black, (tilesize, tilesize-1))
        self.board_imgs.append(self.board_img_black)
        self.w_pawn = pg.image.load(path.join(img_folder,"w_pawn.png"))
        self.w_pawn = pg.transform.scale(self.w_pawn,(tilesize-20,tilesize-20))
        self.b_pawn = pg.image.load(path.join(img_folder,"b_pawn.png"))
        self.b_pawn = pg.transform.scale(self.b_pawn,(tilesize-20,tilesize-20))
        self.w_king = pg.image.load(path.join(img_folder, "w_king.png"))
        self.w_king = pg.transform.scale(self.w_king, (tilesize - 20, tilesize - 20))
        self.b_king = pg.image.load(path.join(img_folder, "b_king.png"))
        self.b_king = pg.transform.scale(self.b_king, (tilesize - 20, tilesize - 20))
        self.w_queen = pg.image.load(path.join(img_folder, "w_queen.png"))
        self.w_queen = pg.transform.scale(self.w_queen, (tilesize - 20, tilesize - 20))
        self.b_queen = pg.image.load(path.join(img_folder, "b_queen.png"))
        self.b_queen = pg.transform.scale(self.b_queen, (tilesize - 20, tilesize - 20))
        self.w_rook = pg.image.load(path.join(img_folder, "w_rook.png"))
        self.w_rook = pg.transform.scale(self.w_rook, (tilesize - 20, tilesize - 20))
        self.b_rook = pg.image.load(path.join(img_folder, "b_rook.png"))
        self.b_rook = pg.transform.scale(self.b_rook, (tilesize - 20, tilesize -20))
        self.w_bishop = pg.image.load(path.join(img_folder, "w_bishop.png"))
        self.w_bishop = pg.transform.scale(self.w_bishop, (tilesize - 20, tilesize - 20))
        self.b_bishop = pg.image.load(path.join(img_folder, "b_bishop.png"))
        self.b_bishop = pg.transform.scale(self.b_bishop, (tilesize - 20, tilesize - 20))
        self.w_knight = pg.image.load(path.join(img_folder, "w_knight.png"))
        self.w_knight = pg.transform.scale(self.w_knight, (tilesize - 20, tilesize - 20))
        self.b_knight = pg.image.load(path.join(img_folder, "b_knight.png"))
        self.b_knight = pg.transform.scale(self.b_knight, (tilesize - 20, tilesize - 20))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.white_group = pg.sprite.Group()
        self.black_group = pg.sprite.Group()
        self.board_group = pg.sprite.Group()
        self.pointer_group = pg.sprite.Group()
        self.mouse_group = pg.sprite.Group()
        pg.mixer.music.load(path.join(snd_folder,"main game chess.ogg"))
        self.create_board()
        self.spawn_peices()
        self.pointer = Pointer(self)





        self.run()

    def spawn_peices(self):
        color = "black"
        for i in range(8):
            x = Pawn(self,(i*tilesize+tilesize/2)+tilesize,tilesize*2+tilesize/2,color)
        x = King(self, 5*tilesize + tilesize / 2,tilesize*1+tilesize/2,color)
        x = Queen(self, 4 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)
        x = Bishop(self, 3 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)
        x = Bishop(self, 6 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)
        x = Knight(self, 2 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)
        x = Knight(self, 7 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)
        x = Rook(self, 1 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)
        x = Rook(self, 8 * tilesize + tilesize / 2, tilesize * 1 + tilesize / 2, color)

        color = "white"
        for i in range(8):
            x = Pawn(self, (i * tilesize + tilesize / 2) + tilesize, tilesize * 7 + tilesize / 2, color)
        x = King(self, 5 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Queen(self, 4 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Bishop(self, 3 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Bishop(self, 6 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Knight(self, 2 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Knight(self, 7 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Rook(self, 1 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)
        x = Rook(self, 8 * tilesize + tilesize / 2, tilesize * 8 + tilesize / 2, color)

    def create_board(self):
        count = 0
        for i in range(8):
            for y in range(8):
                x = Square(self, (tilesize+i * tilesize), tilesize + y * tilesize, count)
                count += 1
            count -= 1


    def run(self):
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                if event.key == pg.K_q:
                    self.switch_turn()


            if event.type == pg.MOUSEBUTTONDOWN and self.pointer.held == False and self.can_click_mouse:
                self.pointer.held = True
                self.can_click_mouse = False
            if event.type == pg.MOUSEBUTTONUP:
                self.can_click_mouse = True

        self.clicked = pg.mouse.get_pressed()

        if self.turn == "white":
            hits = pg.sprite.spritecollide(self.pointer, self.white_group, False)
            if self.clicked[0] and hits and len(self.peice_held) < 1:
                self.peice_held.append(hits[0])
                self.peice_held[0].held = True

            if len(self.peice_held) > 0 and self.pointer.held == True and self.can_click_mouse:
                hits = pg.sprite.spritecollide(self.peice_held[0],self.board_group,False)
                if self.clicked[0] and hits and hits[0].ocupied == False:
                    self.peice_held[0].place_peice(hits[0].rect.centerx, hits[0].rect.centery)
                    temp_list = self.peice_held[:]
                    for i in temp_list:
                        self.peice_held.remove(i)
                    self.pointer.held = False
                    self.can_click_mouse = True
                    hits[0].ocupied = True






        if self.turn == "black":
            hits = pg.sprite.spritecollide(self.pointer, self.black_group, False)
            if self.clicked[0] and hits and len(self.peice_held) < 1:
                self.peice_held.append(hits[0])
                self.peice_held[0].held = True
            if len(self.peice_held) > 0 and self.pointer.held == True and self.can_click_mouse:
                hits = pg.sprite.spritecollide(self.peice_held[0],self.board_group,False)
                if self.clicked[0] and hits and hits[0].ocupied == False:
                    self.peice_held[0].place_peice(hits[0].rect.centerx, hits[0].rect.centery)
                    temp_list = self.peice_held[:]
                    for i in temp_list:
                        self.peice_held.remove(i)
                    self.pointer.held = False
                    self.can_click_mouse = True
                    hits[0].ocupied = True
                    



    def update(self):
        # Game Loop - update
        if self.white_turn == True:
            self.turn = "white"
        else:
            self.turn = "black"

        self.all_sprites.update()
        if len(self.peice_held) > 0 and self.clicked[2] == True:
            print("testing release")
            self.peice_held[0].held = False
            self.peice_held.remove(self.peice_held[0])
            self.pointer.held = False

        x = pg.mouse.get_pos()
        self.mouse_pos.x = x[0]
        self.mouse_pos.y = x[1]



    def switch_turn(self):
        self.white_turn = not self.white_turn

    def draw(self):
        # Game Loop - draw
        if self.white_turn:
            self.screen.fill(LIGHTGREY)
            self.draw_text( self.turn+"'s Turn", 48, BLACK, WIDTH / 2, HEIGHT / 35)
        else:
            self.screen.fill(BLACK)
            self.draw_text(self.turn + "'s Turn", 48, WHITE, WIDTH / 2, HEIGHT / 35)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pg.mixer.music.load(path.join(snd_folder, 'intro theme chess.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(GREY)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def show_GO_screen(self):
        # game over/continue
        if not self.running:
            return
        pg.mixer.music.load(path.join(snd_folder, 'end theme chess.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(GREY)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()

while g.running:
    g.show_start_screen()
    g.new()
    g.show_GO_screen()

pg.quit()