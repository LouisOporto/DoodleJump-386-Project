# DoodleJump-386-Project
Doodle Jump Clone made in PyGame


# Modules

game.py
player.py
settings.py
scoreboard.py
timer.py
sound.py
platforms.py
dogs.py
vectors.py
laser.py 
button.py



# Game Start

The cat should be visible before the game starts, the player is prompted to jump to start. Once the player jumps the platform will below the cat will bounce the player and spawn the next random platforms for the cat to land on, this means that aliens should spawn twice as high as the platforms are spawned. The platfroms are reachable to the player, but random in their x position and quanitity. The aliens spawn randomly on top of the screen (with varying x-pos). When the player succeeds to bounce on the next platform the previous platform is despawned (perforamnce and to make the game one way). The game scores the player for the number of bounces (250 points) and enemies killed (500 points). No level progression, but difficulty by increasing spawn rate of enemies and making platforms widths thinner. The game takes record of score/highscore, with one life. If the player dies or falls that is the end of the round. Player gets a chance to restart the game if needed. Restart the game and reset the current score.