import pygame as pg
from laser import Lasers
from settings import Settings

class Player:
    def __init__(self, dj_game):
        self.screen = dj_game.screen
        self.screen_rect = dj_game.screen.get_rect()
        self.settings = dj_game.settings

        self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (150, 150))
        self.rect = self.image.get_rect()

        self.rect1 = (100,150)
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False

        self.lasers = dj_game.lasers
        self.continuous_fire = False

    def check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.moving_right = True
        elif event.key == pg.K_LEFT:
            self.moving_left = True
        elif event.key == pg.K_UP:
            self.settings.jumping = True
        elif event.key == pg.K_SPACE:
            self.open_fire()

    def check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.moving_right = False
        elif event.key == pg.K_LEFT:
            self.moving_left = False
        elif event.key == pg.K_SPACE:
            self.cease_fire()

    def fire(self): self.lasers.add()
    def open_fire(self): self.continuous_fire = True
    def cease_fire(self): self.continuous_fire = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed

        self.rect.x = self.x
        self.rect.y = self.y

        if self.continuous_fire: self.fire()
        self.jump()
        self.draw()


    def jump(self):
        if self.settings.jumping:
            self.image = pg.transform.scale(pg.image.load('images/cat_1.png'), (150, 150))
            self.y -= self.settings.y_velocity
            self.settings.y_velocity -= self.settings.gravity
            if self.settings.y_velocity < -self.settings.jump_height:
                self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (150, 150))
                self.settings.jumping = False
                self.settings.y_velocity = self.settings.jump_height


    def draw(self):
        self.screen.blit(self.image, self.rect)