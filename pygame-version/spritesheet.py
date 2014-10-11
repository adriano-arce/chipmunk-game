from settings import *

class SpriteSheet:
    def __init__(self, file_name, patch_size):
        self.sheet = pygame.image.load(file_name).convert_alpha()
        self.patch_size = patch_size

    def patch2pixel(self, patch_coords):
        """
        Computes the top left pixel coordinate of the given patch.
        """
        left = self.patch_size[0] * patch_coords[0]
        top  = self.patch_size[1] * patch_coords[1]
        return left, top

    # TODO: Consider caching all patches into a 2D-array.
    def get_patch(self, patch_coords):
        """
        Returns the requested patch image from the sprite sheet.
        """

        # Create a new blank image.
        patch = pygame.Surface(self.patch_size)
        patch.fill(CELL_COLOUR)
        patch.set_colorkey(CELL_COLOUR)

        # Copy the patch from the large sheet onto the smaller image.
        patch.blit(self.sheet, (0, 0),
                   (self.patch2pixel(patch_coords), self.patch_size))

        # Set the transparent colour.
        patch.set_colorkey(CELL_COLOUR)

        return pygame.transform.scale(patch, (CELL_SIDE, CELL_SIDE))