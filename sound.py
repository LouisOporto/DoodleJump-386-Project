import pygame as pg
import time

class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer_music.load(bg_music)
        pg.mixer_music.set_volume(1.000)
        # TODO: Initialize all sounds needed in the game instance
        # sound = pg.mixer.Sound("filename.wav")
        # self.sounds = {"sound1" : sound}

        jump_sound = pg.mixer.Sound('sounds/jump.wav')
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        self.sounds = {'jump' : jump_sound, 'gameover' : gameover_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0, 0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type):
        # TODO Replace self.sounds with proper naming convetions
        # pg.mixer.Sound.play(self.sounds['enemy laser' if type == LaserType.enemey else 'playerlaser'])
        pass

    def bounce(self): 
        pg.mixer.Sound.play(self.sounds["jump"])

    def gameover(self):
        self.stop_bg()
        pg.mixer.music.load("sounds/gameover.wav")
        self.play_bg()
        time.sleep(2.8)