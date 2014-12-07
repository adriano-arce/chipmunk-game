from graphics_component import GraphicsComponent
from settings import *


class AcornGraphicsComponent(GraphicsComponent):
    def __init__(self):
        super().__init__(ACORN_FILENAME, ACORN_PATCH, ACORN, (0, 0))