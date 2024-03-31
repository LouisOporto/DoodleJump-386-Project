import pygame as pg
from pygame.sprite import Sprite

class Laser(Sprite):
    def __init__(self, dj_game):
        super().__init()
        self.screen = dj_game.screen
        self.settings = dj_game.settings
        self.color = self.settings.laser_color

        self.rect = pg.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self.rect.midtop = dj_game.player.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y
    
    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)