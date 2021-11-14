import pygame as pg
from setting import *
vec = pg.math.Vector2


class Player1(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    # def move_l(self):
    #     #키보드 a입력시 왼쪽이동
    #     self.acc = vec(0, PLAYER_GRAVITY)
    #
    #     self.acc.x = -PLAYER_ACC
    #     self.acc.x += self.vel.x * PLAYER_FRICTION
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #
    #     if self.pos.x > WIDTH:
    #         self.pos.x = WIDTH
    #     if self.pos.x < 0:
    #         self.pos.x = 0
    #
    #     self.rect.midbottom = self.pos
    # def move_r(self):
    #     #키보드 d입력시 오른쪽이동
    #     self.acc = vec(0, PLAYER_GRAVITY)
    #     self.acc.x = PLAYER_ACC
    #     self.acc.x += self.vel.x * PLAYER_FRICTION
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #
    #     if self.pos.x > WIDTH:
    #         self.pos.x = WIDTH
    #     if self.pos.x < 0:
    #         self.pos.x = 0
    #
    #     self.rect.midbottom = self.pos
    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:                #키보드 a입력시 왼쪽이동
            self.acc.x = -PLAYER_ACC
        # elif keys[pg.K_LEFT]:
        #     self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:                #키보드 d입력시 오른쪽이동
            self.acc.x = PLAYER_ACC
        # elif keys[pg.K_RIGHT]:
        #     self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    # def move_l(self):
    #     #키보드 a입력시 왼쪽이동
    #     self.acc = vec(0, PLAYER_GRAVITY)
    #
    #     self.acc.x = -PLAYER_ACC
    #     self.acc.x += self.vel.x * PLAYER_FRICTION
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #
    #     if self.pos.x > WIDTH:
    #         self.pos.x = WIDTH
    #     if self.pos.x < 0:
    #         self.pos.x = 0
    #
    #     self.rect.midbottom = self.pos
    # def move_r(self):
    #     #키보드 d입력시 오른쪽이동
    #     self.acc = vec(0, PLAYER_GRAVITY)
    #     self.acc.x = PLAYER_ACC
    #     self.acc.x += self.vel.x * PLAYER_FRICTION
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #
    #     if self.pos.x > WIDTH:
    #         self.pos.x = WIDTH
    #     if self.pos.x < 0:
    #         self.pos.x = 0
    #
    #     self.rect.midbottom = self.pos
    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        # if keys[pg.K_a]:                #키보드 a입력시 왼쪽이동
        #     self.acc.x = -PLAYER_ACC
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        # if keys[pg.K_d]:                #키보드 d입력시 오른쪽이동
        #     self.acc.x = PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y