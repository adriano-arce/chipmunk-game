import pygame
from settings import *
from random import shuffle


def draw_grid(screen_surf):
    """
    Draws the grid to the given screen surface.
    """
    for cell_x in range(GRID.width):
        for cell_y in range(GRID.height):
            (left, top) = Grid.cell2pixel((cell_x, cell_y))
            pygame.draw.rect(screen_surf, CELL_COLOUR,
                             (left, top, CELL_SIDE, CELL_SIDE))


class Grid:
    # ASSERT: empty_cells is always randomized.
    # Popping is easy, inserting is hard.
    empty_cells = [(x, y) for x in range(GRID.width)
                   for y in range(GRID.height)]
    shuffle(empty_cells)

    @staticmethod
    def cell2pixel(cell_coords):
        """
        Computes the left top pixel coordinate of the given cell.
        """
        left = MARGIN.width  + (CELL_SIDE + LINE_SIZE) * cell_coords[0]
        top  = MARGIN.height + (CELL_SIDE + LINE_SIZE) * cell_coords[1]
        return left, top