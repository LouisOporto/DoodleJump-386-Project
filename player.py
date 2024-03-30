import pygame as pg
from settings import Settings

class Player:
    cat_jump_images = (pg.image.load(f'images/cat_{n}.png') for n in range (3))

    def __init__(self, dj_game):
        self.screen = dj_game.screen
        self.screen_rect = dj_game.screen.get_rect()

        self.settings = dj_game.settings

        self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (200, 200))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.player_speed
        if self.moving_left:
            self.x -= self.settings.player_speed

        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)