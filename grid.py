from settings import *
from random import shuffle


class Grid(object):
    # ASSERT: empty_tiles is always randomized.
    # Popping is easy, inserting is hard.
    empty_tiles = [(x, y) for x in range(GRID.width)
                   for y in range(GRID.height)]
    shuffle(empty_tiles)