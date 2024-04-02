import pygame as pg
from pygame.sprite import Sprite, Group

class PlatformGroup:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.platform_group = Group()

    def update(self):
        for platform in self.platform_group.sprites():
            platform.update()
    
    def create_platform(self):
        pass


class Platform(Sprite):
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings


    def update(self):
        pass

    def add(self):
        pass