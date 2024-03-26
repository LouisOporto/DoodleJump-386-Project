import pygame as pg

class Player:
    cat_images = (pg.image.load(f'images/cat_{n}.png') for n in range (3))
