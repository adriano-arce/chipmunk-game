from grid import *
from collections import deque
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
    assert (CELL_SIDE + LINE_SIZE) % speed == 0,\
        "(CELL_SIDE + LINE_SIZE) must be evenly divisible by speed."
    assert ((CELL_SIDE + LINE_SIZE) // speed) % (cycle_len + 1) == 0,\
        "(CELL_SIDE + LINE_SIZE) // speed must be evenly divisible by (cycle_len + 1)."

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.sheet = SpriteSheet(Chipmunk.file_name, Chipmunk.patch_size)
        self.patch_coords = [0, 2]  # Initially facing down, at DOWN0.
        self.image = self.sheet.get_patch(self.patch_coords)

        self.dir_queue = deque()
        self._cell_coords = Grid.empty_cells.pop()
        self.rect = self.image.get_rect()
        self.rect.topleft = Grid.cell2pixel(self._cell_coords)

        self.acorn_count = 0

    def turn_to(self, new_dir):
        """
        Turns towards the given direction, if necessary.
        """
        if self.patch_coords[1] != new_dir.index:
            self.patch_coords[1] = new_dir.index
            self.image = self.sheet.get_patch(self.patch_coords)

    def animate_step(self, direction,
                     fps_clock, screen_surf, acorns, text):
        """
        Animates a step towards the given direction in the queue.
        """
        self.turn_to(direction)

        new_cell_x = self._cell_coords[0] + direction.offset[0]
        new_cell_y = self._cell_coords[1] + direction.offset[1]
        new_cell_coords = [new_cell_x, new_cell_y]
        if 0 <= new_cell_x < GRID.width and 0 <= new_cell_y < GRID.height:
            new_pixel_coords = Grid.cell2pixel(new_cell_coords)
            pixel_coords = list(self.rect.topleft)

            # Prepare the base surface.
            screen_surf.fill(BG_COLOUR)
            draw_grid(screen_surf)
            acorns.draw(screen_surf)
            screen_surf.blit(text, text.get_rect())
            base_surf = screen_surf.copy()

            # Mini game loop.
            print()
            for i in range(0, CELL_SIDE + LINE_SIZE, Chipmunk.speed):
                # The event handling loop.
                # TODO: Check for quit.

                # Update all the things.
                pixel_coords[0] += direction.offset[0] * Chipmunk.speed
                pixel_coords[1] += direction.offset[1] * Chipmunk.speed
                self.rect.topleft = pixel_coords
                self.patch_coords[0] = \
                    (i // Chipmunk.speed) % self.cycle_len
                print(self.patch_coords, end=" ")
                self.image = self.sheet.get_patch(self.patch_coords)

                # Draw all the things.
                screen_surf.blit(base_surf, (0, 0))
                screen_surf.blit(self.image, self.rect)

                # Render the screen.
                pygame.display.update()
                fps_clock.tick(FPS)

            self._cell_coords = new_cell_coords
            self.rect.topleft = new_pixel_coords