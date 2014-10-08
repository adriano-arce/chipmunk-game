# Set up the frame rate.
FPS = 30

# Each cell in the grid is a square with side length CELL_SIDE pixels.
# (GRID_WIDTH, GRID_HEIGHT) is the size of the grid in cells.
# (SCREEN_WIDTH, SCREEN_HEIGHT) is the size of the screen in pixels.
CELL_SIDE = 30
LINE_SIZE = 1
(GRID_WIDTH, GRID_HEIGHT) = (24, 16)
(SCREEN_WIDTH, SCREEN_HEIGHT) = (960, 600)
(MARGIN_WIDTH, MARGIN_HEIGHT) = (
    (SCREEN_WIDTH  - GRID_WIDTH  * (CELL_SIDE + LINE_SIZE)) // 2,
    (SCREEN_HEIGHT - GRID_HEIGHT * (CELL_SIDE + LINE_SIZE)) // 2
)
assert SCREEN_WIDTH % 2 == 0, "Screen width must be even."
assert SCREEN_HEIGHT % 2 == 0, "Screen height must be even."
assert GRID_WIDTH % 2 == 0, "Grid width must be even."
assert GRID_HEIGHT % 2 == 0, "Grid height must be even."
assert MARGIN_WIDTH > 0, "Grid is too wide for the screen."
assert MARGIN_HEIGHT > 0, "Grid is too high for the screen."

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
DARK_GRAY = ( 40,  40,  40)
NAVY_BLUE = ( 60,  60, 100)
BG_COLOUR   = NAVY_BLUE
LINE_COLOUR = DARK_GRAY
CELL_COLOUR = WHITE