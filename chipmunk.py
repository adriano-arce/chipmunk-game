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

        self.offset_queue = deque()

        self.acorn_count = 0
        self.nest = Nest(place_rect)

        self.wall_rects = wall_rects

    def turn_to(self, dx, dy):
        """Turns towards the given offset, if necessary."""
        # In the Cartesian plane, the signs for vertical movement swap.
        angle = atan2(-dy, dx)
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
        # Move each axis separately, checking for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def update(self):
        """Updates the chipmunk.

        Note:
            This method gets called once per frame.
        """
        if self.offset_queue:  # The queue is nonempty.
            offset = self.offset_queue[0]
            self.turn_to(*offset)
            self.patch_pos[0] += 1
            self.patch_pos[0] %= self.cycle_len

            self.move(offset[0] * self.speed, offset[1] * self.speed)
        else:
            self.patch_pos[0] = 0
        self.image = self.sheet.get_patch(self.patch_pos)