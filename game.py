import time, sys
import pygame as pg
from settings import Settings
from player import Player
from laser import Lasers
from enemy import Dogs
from button import Button
from platforms import PlatformGroup
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
        self.platforms = PlatformGroup(self)

        self.play_button = Button(game=self, text='Play')
        self.game_active = False


    def checkEvent(self):
        # Cool idea to put all events into a single line for player to handle but would likely be less messy if all were here
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN and not self.game_active:
                if event.key == K_q:
                    pg.quit()
                    sys.exit()
            elif event.type == KEYDOWN and self.game_active:
                if event.key == K_q:
                    pg.quit()
                    sys.exit()
                self.player.check_keydown_events(event)
            elif event.type == KEYUP and self.game_active:
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
        
    def restart_game(self):
        #TODO Should reset score, player at starting position and remove all aliens and reset platform to one starting at the center of the map and below player
        pass


    def play(self):
        finished = False
        while not finished:
            self.screen.fill(self.settings.background_color)
            # TODO Need to include a state where the game is visible, but the game is either finished or hasn't begun.
            self.checkEvent() # Should ignore player movement if the game isn't active
            self.player.update()
            self.platforms.update()
            if self.game_active:
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

  


  