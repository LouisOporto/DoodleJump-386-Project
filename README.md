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


Update April 2
The player only objective is reach as high as possible, whilst avoiding enmey lasers from above (the aliens only fly by left(odd) or right(event) to shoot a predetermined xpos on the map before leaving the screen again) The player cant shoot the aliens, but only dodge lasers. The player cant jump, but everytime it collides with a platform it will give him the ability to jump automatically. This also spawns another platform reacheable to the player with a dynamic minimum platform width. Max - 100 pixels down to a variable min width. The game will increase odds of enemy spawning and maybe speed of the character, the min width of the platforms will decrase until it reaches a min of x pixels. The game is one life one chance. The number of platforms is determined by a random number (1 - 4) can spawn

The illusion here is that the platforms are going down not the player jumping up. The characer is always in view, but the platforms are falling down. Makes it easier to deal with aliens at the top and player in the middle