import pygame as pg
from pygame.sprite import Sprite
from vector import Vector

class Laser(Sprite):
    def __init__(self, game, rect, v):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.v = v
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.laser_color

        self.rect = pg.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        #Change location to be given by arguments (x) and (y)
        self.rect.midtop = rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y
    
        if self.rect.bottom < 0: self.kill()
        self.draw()
    
    def draw(self): pg.draw.rect(self.screen, self.color, self.rect)


class Lasers():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings 
        self.laser_group = pg.sprite.Group()
    
    def resetLasers(self):
        self.laser_group.empty()

    def add(self, rect, direction=-1):
        # Add argument to get direction of laser, position (x, y)
        #if len(self.laser_group) < self.settings.lasers_allowed:                     (optional) limiting the amount of lasers on screen
            new_laser = Laser(self.game, rect, v=Vector(0, direction*self.settings.laser_speed))
            self.laser_group.add(new_laser) 
    
    def update(self):
        for laser in self.laser_group.sprites():
            laser.update()