import pygame
from settings import *


class SpriteSheet(object):
    def __init__(self, file_name, patch_size):
        self.sheet = pygame.image.load(file_name).convert_alpha()
        self.patch_size = patch_size
        self._patch_dict = {}

    def patch2pixel(self, patch_coords):
        """Returns the top left pixel coordinate of the given patch."""
        left = self.patch_size[0] * patch_coords[0]
        top  = self.patch_size[1] * patch_coords[1]
        return left, top

    def get_patch(self, patch_coords):
        """Returns the requested patch image from the sprite sheet."""
        # Lists aren't hashable, so convert to an immutable tuple.
        patch_coords = tuple(patch_coords)

        # Don't do extra work.
        if patch_coords in self._patch_dict:
            return self._patch_dict[patch_coords]

        # Create a new blank image.
        patch = pygame.Surface(self.patch_size)
        patch.fill(CELL_COLOUR)
        patch.set_colorkey(CELL_COLOUR)

        # Copy the patch from the large sheet onto the smaller image.
        patch.blit(self.sheet, (0, 0),
                   (self.patch2pixel(patch_coords), self.patch_size))

        # Set the transparent colour and scale to fit.
        patch.set_colorkey(CELL_COLOUR)
        patch = pygame.transform.scale(patch, (CELL_SIDE, CELL_SIDE))

        # Cache and return the patch.
        self._patch_dict[patch_coords] = patch
        return patch