import pygame
from settings import *


class Grid:
    def draw(self, screen):
        """
        Draws this grid to the given screen.
        """
        for cell_x in range(GRID.width):
            for cell_y in range(GRID.height):
                (left, top) = cell2pixel((cell_x, cell_y))
                pygame.draw.rect(screen, CELL_COLOUR,
                                 (left, top, CELL_SIDE, CELL_SIDE))