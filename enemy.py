from pygame.sprite import Sprite, Group
from timer import Timer
import pygame as pg

class Dog(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        
        self.dog_images = [pg.transform.scale(pg.image.load(f'images/dog_{n}.png'), (self.settings.image_scale, self.settings.image_scale)) for n in range (3)]

        self.image = pg.transform.scale(pg.image.load('images/dog_0.png'), (self.settings.image_scale, self.settings.image_scale))
        self.rect = self.image.get_rect()

        self.timer_normal = Timer(image_list=self.dog_images)
        self.timer = self.timer_normal  

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
      self.draw()
    
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
        self.create_fleet()

    def create_fleet(self):
        dog = Dog(self)
        dog_width = dog.rect.width / 2

        current_x = dog_width
        while current_x < (self.settings.screen_width -2 * dog_width):
            self.create_dog(current_x)
            current_x += 2 * dog_width

    def create_dog(self, x_position):
        new_dog = Dog(self)
        new_dog.x = x_position
        new_dog.rect.x = x_position
        self.dog_group.add(new_dog)

    def update(self):
        for dog in self.dog_group.sprites():
            dog.update()
            
        if pg.sprite.groupcollide(self.dog_group, self.laser_group, True, True):
            #Play alien death sound
            # Add points
            # Prep score
            pass
