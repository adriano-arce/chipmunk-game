from sprite_sheet import SpriteSheet


class GraphicsComponent(object):
    def __init__(self, filename, patch_size, final_size, patch_pos):
        self._sheet = SpriteSheet(filename, patch_size, final_size)
        self._patch_pos = patch_pos

    def get_image(self):
        """Retrieves the sprite's image.

        Returns:
            The sprite's requested patch image.
        """
        return self._sheet.get_patch(self._patch_pos)

    def update(self, sprite):
        sprite.image = self.get_image()