from input_component import InputComponent
from settings import CHIP_INIT_SPEED, ALL_DIRS


class PlayerInputComponent(InputComponent):
    def __init__(self):
        super().__init__(CHIP_INIT_SPEED)
        self.is_pressed = [False] * len(ALL_DIRS)

    def get_offset(self, curr_x, curr_y):
        """Gets the position offset (or None if no mouse/keyboard input)."""
        (dx, dy) = super().get_offset(curr_x, curr_y)
        if (dx, dy) == (0, 0):  # If no mouse input, check for keyboard input.
            for index, pressed in enumerate(self.is_pressed):
                if pressed:
                    direction = ALL_DIRS[index]
                    dx += direction.offset[0] * self._speed
                    dy += direction.offset[1] * self._speed
        return dx, dy