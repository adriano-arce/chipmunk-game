from grid import *
from collections import deque
from spritesheet import SpriteSheet


class Chipmunk(pygame.sprite.Sprite):

    ###############################
    # Order matches ALL_DIRS.     #
    ###############################
    #    UP0,    UP1, ...,    UP8 #
    #  LEFT0,  LEFT1, ...,  LEFT8 #
    #  DOWN0,  DOWN1, ...,  DOWN8 #
    # RIGHT0, RIGHT1, ..., RIGHT8 #
    ###############################
    file_name = "images/fake-chipmunk.png"
    patch_size = (64, 64)  # Each patch is 64 by 64 px.
    cycle_len = 9          # Each cycle takes 9 patches to complete.
    speed = 7              # The patch travels at 7 pixels per frame.
    assert (CELL_SIDE + LINE_WIDTH) % speed == 0,\
        "(CELL_SIDE + LINE_WIDTH) must be evenly divisible by speed."
    assert ((CELL_SIDE + LINE_WIDTH) // speed) % (cycle_len + 1) == 0,\
        "(CELL_SIDE + LINE_WIDTH) // speed must be evenly divisible by (cycle_len + 1)."

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.sheet = SpriteSheet(Chipmunk.file_name, Chipmunk.patch_size)
        self.patch_coords = [0, 2]  # Initially facing down, at DOWN0.
        self._progress = 0
        self.image = self.sheet.get_patch(self.patch_coords)

        self.dir_queue = deque()
        self.curr_dir = None
        self._cell_coords = Grid.empty_cells.pop()
        self._next_cell_coords = None
        self.rect = self.image.get_rect()
        self.rect.topleft = Grid.cell2pixel(self._cell_coords)

        self.acorn_count = 0

    def turn_to(self, new_dir):
        """
        Turns towards the given direction, if necessary.
        """
        if self.patch_coords[1] != new_dir.index:
            self.patch_coords[1] = new_dir.index
            self.image = self.sheet.get_patch(self.patch_coords)

    def update(self):
        """
        Update the chipmunk.
        """
        if self._next_cell_coords:
            self.rect = \
                self.rect.move(self.curr_dir.offset[0] * self.speed,
                               self.curr_dir.offset[1] * self.speed)
            self.patch_coords[0] = self._progress % self.cycle_len
            self.image = self.sheet.get_patch(self.patch_coords)
            self._progress += 1
            if self.rect.topleft ==\
                    Grid.cell2pixel(self._next_cell_coords):
                self._progress = 0
                self._cell_coords = self._next_cell_coords
                self._next_cell_coords = None
                self.curr_dir = None
        else:
            if self.dir_queue:  # The queue is nonempty.
                self.curr_dir = self.dir_queue[0]
                self.turn_to(self.curr_dir)

                next_cell_x = self._cell_coords[0] + self.curr_dir.offset[0]
                next_cell_y = self._cell_coords[1] + self.curr_dir.offset[1]
                if 0 <= next_cell_x < GRID.width:
                    if 0 <= next_cell_y < GRID.height:
                        self._next_cell_coords = (next_cell_x,
                                                  next_cell_y)