import pygame as pg
from settings import Settings
from settings import Settings

class Player:
    cat_jump_images = (pg.image.load(f'images/cat_{n}.png') for n in range (3))

    def __init__(self, dj_game):
        self.screen = dj_game.screen
        self.screen_rect = dj_game.screen.get_rect()

        self.settings = dj_game.settings

        self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (150, 150))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def jump(self):
        if self.settings.jumping == True:
            self.y -= self.settings.y_velocity
            self.settings.y_velocity -= self.settings.gravity

            if self.settings.y_velocity < -self.settings.jump_height:
                self.settings.jumping = False
                self.settings.y_velocity = self.settings.jump_height

    def draw(self):
        self.screen.blit(self.image, self.rect)