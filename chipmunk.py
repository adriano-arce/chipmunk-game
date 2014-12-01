from tile import *
from nest import Nest


class Chipmunk(pygame.sprite.Sprite):
    groups = tuple()

    def __init__(self, place_rect, input_comp, physics_comp, graphics_comp):
        # Initialize the rect's position before inserting into any groups.
        self.image = graphics_comp.get_image()
        self.rect = place_rect(self.image.get_rect())

        super().__init__(self.__class__.groups)

        self.acorn_count = 0
        self.nest = Nest(place_rect)
        self.velocity = (0, 0)
        self.input_comp = input_comp
        self.physics_comp = physics_comp
        self.graphics_comp = graphics_comp

    def update(self, world):
        """Updates the chipmunk.

        Note:
            This method gets called once per frame.
        """
        self.input_comp.update(self)
        self.physics_comp.update(self, world)
        self.graphics_comp.update(self)