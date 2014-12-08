from collections import namedtuple
from pygame.constants import *


# Frame rate stuff.
FPS = 60

# Custom user event stuff.
SECOND_EVENT = USEREVENT + 1
GAME_LENGTH = 3 * 60  # 3 minutes long.

# (SCREEN.width, SCREEN.height) is the size of the screen in pixels.
# (GRID.width, GRID.height) is the size of the grid in tiles.
# Each tile has a position (x, y), where:
#     0 <= x < GRID.width
#     0 <= y < GRID.height
# (TILE.width, TILE.height) is the size of each tile in pixels.
Size = namedtuple("Size", "width, height")
ACORN       = Size(30, 30)
NEST        = Size(50, 50)
SCREEN      = Size(1240, 900)
GRID        = Size(16, 12)
TILE        = Size(64, 64)
MARGIN      = Size(
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
    "WWWWWWWWWWWWWWWW",
    "W              W",
    "W              W",
    "W              W",
    "W   WWWW       W",
    "W   W          W",
    "W   W          W",
    "W   W          W",
    "W              W",
    "W              W",
    "W              W",
    "WWWWWWWWWWWWWWWW"
]
assert len(TILE_MAP) == GRID.height, "Map and grid heights must match."
assert len(TILE_MAP[0]) == GRID.width, "Map and grid widths must match."

# Colour stuff.
Colour = namedtuple("Colour", "red, green, blue")
_BEIGE     = Colour(245, 245, 220)
_WHITE     = Colour(255, 255, 255)
_DARK_GRAY = Colour(100, 100, 100)
_NAVY_BLUE = Colour( 60,  60, 100)
_RED       = Colour(255,   0,   0)
BKGD_COLOUR  = _DARK_GRAY
WALL_COLOUR  = _NAVY_BLUE
FLOOR_COLOUR = _BEIGE
FONT_COLOUR  = _WHITE
NEST_COLOUR  = _RED

# Font stuff.
Font = namedtuple("Font", "name, size")
_BASIC = Font("consolas", 28)
_FINAL = Font("consolas", 48)
MSG_FONT  = _BASIC
NEST_FONT = _BASIC
END_FONT  = _FINAL

# Direction stuff.
Direction = namedtuple("Direction", "index, keys, offset, abbrev")
UP    = Direction(0, (   K_UP, K_w), ( 0, -1), "U")
LEFT  = Direction(1, ( K_LEFT, K_a), (-1,  0), "L")
DOWN  = Direction(2, ( K_DOWN, K_s), ( 0,  1), "D")
RIGHT = Direction(3, (K_RIGHT, K_d), ( 1,  0), "R")
ALL_DIRS = (UP, LEFT, DOWN, RIGHT)

# Acorn stuff.
MIN_ACORN_SPAWN = 0.5
MAX_ACORN_SPAWN = 1.5
ACORN_INIT_COUNT = 3
ACORN_LIMIT = 10
ACORN_INIT_SPEED = 20
ACORN_FILENAME = "imgs/fake-acorn.png"
ACORN_PATCH = Size(535, 535)

# Chipmunk sprite sheet stuff.
###############################
# Order matches ALL_DIRS.     #
###############################
#    UP0,    UP1, ...,    UP8 #
#  LEFT0,  LEFT1, ...,  LEFT8 #
#  DOWN0,  DOWN1, ...,  DOWN8 #
# RIGHT0, RIGHT1, ..., RIGHT8 #
###############################
CHIP_HITBOX = Size(24, 50)
CHIP_PATCH  = Size(64, 64)
CHIP_FILENAME = "imgs/fake-chipmunk.png"
CHIP_CYCLE_LEN = 9            # The number of patches per cycle.
CHIP_INIT_PATCH_POS = (0, 2)  # Initially facing down, at DOWN0.
CHIP_INIT_SPEED = 9           # Speed in pixels per frame.