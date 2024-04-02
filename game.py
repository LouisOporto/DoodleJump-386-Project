import time, sys
import pygame as pg
from settings import Settings
from player import Player
from laser import Lasers
from enemy import Dogs
from pygame.locals import *


class Game:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height),0, 32)
        pg.display.set_caption("Doodle Jump")

        self.lasers = Lasers(self)
        self.dogs = Dogs(self)
        self.player = Player(self)


    def checkEvent(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                self.player.check_keydown_events(event)
            elif event.type == KEYUP:
                self.player.check_keyup_events(event)


    def play(self):
        finished = False

        while not finished:
            self.screen.fill(self.settings.background_color)
            self.checkEvent()
            self.player.update()
            self.dogs.update()
            self.lasers.update()

            pg.display.flip()
            time.sleep(0.02)


if __name__ == "__main__":
    print("Starting Doodle Jump Game")
    game = Game()
    game.play()

  


  