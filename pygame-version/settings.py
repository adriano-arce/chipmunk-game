from collections import namedtuple
from pygame.constants import *


# Set up the frame rate.
FPS = 60

# Each cell in the grid is a square with side length CELL_SIDE pixels.
CELL_SIDE = 69
LINE_WIDTH = 1

# (GRID.width, GRID.height) is the size of the grid in cells.
# Each cell has a grid coordinate (x, y), where:
#     0 <= x < GRID.width
#     0 <= y < GRID.height
# (SCREEN.width, SCREEN.height) is the size of the screen in pixels.
Size = namedtuple("Size", "width, height")
GRID   = Size(12, 8)
SCREEN = Size(960, 640)
MARGIN = Size(
    (SCREEN.width  - GRID.width  * (CELL_SIDE + LINE_WIDTH)) // 2,
    (SCREEN.height - GRID.height * (CELL_SIDE + LINE_WIDTH)) // 2
)

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

# The above colours shouldn't be directly used (private to this class).
# Assign the colours to more descriptive names like the following.
BKGD_COLOUR = NAVY_BLUE
LINE_COLOUR = DARK_GRAY
CELL_COLOUR = WHITE
FONT_COLOUR = WHITE

# The directions.
Direction = namedtuple("Direction", "index, keys, offset, abbrev")
UP    = Direction(0, (   K_UP, K_w), ( 0, -1), "U")
LEFT  = Direction(1, ( K_LEFT, K_a), (-1,  0), "L")
DOWN  = Direction(2, ( K_DOWN, K_s), ( 0,  1), "D")
RIGHT = Direction(3, (K_RIGHT, K_d), ( 1,  0), "R")
ALL_DIRS = (UP, LEFT, DOWN, RIGHT)

# Acorn stuff.
ACORN_INIT = 3
ACORN_LIMIT = 10
MIN_ACORN_SPAWN = 0.5
MAX_ACORN_SPAWN = 1.5