import pygame as pg
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.20)

        jump_sound = pg.mixer.Sound('sounds/jump.wav')
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        meow_sound = pg.mixer.Sound('sounds/meow.wav')
        woof_sound = pg.mixer.Sound('sounds/woof.wav')
        dog_hit_sound = pg.mixer.Sound('sounds/dog_hit.wav')
        cat_hit_sound = pg.mixer.Sound('sounds/cat_hit.wav')
        level_up_sound = pg.mixer.Sound('sounds/level_up.wav')
        self.sounds = {'jump' : jump_sound, 'gameover' : gameover_sound,
                       'meow' : meow_sound, 'woof' : woof_sound,
                       'dog_hit' : dog_hit_sound, 'cat_hit' : cat_hit_sound,
                       'level_up' : level_up_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0, 0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def cat_shoot(self):
        pg.mixer.Sound.play(self.sounds['meow'])

    def dog_shoot(self):
        pg.mixer.Sound.play(self.sounds["woof"])

    def bounce(self):
        pg.mixer.Sound.play(self.sounds["jump"])
    
    def enemy_hit(self):
        pg.mixer.Sound.play(self.sounds['dog_hit'])

    def player_hit(self):
        pg.mixer.Sound.play(self.sounds['cat_hit'])

    def up_level(self):
        pg.mixer.Sound.play(self.sounds['level_up'])

    def gameover(self):
        self.stop_bg()
        pg.mixer.Sound.play(self.sounds["gameover"])
        time.sleep(2.8)


if __name__ == '__main__':
    print("\nERROR: sound.py is the wrong file! To play run game.py\n")