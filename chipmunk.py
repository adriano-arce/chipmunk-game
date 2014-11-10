from collections import deque
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
    speed = 7              # The patch travels at 7 pixels per frame.
    assert TILE.width % speed == 0,\
        "TILE.width must be evenly divisible by speed."
    assert TILE.height % speed == 0,\
        "TILE.height must be evenly divisible by speed."
    assert (TILE.width // speed) % (cycle_len + 1) == 0,\
        "TILE.width must be divisible by cycle_len + 1."
    assert (TILE.height // speed) % (cycle_len + 1) == 0,\
        "TILE.height must be divisible by cycle_len + 1."

    def __init__(self, place_rect):
        # Initialize the rect's position before inserting into any groups.
        self.sheet = SpriteSheet(Chipmunk.file_name, Chipmunk.patch_size)
        self.patch_pos = [0, 2]  # Initially facing down, at DOWN0.
        self.image = self.sheet.get_patch(self.patch_pos)
        self.rect = place_rect(self.image.get_rect())

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.dir_queue = deque()

        self.acorn_count = 0
        self.nest = Nest(place_rect)

    def turn_to(self, new_dir):
        """Turns towards the given direction, if necessary."""
        if self.patch_pos[1] != new_dir.index:
            self.patch_pos[1] = new_dir.index
            self.image = self.sheet.get_patch(self.patch_pos)

    def can_move(self, direction):
        """Returns True iff the chipmunk can move in the given direction."""
        pass

    def update(self):
        """Updates the chipmunk.

        Note:
            This method gets called once per frame.
        """
        if self.dir_queue:  # The queue is nonempty.
            curr_dir = self.dir_queue[0]
            self.turn_to(curr_dir)
            self.rect = self.rect.move(curr_dir.dx * self.speed,
                                       curr_dir.dy * self.speed)

            self.patch_pos[0] += 1
            self.patch_pos[0] %= self.cycle_len
        else:
            self.patch_pos[0] = 0
        self.image = self.sheet.get_patch(self.patch_pos)