import pygame as pg
import random
from setting import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.Player_gg = " "

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        self.player1 = Player1(self)
        self.player2 = Player2(self)
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platfrom
        if self.player1.vel.y > 0:
            hits1 = pg.sprite.spritecollide(self.player1, self.platforms, False)
            if hits1:
                self.player1.pos.y = hits1[0].rect.top + 0.1
                self.player1.vel.y = 0
                self.player1.jumping = False
        if self.player2.vel.y > 0:
            hits2 = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits2:
                self.player2.pos.y = hits2[0].rect.top + 0.1
                self.player2.vel.y = 0
                self.player2.jumping = False

        # If player reached top 1/4 of screen
        if self.player1.rect.top < self.player2.rect.top:
            print("1")
            if self.player1.rect.top <= HEIGHT/4:
                self.player1.pos.y += max(abs(self.player1.vel.y), 5)
                for plat in self.platforms:
                    plat.rect.y += max(abs(self.player1.vel.y), 5)
                    if plat.rect.top >= HEIGHT:
                        plat.kill()
        elif self.player1.rect.top > self.player2.rect.top:
            print("2")
            if self.player2.rect.top <= HEIGHT/4:
                self.player2.pos.y += max(abs(self.player2.vel.y), 5)
                for plat in self.platforms:
                    plat.rect.y += max(abs(self.player2.vel.y), 5)
                    if plat.rect.top >= HEIGHT:
                        plat.kill()


        #Die
        if self.player1.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player1.vel.y, 10)
                if sprite.rect.bottom < 0:
                    self.Player_gg = "Player1 DIE"
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        if self.player2.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player2.vel.y, 10)
                if sprite.rect.bottom < 0:
                    self.Player_gg = "Player2 DIE"
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

       #Spawn new platforms
        while len(self.platforms) < 10:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player1.jump()
                if event.key == pg.K_UP:
                    self.player2.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.player1.jump_cut()
                if event.key == pg.K_UP:
                    self.player2.jump_cut()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("1P : w, a, d, 2P : <- ^ ->",
                       22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Space to jump",22,WHITE,WIDTH/2,HEIGHT/2 +25)
        self.draw_text("Press a key to play",
                       22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Press a key to play again",
                       22, WHITE, WIDTH/2, HEIGHT*3/4)
        self.draw_text(self.Player_gg, 40, WHITE, WIDTH/2, HEIGHT/4+60)
        pg.display.flip()
        self.wait_for_key()

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
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()