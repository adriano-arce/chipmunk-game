from math import atan2, pi
from spritesheet import SpriteSheet
from tile import *


class GraphicsComponent(object):
    ###############################
    # Order matches ALL_DIRS.     #
    ###############################
    #    UP0,    UP1, ...,    UP8 #
    #  LEFT0,  LEFT1, ...,  LEFT8 #
    #  DOWN0,  DOWN1, ...,  DOWN8 #
    # RIGHT0, RIGHT1, ..., RIGHT8 #
    ###############################
    FILE_NAME = "images/fake-chipmunk.png"
    CYCLE_LEN = 9  # Each cycle takes 9 patches to complete.

    def __init__(self):
        self.sheet = SpriteSheet(GraphicsComponent.FILE_NAME, CHIP_PATCH)
        self.patch_pos = [0, 2]  # Initially facing down, at DOWN0.

    def update(self, chipmunk):
        if chipmunk.velocity != (0, 0):
            (dx, dy) = chipmunk.velocity
            # In the Cartesian plane, the signs for vertical movement swap.
            angle = atan2(-dy, dx)
            self.turn_to(angle)
            self.patch_pos[0] = (self.patch_pos[0] + 1) % self.CYCLE_LEN
        else:
            self.patch_pos[0] = 0
        chipmunk.image = self.get_image()

    def turn_to(self, angle):
        """Turns towards the given angle, if necessary."""
        if -3*pi/4 <= angle < -pi/4:
            direction = DOWN
        elif -pi/4 <= angle < pi/4:
            direction = RIGHT
        elif pi/4 <= angle < 3*pi/4:
            direction = UP
        else:  # -pi <= angle < -3*pi/4 or 3*pi/4 <= angle <= pi
            direction = LEFT

        if self.patch_pos[1] != direction.index:
            self.patch_pos[1] = direction.index

    def get_image(self):
        return self.sheet.get_patch(self.patch_pos)