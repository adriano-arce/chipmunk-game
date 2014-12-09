from input_component import InputComponent
from settings import CHIP_INIT_SPEED, ALL_DIRS


class PlayerInputComponent(InputComponent):
    def __init__(self):
        super().__init__(CHIP_INIT_SPEED)
        self.is_pressed = [False] * len(ALL_DIRS)

    def get_offset(self, curr_x, curr_y):
        """Gets the position offset (or None if no mouse/keyboard input)."""
        offset = super().get_offset(curr_x, curr_y)
        if offset is None:  # If no mouse input, check for keyboard input.
            dx = dy = 0
            for index, pressed in enumerate(self.is_pressed):
                if pressed:
                    direction = ALL_DIRS[index]
                    dx += direction.offset[0] * self._speed
                    dy += direction.offset[1] * self._speed
            offset = (dx, dy)
        return offset