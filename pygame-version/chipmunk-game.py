import sys
from chipmunk import *


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
                            # Enqueue the direction.
                            player.dir_queue.insert(0, direction)
            elif event.type == KEYUP:
                for direction in ALL_DIRS:
                    if event.key in direction.keys:
                        # Dequeue the direction.
                        player.dir_queue.pop()

        # Update all the things.
        player.try_step()

        # Draw all the things.
        screen_surf.fill(BG_COLOUR)
        draw_grid(screen_surf)
        screen_surf.blit(player.image, player.rect)

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()