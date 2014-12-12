from acorn_graphics_component import AcornGraphicsComponent
from base_sprite import BaseSprite
from input_component import InputComponent
from physics_component import PhysicsComponent
from settings import ACORN_INIT_SPEED, ACORN


class Acorn(BaseSprite):
    def __init__(self):
        super().__init__()

    def initialize_components(self):
        self.input_comp = InputComponent(ACORN_INIT_SPEED)
        self._physics_comp = PhysicsComponent(ACORN)
        self._graphics_comp = AcornGraphicsComponent()