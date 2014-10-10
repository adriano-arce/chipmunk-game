from settings import *
from random import randint


class Acorn(pygame.sprite.Sprite):
    image = pygame.image.load("images/fake-acorn.png")
    image = pygame.transform.scale(image, (CELL_SIDE, CELL_SIDE))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = Acorn.image.convert_alpha()

        # TODO: What if two Acorns spawn in the same place?
        self._cell_coords = (randint(0, GRID.width  - 1),
                             randint(0, GRID.height - 1))
        self.rect = self.image.get_rect()
        self.rect.topleft = cell2pixel(self._cell_coords)
