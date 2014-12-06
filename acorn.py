import pygame
from settings import ACORN


class Acorn(pygame.sprite.Sprite):
    _image = pygame.image.load("images/fake-acorn.png")
    _image = pygame.transform.scale(_image, ACORN)
    groups = tuple()

    def __init__(self):
        super().__init__()
        self.image = self.__class__._image.convert_alpha()
        self.rect = None

    def revive(self, place_rect):
        """Initializes the rect's position before inserting into its groups."""
        self.rect = place_rect(self.image.get_rect())
        self.add(self.__class__.groups)

    def kill(self):
        """Resets the rect before removing from all of its groups."""
        self.rect = None
        super().kill()