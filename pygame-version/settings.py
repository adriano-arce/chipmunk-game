from collections import namedtuple
from pygame.constants import *


# Set up the frame rate.
FPS = 60

# Set up the custom user events.
SECOND_EVENT = USEREVENT + 1
GAME_LENGTH = 3 * 60  # 3 minutes long.

# (SCREEN.width, SCREEN.height) is the size of the screen in pixels.
# (GRID.width, GRID.height) is the size of the grid in tiles.
# Each tile has a position (x, y), where:
#     0 <= x < GRID.width
#     0 <= y < GRID.height
# (TILE.width, TILE.height) is the size of each tile in pixels.
Size = namedtuple("Size", "width, height")
ACORN  = Size(30, 30)
SCREEN = Size(960, 640)
GRID   = Size(12, 8)
TILE   = Size(70, 70)
MARGIN = Size(
    (SCREEN.width  - GRID.width  * TILE.width) // 2,
    (SCREEN.height - GRID.height * TILE.height) // 2
)
assert SCREEN.width % 2 == 0, "Screen width must be even."
assert SCREEN.height % 2 == 0, "Screen height must be even."
assert GRID.width % 2 == 0, "Grid width must be even."
assert GRID.height % 2 == 0, "Grid height must be even."
assert MARGIN.width > 0, "Grid is too wide for the screen."
assert MARGIN.height > 0, "Grid is too high for the screen."

# The grid's tile map. Each W is a wall.
TILE_MAP = [
    "WWWWWWWWWWWW",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "WWWWWWWWWWWW"
]
assert len(TILE_MAP) == GRID.height, "Map and grid heights must match."
assert len(TILE_MAP[0]) == GRID.width, "Map and grid widths must match."

#             R    G    B
white     = (255, 255, 255)
dark_gray = (100, 100, 100)
navy_blue = ( 60,  60, 100)
red       = (255,   0,   0)

# The above colours shouldn't be directly used (private to this class).
# Assign the colours to more descriptive names like the following.
BKGD_COLOUR  = dark_gray
WALL_COLOUR  = navy_blue
FLOOR_COLOUR = white
FONT_COLOUR  = white
NEST_COLOUR  = red

# The directions.
Direction = namedtuple("Direction", "index, keys, dx, dy, abbrev")
UP    = Direction(0, (   K_UP, K_w),  0, -1, "U")
LEFT  = Direction(1, ( K_LEFT, K_a), -1,  0, "L")
DOWN  = Direction(2, ( K_DOWN, K_s),  0,  1, "D")
RIGHT = Direction(3, (K_RIGHT, K_d),  1,  0, "R")
ALL_DIRS = (UP, LEFT, DOWN, RIGHT)

# Acorn stuff.
ACORN_INIT = 3
ACORN_LIMIT = 10
MIN_ACORN_SPAWN = 0.5
MAX_ACORN_SPAWN = 1.5