from pygame.sprite import Sprite, Group
import pygame as pg
from random import randint
from vector import Vector
from timer import Timer

class Dog(Sprite):
    def __init__(self, game, v=Vector()):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        
        self.v = v
        self.entered = False # For when alien enters screen
        self.dog_images = [pg.transform.scale(pg.image.load(f'images/dog_{n}.png'), (self.settings.image_scale, self.settings.image_scale)) for n in range (3)]
        self.dog_lasers = game.dog_lasers
        self.image = pg.transform.scale(pg.image.load('images/dog_0.png'), (self.settings.image_scale, self.settings.image_scale))
        self.rect = self.image.get_rect()
        self.timer_normal = Timer(image_list=self.dog_images)
        self.timer = self.timer_normal  

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect.y = self.settings.image_scale
        self.x = float(self.rect.x)

    def update(self):
        
      # Random roll to shoot laser
        if randint(0, self.settings.dog_shoot) == 0:
            self.dog_lasers.add(self.rect, 1)
        self.x += self.v.x
        self.rect.x = self.x
        self.checkEdge()
        self.draw()
    
    def checkEdge(self):
        if not self.entered and (self.rect.left < 0 or self.rect.right > self.settings.screen_width): self.entered = True
        if self.entered:
            if self.rect.left < 0: 
                self.x = 0
                self.v = -self.v
            if self.rect.right > self.settings.screen_width: 
                self.x = self.settings.screen_width - self.rect.width
                self.v = -self.v
        

    def draw(self): 
        self.image = self.timer.image()
        self.screen.blit(self.image, self.rect)

class Dogs:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.dog_group = Group()
        self.laser_group = game.lasers.laser_group
        self.dog_laser_group = game.dog_lasers.laser_group
        self.player = self.game.player
        self.sb = game.scoreboard
        self.stats = game.stats
    
    def reset_dogs(self):
        self.dog_group.empty()


    def create_dog(self, x_position, right):
        v = Vector(-self.settings.dog_speed,0) if right else Vector(self.settings.dog_speed,0)
        new_dog = Dog(self.game, v)
        new_dog.x = x_position
        new_dog.rect.x = x_position
        self.dog_group.add(new_dog)

    def update(self):
        
        if randint(0, int(self.settings.dog_spawn_rate)) == 0:
            if randint(0, 1) == 0:
                self.create_dog(-50, False)
            else:
                self.create_dog(self.settings.screen_height + 50, True)
    
        for dog in self.dog_group.sprites():
            dog.update()
            
        if pg.sprite.groupcollide(self.dog_group, self.laser_group, True, True):
            #Play alien death sound
            self.stats.score += self.settings.dog_point
            self.sb.prep_score()

        player_collided = pg.sprite.spritecollide(self.player, self.dog_laser_group, False)
        if len(player_collided):
            self.player.image = pg.transform.scale(pg.image.load('images/cat_2.png'), (self.settings.image_scale, self.settings.image_scale))
            self.player.draw()
            self.player.isAlive = False