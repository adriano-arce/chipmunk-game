from tile import *


class Nest(pygame.sprite.Sprite):
    def __init__(self, place_rect):
        # Initialize the rect's position before inserting into any groups.
        self.image = pygame.Surface(TILE)
        self.rect = place_rect(self.image.get_rect())

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.acorn_count = 0
        self.font = pygame.font.SysFont(*NEST_FONT)
        self.update()

    def update(self):
        """Updates the nest's acorn count."""
        count_str = str(self.acorn_count)
        count_surf = self.font.render(count_str, True, FONT_COLOUR)
        self.image.fill(NEST_COLOUR)
        self.image.blit(count_surf, self.image.get_rect())