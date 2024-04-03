import pygame as pg
from pygame.sprite import Sprite, Group

class PlatformGroup:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.platform_group = Group()
        self.initiate_platofrm()
        self.screen_rect = self.screen.get_rect()

    def update(self):
        for platform in self.platform_group.sprites():
            platform.update()
            if platform.check_bottom():
                self.platform_group.remove(platform)
            
    def initiate_platofrm(self):
        # Will draw the first inital platform when the game begins
        start_platform = Platform(self.game, self.settings.screen_width / 2 - self.settings.platform_max_width / 2, self.settings.screen_height - 100)
        self.platform_group.add(start_platform)
    
    def create_sucession(self):
        # Whenever a platform collides with a player, the game will create the next set of platforms 
        # Random number and random position at a set y height (-10) to be out of players view when spawned. but falls into view
        pass

    def fall(self):
        # When player hits any platform all platforms spawned and exisitng will fall down to imitate a jump from the player.
        pass


class Platform(Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.platform_color

        self.width = self.settings.platform_max_width
        
        self.image = pg.Rect(x, y, self.width, self.settings.platform_height)
        self.x = float(self.image.x)
        self.y = float(self.image.y)
        

    def update(self):
        self.draw()

    def draw(self):
        self.screen.fill(self.color, self.image)

    def check_bottom(self):
        if self.y >= self.settings.screen_height: return True
        return False
    