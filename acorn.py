from tile import *


class Acorn(pygame.sprite.Sprite):
    image = pygame.image.load("images/fake-acorn.png")
    image = pygame.transform.scale(image, ACORN)

    def __init__(self, place_rect):
        # Initialize the rect's position before inserting into any groups.
        self.image = Acorn.image.convert_alpha()
        self.rect = place_rect(self.image.get_rect())

        super().__init__(self.groups)