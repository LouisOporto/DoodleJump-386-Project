import time, sys
import pygame as pg
from pygame.locals import *


class Game:
  def __init__(self):
    pg.init()
    clock = pg.time.Clock()

  def play(self):
    print("Game is running")

if __name__ == "__main__":
  print("Starting Game")
  game = Game()
  game.play()

  


  