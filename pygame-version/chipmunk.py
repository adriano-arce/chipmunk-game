from settings import *
from random import randint
from collections import deque
from spritesheet import SpriteSheet


class Chipmunk(pygame.sprite.Sprite):

    ###############################
    # Each patch is 64 by 64 px.  #
    ###############################
    #    UP0,    UP1, ...,    UP8 #
    #  LEFT0,  LEFT1, ...,  LEFT8 #
    #  DOWN0,  DOWN1, ...,  DOWN8 #
    # RIGHT0, RIGHT1, ..., RIGHT8 #
    ###############################
    file_name = "images/fake-chipmunk.png"
    patch_size = (64, 64)
    patch_count = 9
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.sheet = SpriteSheet(Chipmunk.file_name, Chipmunk.patch_size)
        self.patch_coords = (2, 0)  # Initially facing down.
        self.image = self.sheet.get_patch(self.patch_coords)

        self.dir_queue = deque()
        self._cell_coords = (randint(0, GRID.width  - 1),
                             randint(0, GRID.height - 1))
        self.rect = self.image.get_rect()
        self.move_to(self._cell_coords)

        self.acorn_count = 0




    def move_to(self, new_cell_coords):
        """
        Moves to the given cell. Does nothing if the cell is blocked.
        """
        (new_x, new_y) = new_cell_coords
        if 0 <= new_x < GRID.width and 0 <= new_y < GRID.height:
            self._cell_coords = new_cell_coords
            self.rect.topleft = cell2pixel(new_cell_coords)

    def try_step(self):
        """
        Tries to take a step towards the next direction in the queue.
        Does nothing if the queue is empty or there is an obstacle.
        """
        if self.dir_queue:  # The queue is nonempty.
            direction = self.dir_queue[0]  # Peek at the next direction.
            new_x = self._cell_coords[0] + direction.offset[0]
            new_y = self._cell_coords[1] + direction.offset[1]
            self.move_to((new_x, new_y))