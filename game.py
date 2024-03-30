import time, sys
import pygame as pg
from settings import Settings
from player import Player
from pygame.locals import *


class Game:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height),0, 32)
        pg.display.set_caption("Doodle Jump")

        self.player = Player(self)


    def checkEvent(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # TODO - Player input and other keyboard functions
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.player.moving_right = True
                elif event.key == pg.K_LEFT:
                    self.player.moving_left = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.player.moving_right = False
                elif event.key == pg.K_LEFT:
                    self.player.moving_left = False
            

    def play(self):
        finished = False

        while not finished:
            self.screen.fill(self.settings.background_color)
            self.player.draw()
            self.checkEvent()
            self.player.update()
            pg.display.flip()
            time.sleep(0.02)

if __name__ == "__main__":
    print("Starting Doodle Jump Game")
    game = Game()
    game.play()

  


  