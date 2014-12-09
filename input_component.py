from math import hypot


class InputComponent(object):
    def __init__(self, speed):
        self._speed = speed
        self._next_pos = None

    def get_offset(self, curr_x, curr_y):
        """Gets the position offset (or None if no mouse input)."""
        offset = None
        if self._next_pos:
            (next_x, next_y) = self._next_pos
            offset = (next_x - curr_x, next_y - curr_y)
        return offset

    def update(self, sprite):
        """Updates the given sprite's velocity."""
        (dx, dy) = self.get_offset(*sprite.rect.center)

        dr = hypot(dx, dy)
        if dr <= self._speed:  # We're close enough.
            self._next_pos = None
            sprite.velocity = dx, dy
        else:
            sprite.velocity = dx * self._speed/dr, dy * self._speed/dr