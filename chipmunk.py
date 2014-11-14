from collections import deque
from math import atan2, pi
from tile import *
from nest import Nest
from spritesheet import SpriteSheet


class Chipmunk(pygame.sprite.Sprite):

    ###############################
    # Order matches ALL_DIRS.     #
    ###############################
    #    UP0,    UP1, ...,    UP8 #
    #  LEFT0,  LEFT1, ...,  LEFT8 #
    #  DOWN0,  DOWN1, ...,  DOWN8 #
    # RIGHT0, RIGHT1, ..., RIGHT8 #
    ###############################
    file_name = "images/fake-chipmunk.png"
    patch_size = (64, 64)  # Each patch is 64 by 64 px.
    cycle_len = 9          # Each cycle takes 9 patches to complete.
    speed = 9              # The patch speed in pixels per frame.

    def __init__(self, place_rect, wall_rects):
        # Initialize the rect's position before inserting into any groups.
        self.sheet = SpriteSheet(Chipmunk.file_name, Chipmunk.patch_size)
        self.patch_pos = [0, 2]  # Initially facing down, at DOWN0.
        self.image = self.sheet.get_patch(self.patch_pos)
        self.rect = place_rect(self.image.get_rect())

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.is_pressed = [False] * len(ALL_DIRS)

        self.acorn_count = 0
        self.nest = Nest(place_rect)

        self.wall_rects = wall_rects

    def turn_to(self, angle):
        """Turns towards the given angle, if necessary."""
        # In the Cartesian plane, the signs for vertical movement swap.
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
            self.image = self.sheet.get_patch(self.patch_pos)

    def move_single_axis(self, dx, dy):
        """Moves in a single axis, checking for collisions."""
        self.rect = self.rect.move(dx, dy)

        indices = self.rect.collidelistall(self.wall_rects)
        if indices:  # There was a collision.
            other_rects = (self.wall_rects[i] for i in indices)
            if dx > 0:
                self.rect.right = min(r.left for r in other_rects)
            if dx < 0:
                self.rect.left = max(r.right for r in other_rects)
            if dy > 0:
                self.rect.bottom = min(r.top for r in other_rects)
            if dy < 0:
                self.rect.top = max(r.bottom for r in other_rects)

    def move(self, dx, dy):
        """Moves each axis separately, checking for collisions both times."""
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def compute_offset(self):
        dx = dy = 0
        for index, pressed in enumerate(self.is_pressed):
            if pressed:
                direction = ALL_DIRS[index]
                dx += direction.offset[0]
                dy += direction.offset[1]
        return dx, dy

    def update(self):
        """Updates the chipmunk.

        Note:
            This method gets called once per frame.
        """
        (dx, dy) = self.compute_offset()
        if (dx, dy) != (0, 0):
            angle = atan2(-dy, dx)
            self.turn_to(angle)

            self.patch_pos[0] += 1
            self.patch_pos[0] %= self.cycle_len

            self.move(self.speed * dx, self.speed * dy)
        else:
            self.patch_pos[0] = 0
        self.image = self.sheet.get_patch(self.patch_pos)