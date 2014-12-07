from math import atan2, pi
from graphics_component import GraphicsComponent
from settings import *


class ChipmunkGraphicsComponent(GraphicsComponent):
    def __init__(self):
        super().__init__(CHIP_FILENAME, CHIP_PATCH, TILE, CHIP_INIT_PATCH_POS)

    def update(self, chipmunk):
        (patch_x, patch_y) = self.patch_pos
        if chipmunk.velocity != (0, 0):
            patch_x = (patch_x + 1) % CHIP_CYCLE_LEN

            # In the Cartesian plane, the signs for vertical movement swap.
            (dx, dy) = chipmunk.velocity
            angle = atan2(-dy, dx)
            patch_y = self.turn_to(angle)
        else:
            patch_x = 0
        self.patch_pos = (patch_x, patch_y)
        super().update(chipmunk)

    @staticmethod
    def turn_to(angle):
        """Turns towards the given angle, if necessary.

        Returns the index of the direction, as determined by the given angle.
        """
        if -3*pi/4 <= angle < -pi/4:
            direction = DOWN
        elif -pi/4 <= angle < pi/4:
            direction = RIGHT
        elif pi/4 <= angle < 3*pi/4:
            direction = UP
        else:  # -pi <= angle < -3*pi/4 or 3*pi/4 <= angle <= pi
            direction = LEFT

        return direction.index