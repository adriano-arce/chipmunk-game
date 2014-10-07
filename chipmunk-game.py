import pygame
from pygame.locals import *

import sys

# Set up the frame rate.
FPS = 30
fpsClock = pygame.time.Clock()

# Set up the window.
SCREEN_SIZE = (WIDTH, HEIGHT) = (500, 300)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Chipmunk Game")

#         R    G    B
WHITE = (255, 255, 255)


def terminate():
    """
    Terminates the program.
    """
    pygame.quit()
    sys.exit()


def main():
    """
    The main game loop.
    """
    pygame.init()
    while True:
        SCREEN.fill(WHITE)

        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        # Render the Surface object.
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()