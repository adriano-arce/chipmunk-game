import sys

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
    The entry point.
    """
    pygame.init()

    fps_clock = pygame.time.Clock()
    screen_surf = pygame.display.set_mode((SCREEN.width, SCREEN.height))
    pygame.display.set_caption("Chipmunk Game")
    grid = Grid()
    player = Chipmunk()

    # The main game loop.
    while True:
        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    for direction in ALL_DIRS:
                        if event.key in direction.keys:
                            player.is_pressed[direction] = True
            elif event.type == KEYUP:
                for direction in ALL_DIRS:
                    if event.key in direction.keys:
                        player.is_pressed[direction] = False

        # Update all the things.
        player.take_step()

        # Draw all the things.
        screen_surf.fill(BG_COLOUR)
        grid.draw(screen_surf)
        screen_surf.blit(player.image, player.rect)

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()