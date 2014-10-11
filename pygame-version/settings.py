import pygame
from collections import namedtuple
from pygame.constants import *


# Set up the frame rate.
FPS = 25

# Each cell in the grid is a square with side length CELL_SIDE pixels.
CELL_SIDE = 64
LINE_SIZE = 1

# (GRID.width, GRID.height) is the size of the grid in cells.
# Each cell has a grid coordinate (x, y), where:
#     0 <= x < GRID.width
#     0 <= y < GRID.height
# (SCREEN.width, SCREEN.height) is the size of the screen in pixels.
Size = namedtuple("Size", "width, height")
GRID   = Size(12, 8)
SCREEN = Size(960, 640)
MARGIN = Size(
    (SCREEN.width  - GRID.width  * (CELL_SIDE + LINE_SIZE)) // 2,
    (SCREEN.height - GRID.height * (CELL_SIDE + LINE_SIZE)) // 2
)


def draw_grid(screen):
    """
    Draws the grid to the given screen.
    """
    for cell_x in range(GRID.width):
        for cell_y in range(GRID.height):
            (left, top) = cell2pixel((cell_x, cell_y))
            pygame.draw.rect(screen, CELL_COLOUR,
                             (left, top, CELL_SIDE, CELL_SIDE))


def cell2pixel(cell_coords):
    """
    Computes the top left pixel coordinate of the given cell.
    """
    left = MARGIN.width  + (CELL_SIDE + LINE_SIZE) * cell_coords[0]
    top  = MARGIN.height + (CELL_SIDE + LINE_SIZE) * cell_coords[1]
    return left, top

assert SCREEN.width % 2 == 0, "Screen width must be even."
assert SCREEN.height % 2 == 0, "Screen height must be even."
assert GRID.width % 2 == 0, "Grid width must be even."
assert GRID.height % 2 == 0, "Grid height must be even."
assert MARGIN.width > 0, "Grid is too wide for the screen."
assert MARGIN.height > 0, "Grid is too high for the screen."

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
DARK_GRAY = ( 40,  40,  40)
NAVY_BLUE = ( 60,  60, 100)
RED       = (255,   0,   0)
BG_COLOUR   = NAVY_BLUE
LINE_COLOUR = DARK_GRAY
CELL_COLOUR = WHITE

# The directions.
Direction = namedtuple("Direction", "name, keys, offset")
RIGHT = Direction("right", (K_RIGHT, K_d), ( 1,  0))
DOWN  = Direction( "down", ( K_DOWN, K_s), ( 0,  1))
LEFT  = Direction( "left", ( K_LEFT, K_a), (-1,  0))
UP    = Direction(   "up", (   K_UP, K_w), ( 0, -1))
ALL_DIRS = (RIGHT, DOWN, LEFT, UP)

# Acorn stuff.
ACORN_LIMIT = 10