import pygame as pg
from vector import Vector
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.sound = game.sound

        self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (self.settings.image_scale, self.settings.image_scale))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom 
        self.rect.y -= 100
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.v = Vector()
        self.moving_right = False
        self.moving_left = False
        self.falling = True
        self.isAlive = True

        self.lasers = game.lasers
        self.continuous_fire = False

    def reset_player(self):
        self.rect.midbottom = self.screen_rect.midbottom 
        self.rect.y -= 100
        self.v = Vector()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.falling = True
        self.continuous_fire = False
        self.isAlive = True
        self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (self.settings.image_scale, self.settings.image_scale))

    def check_keydown_events(self, event):
        if self.game.isActive():
            if event.key == pg.K_RIGHT:
                self.moving_right = True
            elif event.key == pg.K_LEFT:
                self.moving_left = True
            elif event.key == pg.K_SPACE:
                self.open_fire()

    def check_keyup_events(self, event):
        if self.game.isActive():
            if event.key == pg.K_RIGHT:
                self.moving_right = False
            elif event.key == pg.K_LEFT:
                self.moving_left = False
            elif event.key == pg.K_SPACE:
                self.cease_fire()

    def fire(self): self.lasers.add(self.rect)
    def open_fire(self): self.continuous_fire = True
    def cease_fire(self): self.continuous_fire = False

    def update(self):
        if self.game.isActive():
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.player_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.player_speed

            self.rect.x = self.x
            self.rect.y = self.y
            
            if self.v.y < self.settings.fall_speed:
                self.v.y += self.settings.gravity
            
            if self.v.y < 0:
                self.image = pg.transform.scale(pg.image.load('images/cat_1.png'), (self.settings.image_scale, self.settings.image_scale))
                self.falling = False
            else:
                self.image = pg.transform.scale(pg.image.load('images/cat_0.png'), (self.settings.image_scale, self.settings.image_scale))
                self.falling = True

            self.y += self.v.y
            if self.continuous_fire: self.fire()

            if self.y > self.settings.screen_height:
                self.game.game_over()
            
            if not self.isAlive:
                self.image = pg.transform.scale(pg.image.load('images/cat_2.png'), (self.settings.image_scale, self.settings.image_scale))
                self.draw()
                self.game.game_over()
    
        self.draw()


    def jump(self):
        self.y -= 20
        self.v.y = -self.settings.jump_height
        self.sound.bounce()

    def draw(self):
        self.screen.blit(self.image, self.rect)
