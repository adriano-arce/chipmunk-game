from base_sprite import BaseSprite
from nest import Nest


class Chipmunk(BaseSprite):
    def __init__(self, input_comp, physics_comp, graphics_comp, place_rect):
        super().__init__()
        self.revive(input_comp, physics_comp, graphics_comp, place_rect)

        self.acorn_count = 0
        self.nest = Nest(place_rect)