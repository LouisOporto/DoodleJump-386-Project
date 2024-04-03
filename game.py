import time, sys
import pygame as pg
from settings import Settings
from player import Player
from laser import Lasers
from enemy import Dogs
from button import Button
from platforms import PlatformGroup
from stats import Stats
from scoreboard import Scoreboard
from sound import Sound
from pygame.locals import *


class Game:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height),0, 32)
        pg.display.set_caption("Doodle Jump")

        self.sound = Sound(bg_music="sounds/music.wav")
        self.lasers = Lasers(self)
        self.dog_lasers = Lasers(self)
        self.stats = Stats(self)
        self.scoreboard = Scoreboard(self)
        self.player = Player(self)
        self.dogs = Dogs(self)
        self.platforms = PlatformGroup(self)

        self.play_button = Button(game=self, text='Play')
        self.game_active = False


    def isActive(self):
        return self.game_active
    
    
    def checkEvent(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pg.quit()
                    sys.exit()
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

    def game_over(self):
        # TODO Play game over music
        pg.mouse.set_visible(True)
        self.play_button.change_text('Play again?')
        self.play_button.show()
        self.game_active = False
        

    def activate(self):
        self.game_active = True
        self.restart_game()
        # TODO - Start background music


    def restart_game(self):
        #Resets score, player, platforms, and dogs
        self.settings.initialize_dynamic_settings()
        self.stats.reset()
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.player.reset_player()
        self.platforms.reset_platforms()
        self.dogs.reset_dogs()
        self.lasers.resetLasers()
        self.dog_lasers.resetLasers()


    def play(self):
        finished = False
        self.sound.play_bg()
        while not finished:
            self.checkEvent()
            self.screen.fill(self.settings.background_color)
            self.platforms.update()
            self.player.update()
            self.scoreboard.update()
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

  


  