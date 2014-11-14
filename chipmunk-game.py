from random import randint
from chipmunk import *
from acorn import Acorn
from nest import Nest
from tile import Wall, Floor


def main():
    """The main entry point."""
    pygame.init()

    # Icon should be loaded before mode is set.
    icon = pygame.image.load("images/fake-icon.png")
    icon.set_colorkey(FLOOR_COLOUR)
    pygame.display.set_icon(icon)
    screen_surf = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("Chipmunk Game")

    msg_font = pygame.font.SysFont(*MSG_FONT)
    fps_clock = pygame.time.Clock()

    # Set up the sprite groups.
    floor_tiles = pygame.sprite.RenderUpdates()
    wall_tiles = pygame.sprite.RenderUpdates()
    all_tiles = pygame.sprite.RenderUpdates()
    chipmunks = pygame.sprite.RenderUpdates()
    acorns = pygame.sprite.RenderUpdates()
    nests = pygame.sprite.RenderUpdates()
    all_collidables = pygame.sprite.RenderUpdates()
    Floor.groups = floor_tiles, all_tiles
    Wall.groups = wall_tiles, all_tiles, all_collidables
    Acorn.groups = acorns, all_collidables
    Nest.groups = nests, all_collidables
    Chipmunk.groups = chipmunks, all_collidables

    # NOTE: This only relies on all_collidables.
    # TODO: Consider moving this into a base sprite class?
    def place_rect(rect):
        rect.topleft = (
            MARGIN.width  + randint(0, (GRID.width  - 1) * TILE.width),
            MARGIN.height + randint(0, (GRID.height - 1) * TILE.height)
        )
        other_rects = [s.rect for s in all_collidables.sprites()]
        while rect.collidelist(other_rects) > -1:
            rect.topleft = (
                MARGIN.width  + randint(0, (GRID.width  - 1) * TILE.width),
                MARGIN.height + randint(0, (GRID.height - 1) * TILE.height)
            )
        return rect

    # Parse the tile map.
    for y, row in enumerate(TILE_MAP):
        for x, col in enumerate(row):
            if col == "W":
                Wall((x, y))
            elif col == " ":
                Floor((x, y))
            else:
                raise IOError("Tile map parsing error!")

    # Cache the wall rects in a list. Assumes that walls don't change.
    wall_rects = [w.rect for w in wall_tiles.sprites()]

    # Set up acorn and player stuff.
    total_acorns = ACORN_INIT
    acorn_timer = randint(MIN_ACORN_SPAWN * FPS, MAX_ACORN_SPAWN * FPS)
    player = Chipmunk(place_rect, wall_rects)
    for __ in range(ACORN_INIT):
        Acorn(place_rect)

    # Set up timing stuff.
    seconds_left = GAME_LENGTH
    pygame.time.set_timer(SECOND_EVENT, 1000)

    # The main game loop. Each iteration of this loop is called a frame.
    while True:
        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                return None
            elif event.type == SECOND_EVENT:
                seconds_left -= 1
            elif event.type == MOUSEBUTTONUP:
                curr_pos = player.rect.center
                next_pos = event.pos
                offset = (next_pos[0] - curr_pos[0], next_pos[1] - curr_pos[1])
                print(curr_pos, next_pos, offset)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return screen_surf, player.nest.acorn_count
                else:
                    for direction in ALL_DIRS:
                        if event.key in direction.keys:
                            player.is_pressed[direction.index] = True
            elif event.type == KEYUP:
                for direction in ALL_DIRS:
                    if event.key in direction.keys:
                        player.is_pressed[direction.index] = False

        # Update all the things.
        if seconds_left == 0:
            return screen_surf, player.nest.acorn_count
        player.update()
        for __ in pygame.sprite.spritecollide(player, acorns, True):
            player.acorn_count += 1
            total_acorns -= 1
        if total_acorns < ACORN_LIMIT:
            if acorn_timer < 0:
                Acorn(place_rect)
                total_acorns += 1
                acorn_timer = randint(MIN_ACORN_SPAWN * FPS,
                                      MAX_ACORN_SPAWN * FPS)
            else:
                acorn_timer -= 1
        for nest in pygame.sprite.spritecollide(player, nests, False):
            nest.acorn_count += player.acorn_count
            player.acorn_count = 0
            nest.update()
        acorn_msg = "Collected Acorns: {}".format(player.acorn_count)
        acorn_surf = msg_font.render(acorn_msg, True, FONT_COLOUR)
        minutes, seconds = divmod(seconds_left, 60)
        timer_msg = "{}:{:02d}".format(minutes, seconds)
        timer_surf = msg_font.render(timer_msg, True, FONT_COLOUR)
        timer_rect = timer_surf.get_rect()
        timer_rect.topright = (SCREEN.width, 0)

        # Draw all the things.
        screen_surf.fill(BKGD_COLOUR)
        all_tiles.draw(screen_surf)  # Draw tiles before other sprites.
        nests.draw(screen_surf)  # Draw nests before chipmunks.
        chipmunks.draw(screen_surf)
        acorns.draw(screen_surf)
        screen_surf.blit(acorn_surf, acorn_surf.get_rect())
        screen_surf.blit(timer_surf, timer_rect)

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)


def end_game(screen_surf, acorn_count):
    """The end game screen."""
    # Update all the things.
    end_font = pygame.font.SysFont(*END_FONT)
    message = "Game over! Final score: {0}".format(acorn_count)
    text_surf = end_font.render(message, True, FONT_COLOUR)
    text_rect = text_surf.get_rect()
    text_rect.center = (SCREEN.width // 2, SCREEN.height // 2)

    # Draw all the things.
    screen_surf.fill(BKGD_COLOUR)
    screen_surf.blit(text_surf, text_rect)

    # Render the screen.
    pygame.display.update()

    # The main game loop.
    while True:
        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

if __name__ == "__main__":
    output = main()
    if output is not None:
        (screen, score) = output
        end_game(screen, score)

    # Close the window on terminating the main game loop.
    pygame.quit()