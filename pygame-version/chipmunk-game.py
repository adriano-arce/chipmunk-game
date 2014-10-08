import sys
from pygame.locals import *
from grid import *
from chipmunk import Chipmunk


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

    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Chipmunk Game")
    grid = Grid()
    player = Chipmunk()

    while True:
        screen.fill(BG_COLOUR)
        grid.draw(screen)
        screen.blit(player.image, player.rect)

        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()