import pygame
from settings import *


class BaseTile(pygame.sprite.Sprite):
    def __init__(self, colour, tile_pos):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface(TILE)
        self.image.fill(colour)

        self.tile_pos = tile_pos
        self.rect = self.image.get_rect()
        self.rect.topleft = self.tile2pixel(self.tile_pos)

    @staticmethod
    def tile2pixel(tile_pos):
        """Computes the top left pixel position of the given tile."""
        left = MARGIN.width  + TILE.width  * tile_pos[0]
        top  = MARGIN.height + TILE.height * tile_pos[1]
        return left, top


class Wall(BaseTile):
    def __init__(self, tile_pos):
        BaseTile.__init__(self, WALL_COLOUR, tile_pos)


class Floor(BaseTile):
    def __init__(self, tile_pos):
        BaseTile.__init__(self, FLOOR_COLOUR, tile_pos)