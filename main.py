import pygame as pg
import random
from setting import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

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
        if self.player2.vel.y > 0:
            hits2 = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits2:
                self.player2.pos.y = hits2[0].rect.top + 0.1
                self.player2.vel.y = 0

        # If player reached top 1/4 of screen
        if self.player1.rect.top <= HEIGHT / 4:
            self.player1.pos.y += abs(self.player1.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        # if self.player2.rect.top <= HEIGHT / 4:
        #     self.player2.pos.y += abs(self.player2.vel.y)
        #     for plat in self.platforms:
        #         plat.rect.y += abs(self.player2.vel.y)
        #         if plat.rect.top >= HEIGHT:
        #             plat.kill()

        # Spawn new platforms
        while len(self.platforms) < 6:
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
                # if event.key == pg.K_a:
                #     self.player1.update()
                # if event.key == pg.K_d:
                #     self.player1.update()
                # if event.key == pg.K_LEFT:
                #     self.player2.update()
                # if event.key == pg.K_RIGHT:
                #     self.player2.update()
            #self.player1.update()
                # self.player2.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()