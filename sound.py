import pygame as pg

class Sound:
    """  """
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer_music.load(bg_music)
        pg.mixer_music.set_volume(0.001)
        # TODO: Initialize all sounds needed in the game instance
        # sound = pg.mixer.Sound("filename.wav")
        # self.sounds = {"sound1" : sound}

        jump_sound = pg.mixer.Sound('sounds/jump.wav')
        self.sounds = {'jump' : jump_sound}

    def play_bg(self):
        pg.mixer_music.play(-1, 0, 0)

    def stop_bg(self):
        pg.mixer_music.stop()

    def shoot_laser(self, type):
        # TODO Replace self.sounds with proper naming convetions
        # pg.mixer.Sound.play(self.sounds['enemy laser' if type == LaserType.enemey else 'playerlaser'])
        pass

    def bounce(self):
        # TODO Replace jump with proper sound
        pg.mixer.Sound.play(self.sounds["jump"])

    def gameover(self):
        # TODO
        pg.mixer_music.stop()
        pg.mixer_music.load("audios/gameover.wav")
        pg.play_bg()