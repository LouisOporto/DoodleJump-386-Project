import pygame as pg
from pygame.sprite import Sprite, Group
from random import randint

class PlatformGroup:
    def __init__(self, game):
        self.game = game
        self.player = game.player
        self.screen = game.screen
        self.settings = game.settings
        self.sb = game.scoreboard
        self.platform_group = Group()
        self.initiate_platofrm()
        self.screen_rect = self.screen.get_rect()

    def update(self):
        player_collided = pg.sprite.spritecollide(self.player, self.platform_group, False)
        if self.player.falling:
            if len(player_collided) > 0:
                self.player.jump()
                self.create_sucession()
                self.game.stats.score += self.settings.platform_point
                self.sb.platformJumped()
                self.sb.prep_score()
                self.sb.check_high_score()

        self.fall()

        for platform in self.platform_group.sprites():
            platform.update()

            if platform.check_bottom():
                self.platform_group.remove(platform)
            
    def reset_platforms(self):
        self.platform_group.empty()
        self.initiate_platofrm()

    def initiate_platofrm(self):
        # Will draw the first inital platform when the game begins
        start_platform = Platform(self.game, self.settings.screen_width / 2 - self.settings.platform_max_width / 2, self.settings.screen_height - 100)
        self.platform_group.add(start_platform)

    def create_sucession(self):
        # Whenever a platform collides with a player, the game will create the next set of platforms 
        # Random number and random position at a set y height (-10) to be out of players view when spawned. but falls into view
        number_of_platforms = randint(1, 4)
        width_list = [randint(self.settings.platform_min_width, self.settings.platform_max_width) for x in range(0, number_of_platforms)]
        xpos_list = [randint(0, self.settings.screen_width - 100) for x in range(0, number_of_platforms)]

        for x in range(0, number_of_platforms):
            new_platform = Platform(self.game, xpos_list[x], -10, width_list[x])
            self.platform_group.add(new_platform)

    def fall(self):
        if not self.player.falling:
            # When player hits any platform all platforms spawned and exisitng will fall down to imitate a jump from the player.
            for platform in self.platform_group.sprites():
                platform.y -= self.player.v.y * 2.2


class Platform(Sprite):
    def __init__(self, game, x, y, width=100):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.platform_color
        self.width = width
        
        self.rect = pg.Rect(x, y, self.width, self.settings.platform_height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        self.rect.y = self.y
        self.draw()

    def draw(self):
        self.screen.fill(self.color, self.rect)

    def check_bottom(self):
        if self.y >= self.settings.screen_height: return True
        return False


if __name__ == '__main__':
    print("\nERROR: platforms.py is the wrong file! To play run game.py\n")