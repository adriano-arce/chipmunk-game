from base_sprite import BaseSprite
from chipmunk_graphics_component import ChipmunkGraphicsComponent
from chipmunk_physics_component import ChipmunkPhysicsComponent
from nest import Nest
from player_input_component import PlayerInputComponent


class Chipmunk(BaseSprite):
    def __init__(self, place_rect):
        super().__init__()
        self.revive(place_rect)

        self.acorn_count = 0
        self.nest = Nest(place_rect)
        self.throw_pos = None

    def initialize_components(self):
        self.input_comp = PlayerInputComponent()
        self._physics_comp = ChipmunkPhysicsComponent()
        self._graphics_comp = ChipmunkGraphicsComponent()
