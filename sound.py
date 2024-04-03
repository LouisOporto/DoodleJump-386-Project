import pygame as pg
import time

class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(1.000)
        # TODO: Initialize all sounds needed in the game instance
        # sound = pg.mixer.Sound("filename.wav")
        # self.sounds = {"sound1" : sound}

        jump_sound = pg.mixer.Sound('sounds/jump.wav')
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        meow_sound = pg.mixer.Sound('sounds/meow.wav')
        woof_sound = pg.mixer.Sound('sounds/woof.wav')
        dog_hit_sound = pg.mixer.Sound('sounds/dog_hit.wav')
        self.sounds = {'jump' : jump_sound, 'gameover' : gameover_sound,
                       'meow' : meow_sound, 'woof' : woof_sound,
                       'dog_hit' : dog_hit_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0, 0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self):
        pg.mixer.Sound.play(self.sounds['meow'])

    def dog_shoot(self):
        pg.mixer.Sound.play(self.sounds["woof"])

    def bounce(self): 
        pg.mixer.Sound.play(self.sounds["jump"])
    
    def enemy_hit(self):
        pg.mixer.Sound.play(self.sounds['dog_hit'])

    def gameover(self):
        self.stop_bg()
        pg.mixer.Sound.play(self.sounds["gameover"])
        time.sleep(2.8)