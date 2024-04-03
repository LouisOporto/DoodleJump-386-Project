class Stats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset()
        with open('output.txt', 'r') as file:
            self.high_score = float(file.readline())

    def reset(self):
        self.score = 0
        self.level = 1


if __name__ == '__main__':
    print("\nERROR: stats.py is the wrong file! To play run game.py\n")