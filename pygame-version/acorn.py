import pygame
from grid import *
from random import randint
from tile import BaseTile


class Acorn(pygame.sprite.Sprite):
    image = pygame.image.load("images/fake-acorn.png")
    image = pygame.transform.scale(image, TILE)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = Acorn.image.convert_alpha()

        self._tile_pos = Grid.empty_tiles.pop()
        self.rect = self.image.get_rect()
        self.rect.topleft = BaseTile.tile2pixel(self._tile_pos)

    def kill(self):
        """Inserts the acorn's empty tile before killing it.

        Note:
            This gets called by pygame.sprite.spritecollide().
        """
        Grid.empty_tiles.insert(randint(0, len(Grid.empty_tiles)),
                                self._tile_pos)
        pygame.sprite.Sprite.kill(self)