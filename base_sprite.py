import pygame


class BaseSprite(pygame.sprite.Sprite):
    groups = tuple()

    def __init__(self):
        super().__init__()

        self.input_comp = None
        self._physics_comp = None
        self._graphics_comp = None

        self.image = None
        self.rect = None

        self.velocity = None

    # TODO: When AI's implemented, revisit whether or not this is good practice.
    def initialize_components(self):
        pass

    def revive(self, place_rect):
        """Initializes the rect before inserting this sprite into its groups."""
        self.initialize_components()

        self.image = self._graphics_comp.get_image()
        self.rect = place_rect(self.image.get_rect())

        self.velocity = (0, 0)

        self.add(self.__class__.groups)

    def kill(self):
        """Resets the rect before removing this sprite from all groups."""
        self.input_comp = None
        self._physics_comp = None
        self._graphics_comp = None

        self.image = None
        self.rect = None

        self.velocity = None

        super().kill()

    def update(self, world):
        """Updates this sprite (for the current frame)."""
        self.input_comp.update(self)
        self._physics_comp.update(self, world)
        self._graphics_comp.update(self)