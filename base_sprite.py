import pygame


class BaseSprite(pygame.sprite.Sprite):
    groups = tuple()

    def __init__(self, input_comp, physics_comp, graphics_comp):
        super().__init__()

        self.input_comp = input_comp
        self.physics_comp = physics_comp
        self.graphics_comp = graphics_comp

        self.image = self.graphics_comp.get_image()
        self.rect = None

    def revive(self, place_rect):
        """Initializes the rect before inserting this sprite into its groups."""
        self.rect = place_rect(self.image.get_rect())
        self.add(self.__class__.groups)

    def kill(self):
        """Resets the rect before removing this sprite from all groups."""
        self.rect = None
        super().kill()

    def update(self, world):
        """Updates this sprite (for the current frame)."""
        self.input_comp.update(self)
        self.physics_comp.update(self, world)
        self.graphics_comp.update(self)