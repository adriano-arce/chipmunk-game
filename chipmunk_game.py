from random import randint
from chipmunk import *
from acorn import Acorn
from nest import Nest
from physics_component import PhysicsComponent
from tile import Wall, Floor
from input_component import InputComponent


class World(object):
    def __init__(self):
        pygame.init()

        # Icon should be loaded before mode is set.
        icon = pygame.image.load("images/fake-icon.png")
        icon.set_colorkey(FLOOR_COLOUR)
        pygame.display.set_icon(icon)
        self.screen_surf = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption("Chipmunk Game")

        self.msg_font = pygame.font.SysFont(*MSG_FONT)
        self.fps_clock = pygame.time.Clock()

        # Set up the sprite groups.
        floor_tiles = pygame.sprite.RenderUpdates()
        self.wall_tiles = pygame.sprite.RenderUpdates()
        self.all_tiles = pygame.sprite.RenderUpdates()
        self.chipmunks = pygame.sprite.RenderUpdates()
        self.acorns = pygame.sprite.RenderUpdates()
        self.nests = pygame.sprite.RenderUpdates()
        self.all_collidables = pygame.sprite.RenderUpdates()
        Floor.groups = floor_tiles, self.all_tiles
        Wall.groups = self.wall_tiles, self.all_tiles, self.all_collidables
        Acorn.groups = self.acorns, self.all_collidables
        Nest.groups = self.nests, self.all_collidables
        Chipmunk.groups = self.chipmunks, self.all_collidables



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
        wall_rects = [w.rect for w in self.wall_tiles.sprites()]

        # Set up acorn and self.player stuff.
        self.total_acorns = ACORN_INIT
        self.acorn_timer = randint(MIN_ACORN_SPAWN * FPS, MAX_ACORN_SPAWN * FPS)
        self.player = Chipmunk(self.place_rect, wall_rects,
                               InputComponent(), PhysicsComponent())
        for __ in range(ACORN_INIT):
            Acorn(self.place_rect)

        # Set up timing stuff.
        self.seconds_left = GAME_LENGTH
        pygame.time.set_timer(SECOND_EVENT, 1000)

     # NOTE: This only relies on self.all_collidables.
    # TODO: Consider moving this into a base sprite class?
    def place_rect(self, rect):
        rect.topleft = (
            MARGIN.width  + randint(0, (GRID.width  - 1) * TILE.width),
            MARGIN.height + randint(0, (GRID.height - 1) * TILE.height)
        )
        other_rects = [s.rect for s in self.all_collidables.sprites()]
        while rect.collidelist(other_rects) > -1:
            rect.topleft = (
                MARGIN.width  + randint(0, (GRID.width  - 1) * TILE.width),
                MARGIN.height + randint(0, (GRID.height - 1) * TILE.height)
            )
        return rect

    def run(self):
        """Runs the main game loop.

        Note:
            Each iteration of this loop is called a frame.
        """
        # TODO: Encapsulate the stuff in this loop better.
        while True:
            # The event handling loop.
            for event in pygame.event.get():
                if event.type == QUIT:
                    return None
                elif event.type == SECOND_EVENT:
                    self.seconds_left -= 1
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:  # Left click.
                        self.player.input_comp.target_pos = event.pos
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return self.player.acorn_count
                    else:
                        for direction in ALL_DIRS:
                            if event.key in direction.keys:
                                self.player.input_comp.is_pressed[direction.index] = True
                elif event.type == KEYUP:
                    for direction in ALL_DIRS:
                        if event.key in direction.keys:
                            self.player.input_comp.is_pressed[direction.index] = False

            # Update all the things.
            if self.seconds_left == 0:
                return self.player.acorn_count
            self.player.update()
            for acorn in self.acorns.sprites():
                if self.player.hitbox.colliderect(acorn.rect):
                    self.player.acorn_count += 1
                    self.total_acorns -= 1
                    acorn.kill()
            if self.total_acorns < ACORN_LIMIT:
                if self.acorn_timer < 0:
                    Acorn(self.place_rect)
                    self.total_acorns += 1
                    self.acorn_timer = randint(MIN_ACORN_SPAWN * FPS,
                                          MAX_ACORN_SPAWN * FPS)
                else:
                    self.acorn_timer -= 1
            for nest in self.nests.sprites():
                if self.player.hitbox.colliderect(nest.rect):
                    nest.acorn_count += self.player.acorn_count
                    self.player.acorn_count = 0
                    nest.update()
            acorn_msg = "Collected acorns: {}".format(self.player.acorn_count)
            acorn_surf = self.msg_font.render(acorn_msg, True, FONT_COLOUR)
            minutes, seconds = divmod(self.seconds_left, 60)
            timer_msg = "{}:{:02d}".format(minutes, seconds)
            timer_surf = self.msg_font.render(timer_msg, True, FONT_COLOUR)
            timer_rect = timer_surf.get_rect()
            timer_rect.topright = (SCREEN.width, 0)

            # Draw all the things.
            self.screen_surf.fill(BKGD_COLOUR)
            self.all_tiles.draw(self.screen_surf)  # Tiles before other sprites.
            self.nests.draw(self.screen_surf)  # Nests before chipmunks.
            self.chipmunks.draw(self.screen_surf)
            self.acorns.draw(self.screen_surf)
            self.screen_surf.blit(acorn_surf, acorn_surf.get_rect())
            self.screen_surf.blit(timer_surf, timer_rect)

            # Render the screen.
            pygame.display.update()
            self.fps_clock.tick(FPS)

    def end_game(self, final_score):
        """The end game screen."""
        # Update all the things.
        end_font = pygame.font.SysFont(*END_FONT)
        message = "Game over! Final score: {0}".format(final_score)
        text_surf = end_font.render(message, True, FONT_COLOUR)
        text_rect = text_surf.get_rect()
        text_rect.center = (SCREEN.width // 2, SCREEN.height // 2)

        # Draw all the things.
        self.screen_surf.fill(BKGD_COLOUR)
        self.screen_surf.blit(text_surf, text_rect)

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
    world = World()
    score = world.run()
    if score is not None:
        world.end_game(score)

    # Close the window on terminating the main game loop.
    pygame.quit()