from tile import *
from grid import Grid


class Nest(pygame.sprite.Sprite):
    def __init__(self, count_font):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.acorn_count = 0
        self.num_font = count_font

        self.image = pygame.Surface(TILE)
        self.update()

        self._tile_pos = Grid.empty_tiles.pop()
        self.rect = self.image.get_rect()
        self.rect.topleft = tile2pixel(self._tile_pos)

    def update(self):
        """Updates the nest's acorn count."""
        count_str = str(self.acorn_count)
        count_surf = self.num_font.render(count_str, True, FONT_COLOUR)
        self.image.fill(NEST_COLOUR)
        self.image.blit(count_surf, self.image.get_rect())