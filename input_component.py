from math import hypot
from tile import *


class InputComponent(object):
    def __init__(self):
        self.is_pressed = [False] * len(ALL_DIRS)
        self.target_pos = None
        self.speed = CHIP_INIT_SPEED
        assert self.speed > 0, "Speed must be positive."

    def update(self, chipmunk):
        """Updates the given chipmunk's velocity."""
        if self.target_pos:
            (curr_x, curr_y) = chipmunk.rect.center
            (next_x, next_y) = self.target_pos
            (dx, dy) = (next_x - curr_x, next_y - curr_y)
        else:
            dx = dy = 0
            for index, pressed in enumerate(self.is_pressed):
                if pressed:
                    direction = ALL_DIRS[index]
                    dx += direction.offset[0] * self.speed
                    dy += direction.offset[1] * self.speed

        dr = hypot(dx, dy)
        if dr <= self.speed:  # We're close enough.
            self.target_pos = None
            chipmunk.velocity = dx, dy
        else:
            chipmunk.velocity = dx * self.speed/dr, dy * self.speed/dr