# DoodleJump-386-Project
Doodle Jump++ Clone made in PyGame

A doodle jump clone that adds more to the original concept of the game.

# Students
Names - Louis Oporto, Amanda Chen


## Run the Game
To play the game run `py game.py`

## Modules

button.py
enemy.py
game.py
laser.py
platforms.py
player.py
scoreboard.py
settings.py
sound.py
stats.py
timer.py
vector.py


# Game Start
The cat should be visible before the game starts, the player is prompted to jump to start. Once the player jumps the platform below the cat will bounce the player and spawn the next random platforms for the cat to land on, this means that aliens should spawn twice as high to where the platforms will be placed for the player. The platforms are reachable to the player, but the quantity of platforms and each of their x positions will be randomized. There is also the chance for lava platforms to appear that will instantly kill the player if they land on them. The dogs spawn randomly on top of the screen (either left or right of the screen). The dogs will shoot randomly down towards the player. The dogs will continue to exist until the player shoots back. When the player succeeds to bounce on the next platform the previous platform will "fall" and are despawned (performance and to make the game one way). The game scores the player for the number of bounces (100 points) and enemies killed (250 points). Level progression with level difficulty increasing the spawn rate of enemies and making platforms widths thinner. The game takes record of score/highscore, with one life. If the player dies or falls that is the end of the round. Player gets a chance to restart the game if needed.

The illusion here is that the platforms are going down not the player jumping up. The character is always in view, but the platforms are falling down. Makes it easier to deal with aliens at the top and player in the middle
