import pygame
from settings import *


def cell2pixel(cell_x, cell_y):
    """
    Computes the left top pixel coordinate of the given cell.
    """
    left = MARGIN_WIDTH  + (CELL_SIDE + LINE_SIZE) * cell_x
    top  = MARGIN_HEIGHT + (CELL_SIDE + LINE_SIZE) * cell_y
    return left, top


class Grid:
    def draw(self, screen):
        """
        Draws this grid to the given screen.
        """
        for cell_x in range(GRID_WIDTH):
            for cell_y in range(GRID_HEIGHT):
                (left, top) = cell2pixel(cell_x, cell_y)
                pygame.draw.rect(screen, CELL_COLOUR,
                                 (left, top, CELL_SIDE, CELL_SIDE))