import pygame
from settings import *


class Acorn(pygame.sprite.Sprite):
    _image = pygame.image.load("images/fake-acorn.png")
    _image = pygame.transform.scale(_image, ACORN)
    groups = tuple()

    def __init__(self, place_rect):
        # Initialize the rect's position before inserting into any groups.
        self.image = self.__class__._image.convert_alpha()
        self.rect = place_rect(self.image.get_rect())

        super().__init__(self.__class__.groups)