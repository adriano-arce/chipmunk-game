from grid import *
from random import randint


class Chipmunk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([CELL_SIDE, CELL_SIDE])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.topleft = cell2pixel(randint(1, GRID_HEIGHT - 1),
                                       randint(1, GRID_WIDTH - 1))


    def draw(self, screen):
        pygame.draw.rect(screen)