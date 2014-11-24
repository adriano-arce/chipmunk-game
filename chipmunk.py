from math import atan2, pi
from pygame.rect import Rect
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
    FILE_NAME = "images/fake-chipmunk.png"
    CYCLE_LEN = 9  # Each cycle takes 9 patches to complete.

    def __init__(self, place_rect, wall_rects,
                 input_comp, physics_comp):
        # Initialize the rect's position before inserting into any groups.
        self.sheet = SpriteSheet(Chipmunk.FILE_NAME, CHIP_PATCH)
        self.patch_pos = [0, 2]  # Initially facing down, at DOWN0.
        self.image = self.sheet.get_patch(self.patch_pos)
        self.rect = place_rect(self.image.get_rect())
        self.hitbox = Rect((0, 0), CHIP_HITBOX)
        self.hitbox.midbottom = self.rect.midbottom

        super().__init__(self.groups)

        self.acorn_count = 0
        self.nest = Nest(place_rect)

        self.wall_rects = wall_rects

        self.velocity = (0, 0)
        self.input_comp = input_comp
        self.physics_comp = physics_comp

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
            self.image = self.sheet.get_patch(self.patch_pos)

    def move_single_axis(self, dx, dy):
        """Moves in a single axis, checking for collisions."""
        self.rect.move_ip(dx, dy)
        self.hitbox.midbottom = self.rect.midbottom

        indices = self.hitbox.collidelistall(self.wall_rects)
        if indices:  # There was a collision.
            other_rects = (self.wall_rects[i] for i in indices)
            if dx > 0:
                self.hitbox.right = min(r.left for r in other_rects)
            if dx < 0:
                self.hitbox.left = max(r.right for r in other_rects)
            if dy > 0:
                self.hitbox.bottom = min(r.top for r in other_rects)
            if dy < 0:
                self.hitbox.top = max(r.bottom for r in other_rects)

        self.rect.midbottom = self.hitbox.midbottom

    def move(self, dx, dy):
        """Moves each axis separately, checking for collisions both times."""
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def update(self):
        """Updates the chipmunk.

        Note:
            This method gets called once per frame.
        """
        self.input_comp.update(self)
        self.physics_comp.update(self)

        if self.velocity != (0, 0):
            # In the Cartesian plane, the signs for vertical movement swap.
            (dx, dy) = self.velocity
            angle = atan2(-dy, dx)
            self.turn_to(angle)
            self.move(dx, dy)
            self.patch_pos[0] = (self.patch_pos[0] + 1) % self.CYCLE_LEN
        else:
            self.patch_pos[0] = 0
        self.image = self.sheet.get_patch(self.patch_pos)