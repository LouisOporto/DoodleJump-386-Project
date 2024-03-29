import time, sys
import pygame as pg
from settings import Settings
from pygame.locals import *


class Game:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height),0, 32)
        pg.display.set_caption("Doodle Jump")

    def updateEvent(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            # TODO - Player input and other keyboard functions
            if event.type == KEYDOWN:
                pass
            if event.type == KEYUP:
                pass
   

    def play(self):
        finished = False

        while not finished:
            self.screen.fill(self.settings.background_color)
            self.updateEvent()
            pg.display.flip()
            time.sleep(0.02)

if __name__ == "__main__":
    print("Starting Doodle Jump Game")
    game = Game()
    game.play()

  


  