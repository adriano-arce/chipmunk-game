from grid import *
from random import randint

class Chipmunk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((CELL_SIDE, CELL_SIDE))
        self.image.fill(RED)

        self.dir_stack = []
        self._cell_coords = (randint(0, GRID.width  - 1),
                             randint(0, GRID.height - 1))
        self.rect = self.image.get_rect()
        self.move_to(self._cell_coords)

    def move_to(self, new_cell_coords):
        (new_x, new_y) = new_cell_coords
        if 0 <= new_x < GRID.width and 0 <= new_y < GRID.height:
            self._cell_coords = new_cell_coords
            self.rect.topleft = cell2pixel(new_cell_coords)

    def try_step(self):
        if self.dir_stack:  # The stack is nonempty.
            direction = self.dir_stack[-1]  # Peek the last direction.
            new_x = self._cell_coords[0] + direction.offset[0]
            new_y = self._cell_coords[1] + direction.offset[1]
            self.move_to((new_x, new_y))