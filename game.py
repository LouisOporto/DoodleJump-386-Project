import time, sys
import pygame as pg
from settings import Settings
from player import Player
from laser import Lasers
from enemy import Dogs
from button import Button
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

        self.play_button = Button(game=self, text='Play')
        self.game_active = False


    def checkEvent(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                self.player.check_keydown_events(event)
            elif event.type == KEYUP:
                self.player.check_keyup_events(event)
            elif event.type == MOUSEMOTION:
                b = self.play_button
                x, y = pg.mouse.get_pos()
                b.select(b.rect.collidepoint(x, y))
            elif event.type == MOUSEBUTTONDOWN:
                b = self.play_button
                x, y = pg.mouse.get_pos()
                if b.rect.collidepoint(x, y):
                    b.press()


    def activate(self):
        self.game_active = True
        
    def play(self):
        finished = False
        while not finished:
            self.screen.fill(self.settings.background_color)
            self.checkEvent()
            if self.game_active:
                self.player.update()
                self.dogs.update()
                self.lasers.update()
            else:
                self.play_button.update()

            pg.display.flip()
            time.sleep(0.02)


if __name__ == "__main__":
    print("Starting Doodle Jump Game")
    game = Game()
    game.play()

  


  