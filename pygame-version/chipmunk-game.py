from chipmunk import *
from acorn import Acorn

def main():
    """
    The entry point.
    """
    pygame.init()

    fps_clock = pygame.time.Clock()
    screen_surf = pygame.display.set_mode((SCREEN.width, SCREEN.height))
    pygame.display.set_caption("Chipmunk Game")

    msg_font = pygame.font.SysFont("consolas", 28)

    chipmunks = pygame.sprite.Group()
    acorns = pygame.sprite.Group()
    Acorn.groups = acorns
    Chipmunk.groups = chipmunks

    player = Chipmunk()
    for acornNum in range(ACORN_LIMIT):
        Acorn()

    # The main game loop.
    done = False
    while not done:
        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    done = True
                else:
                    for direction in ALL_DIRS:
                        if event.key in direction.keys:
                            # Enqueue the direction.
                            player.dir_queue.appendleft(direction)
            elif event.type == KEYUP:
                for direction in ALL_DIRS:
                    if event.key in direction.keys:
                        # Remove the direction. Not quite a dequeue.
                        player.dir_queue.remove(direction)

        # Update all the things.
        player.try_step()
        for a in pygame.sprite.spritecollide(player, acorns, True):
            player.acorn_count += 1
            Acorn()
        message = str.format("Collected Acorns: {0}", player.acorn_count)
        text = msg_font.render(message, True, WHITE)

        # Draw all the things.
        screen_surf.fill(BG_COLOUR)
        draw_grid(screen_surf)
        chipmunks.draw(screen_surf)
        acorns.draw(screen_surf)
        screen_surf.blit(text, text.get_rect())

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)

    # Close the window on terminating the main game loop.
    pygame.quit()

if __name__ == "__main__":
    main()