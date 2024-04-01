from pygame.sprite import Sprite, Group
import pygame as pg
from timer import Timer

class Dog(Sprite):
    dog_jump_images = (pg.image.load(f'images/dog_{n}.png') for n in range (3))

    def __init__(self, dj_game):
        super().__init__()
        self.dj_game = dj_game
        self.screen = dj_game.screen
        self.settings = dj_game.settings

        self.image = pg.transform.scale(pg.image.load('images/dog_0.png'), (150, 130))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
      self.draw()
    
    def draw(self): self.screen.blit(self.image, self.rect)

    #TODO Implement enemy dogs

class Dogs:
    def __init__(self, dj_game):
        self.dj_game = dj_game
        self.screen = dj_game.screen
        self.settings = dj_game.settings
        self.dog_group = pg.sprite.Group()
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

    # TODO Make a class that manage all dogs