import pygame as pg
from setting import *
vec = pg.math.Vector2


class Player1(pg.sprite.Sprite):
    def __init__(self, game, msg):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2-200, HEIGHT/2+200)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.msg = msg
    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = self.msg

        if keys == 'L' or 'l':
            self.acc.x = -PLAYER_ACC

        if keys == 'R' or 'r':
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

class Player2(pg.sprite.Sprite):
    def __init__(self, game,client_socket):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(RanDom_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2+200, HEIGHT/2+100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.client_socket = client_socket
    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    def update(self, key):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            msg = 'l'
            data = msg.encode()
            length = len(data)
            self.client_socket.sendall(length.to_bytes(4, byteorder="little"))
            self.client_socket.sendall(data)
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            msg = 'r'
            data = msg.encode()
            length = len(data)
            self.client_socket.sendall(length.to_bytes(4, byteorder="little"))
            self.client_socket.sendall(data)

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
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y