from grid import *
from random import randint


class Acorn(pygame.sprite.Sprite):
    image = pygame.image.load("images/fake-acorn.png")
    image = pygame.transform.scale(image, (CELL_SIDE, CELL_SIDE))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = Acorn.image.convert_alpha()

        self._cell_coords = Grid.empty_cells.pop()
        self.rect = self.image.get_rect()
        self.rect.topleft = Grid.cell2pixel(self._cell_coords)

    def kill(self):
        """
        Insert the acorn's empty cell before killing it.
        """
        Grid.empty_cells.insert(randint(0, len(Grid.empty_cells)),
                                self._cell_coords)
        pygame.sprite.Sprite.kill(self)