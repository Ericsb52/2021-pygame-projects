from settings import *

class Game(object):

    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.clock = pg.time.Clock()
        self.loadData()

    def loadData(self):
        pass

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.white_group = pg.sprite.Group()
        self.black_group = pg.sprite.Group()
        self.pointer_group = pg.sprite.Group()



        self.run()

    def run(self):
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

    def update(self):
        # Game Loop - update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(GREY)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        # pg.mixer.music.load(path.join(self.snd_dir, 'add intro music name'))
        # pg.mixer.music.play(loops=-1)
        self.screen.fill(GREY)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
        # pg.mixer.music.fadeout(500)

    def show_GO_screen(self):
        # game over/continue
        if not self.running:
            return
        # pg.mixer.music.load(path.join(self.snd_dir, 'add exit music name))
        # pg.mixer.music.play(loops=-1)
        self.screen.fill(GREY)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
        # pg.mixer.music.fadeout(500)

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