from settings import *
from random import randint
from collections import deque


class Chipmunk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((CELL_SIDE, CELL_SIDE))
        self.image.fill(RED)

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