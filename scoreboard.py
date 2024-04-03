import pygame as pg

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.platform = 0


    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        s = f'{rounded_score:,}'

        self.score_image = self.font.render(s, True, self.text_color, self.settings.background_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.bottom - 150


    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}"

        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.background_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top += 20


    def prep_level(self):
        level_str = f'L {self.stats.level}'
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.background_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top += 20


    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            with open('output.txt', 'w') as file:
                file.write(str(self.stats.high_score))
        self.prep_high_score()

    def check_level(self):
        if self.platform > self.settings.next_level:
            self.settings.increase_dynamics()
            self.stats.level += 1
            self.platform = 0
            self.prep_level()


    def platformJumped(self):
        self.platform += 1


    def update(self):
        self.check_level()
        self.draw()


    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)