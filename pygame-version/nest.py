from grid import *


class Nest(pygame.sprite.Sprite):
    def __init__(self, num_font):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.acorn_count = 0
        self.num_font = num_font

        self.image = pygame.Surface((CELL_SIDE, CELL_SIDE))
        self.update()

        self._cell_coords = Grid.empty_cells.pop()
        self.rect = self.image.get_rect()
        self.rect.topleft = Grid.cell2pixel(self._cell_coords)

    def update(self):
        """Updates the nest."""
        count_str = str(self.acorn_count)
        count_surf = self.num_font.render(count_str, True, FONT_COLOUR)
        self.image.fill(NEST_COLOUR)
        self.image.blit(count_surf, self.image.get_rect())