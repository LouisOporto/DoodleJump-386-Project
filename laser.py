import pygame as pg
from pygame.sprite import Sprite
from vector import Vector

class Laser(Sprite):
    def __init__(self, dj_game, v):
        pg.sprite.Sprite.__init__(self)
        self.dj_game = dj_game
        self.v = v
        self.screen = dj_game.screen
        self.settings = dj_game.settings
        self.color = self.settings.laser_color

        self.rect = pg.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self.rect.midtop = dj_game.player.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y
    
        if self.rect.bottom < 0: self.kill()
        self.draw()
    
    def draw(self): pg.draw.rect(self.screen, self.color, self.rect)


class Lasers():
    def __init__(self, dj_game):
        self.dj_game = dj_game
        self.screen = dj_game.screen
        self.settings = dj_game.settings 
        self.laser_group = pg.sprite.Group()
    
    def add(self):
        #if len(self.laser_group) < self.settings.lasers_allowed:                     (optional) limiting the amount of lasers on screen
            new_laser = Laser(self.dj_game, v=Vector(0, -self.settings.laser_speed))
            self.laser_group.add(new_laser) 
    
    def update(self):
        for laser in self.laser_group.sprites():
            laser.update()