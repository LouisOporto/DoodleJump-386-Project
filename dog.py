from pygame.sprite import Sprite, Group
import pygame as pg
from timer import Timer

class Dogs:
    def __init__(self, game):
        self.game = game
        # TODO Make a class that manage all dogs

class Dog(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        #TODO Implement enemy dogs