import pygame
from settings import FLOOR_COLOUR


class SpriteSheet(object):
    def __init__(self, filename, patch_size, final_size):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.patch_size = patch_size
        self.final_size = final_size
        self._patch_dict = {}

    def patch2pixel(self, patch_pos):
        """Returns the top left pixel position of the given patch."""
        left = self.patch_size[0] * patch_pos[0]
        top  = self.patch_size[1] * patch_pos[1]
        return left, top

    def get_patch(self, patch_pos):
        """Returns the requested patch image from the sprite sheet.

        Args:
            patch_pos: An immutable tuple that represents the coordinates of the
                       desired patch in the sprite sheet grid. Don't use a list,
                       since lists aren't hashable.
        """
        # Don't do extra work.
        if patch_pos in self._patch_dict:
            return self._patch_dict[patch_pos]

        # Create a new blank image.
        patch = pygame.Surface(self.patch_size)
        patch.fill(FLOOR_COLOUR)
        patch.set_colorkey(FLOOR_COLOUR)

        # Copy the patch from the large sheet onto the smaller image.
        patch.blit(self.sheet, (0, 0),
                   (self.patch2pixel(patch_pos), self.patch_size))

        # Set the transparent colour and scale to fit.
        # TODO: Once the assets have been finalized, we should decide on their
        # TODO: size. That way, we won't need to scale their size each time.
        patch.set_colorkey(FLOOR_COLOUR)
        patch = pygame.transform.scale(patch, self.final_size)

        # Cache and return the patch.
        self._patch_dict[patch_pos] = patch
        return patch