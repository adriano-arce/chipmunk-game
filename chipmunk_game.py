from enum import Enum
from random import randint

import pygame

from acorn import Acorn
from chipmunk import Chipmunk
from nest import Nest
from settings import *
from sprite_pool import SpritePool
from tile import Wall, Floor


# noinspection PyArgumentList
WorldMode = Enum("WorldMode", "run, end, quit")


class World(object):
    def __init__(self):
        pygame.init()
        self.mode = WorldMode.run

        # Icon should be loaded before mode is set.
        icon = pygame.image.load("imgs/fake-icon.png")
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

        # Set up acorn and player stuff.
        self.acorn_pool = SpritePool(Acorn, self.place_rect)
        self.acorn_timer = randint(MIN_ACORN_SPAWN * FPS, MAX_ACORN_SPAWN * FPS)
        self.player = Chipmunk(self.place_rect)
        for __ in range(ACORN_INIT_COUNT):
            self.acorn_pool.check_out()

        # Set up timing stuff.
        self.seconds_left = GAME_LENGTH
        pygame.time.set_timer(SECOND_EVENT, 1000)

        # TODO: Encapsulate this part.
        self.acorn_msg = "Collected acorns: {}".format(self.player.acorn_count)
        self.acorn_surf = self.msg_font.render(self.acorn_msg, True, FONT_COLOUR)
        self.timer_msg = "{}:{:02d}".format(*divmod(self.seconds_left, 60))
        self.timer_surf = self.msg_font.render(self.timer_msg, True, FONT_COLOUR)
        self.timer_rect = self.timer_surf.get_rect()

    def place_rect(self, rect):
        """Randomly places the rect in the world in some valid tile."""
        rect.topleft = (
            MARGIN.width  + randint(0, (GRID.width  - 1) * TILE.width),
            MARGIN.height + randint(0, (GRID.height - 1) * TILE.height)
        )
        other_rects = [s.rect for s in self.all_collidables]
        while rect.collidelist(other_rects) > -1:
            rect.topleft = (
                MARGIN.width  + randint(0, (GRID.width  - 1) * TILE.width),
                MARGIN.height + randint(0, (GRID.height - 1) * TILE.height)
            )
        return rect

    def handle_events(self):
        """Handles the events."""
        player_input = self.player.input_comp
        for event in pygame.event.get():
            if event.type == QUIT:
                self.mode = WorldMode.quit
            elif event.type == SECOND_EVENT:
                self.seconds_left -= 1
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:  # Left click for moving.
                    player_input.next_pos = event.pos
                elif event.button == 3:  # Right click for throwing.
                    self.player.throw_pos = event.pos
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.mode = WorldMode.end
                else:
                    for direction in ALL_DIRS:
                        if event.key in direction.keys:
                            player_input.is_pressed[direction.index] = True
            elif event.type == KEYUP:
                for direction in ALL_DIRS:
                    if event.key in direction.keys:
                        player_input.is_pressed[direction.index] = False

    def update(self):
        """Updates all the things."""
        # TODO: Should we measure seconds_left & acorn_timer in frames or secs?
        if self.seconds_left == 0:
            self.mode = WorldMode.end

        self.player.update(self)

        # Update all acorns (in case the player threw any).
        self.acorns.update(self)

        # TODO: Encapsulate this.
        if len(self.acorns) < ACORN_LIMIT:
            if self.acorn_timer < 0:
                self.acorn_pool.check_out()
                self.acorn_timer = randint(MIN_ACORN_SPAWN * FPS,
                                           MAX_ACORN_SPAWN * FPS)
            else:
                self.acorn_timer -= 1

        # TODO: Encapsulate this.
        self.acorn_msg = "Collected acorns: {}".format(self.player.acorn_count)
        self.acorn_surf = self.msg_font.render(self.acorn_msg, True, FONT_COLOUR)
        self.timer_msg = "{}:{:02d}".format(*divmod(self.seconds_left, 60))
        self.timer_surf = self.msg_font.render(self.timer_msg, True, FONT_COLOUR)
        self.timer_rect = self.timer_surf.get_rect()
        self.timer_rect.topright = (SCREEN.width, 0)

    def draw(self):
        """Draws all the things."""
        self.screen_surf.fill(BKGD_COLOUR)
        self.all_tiles.draw(self.screen_surf)  # Tiles before other sprites.
        self.nests.draw(self.screen_surf)  # Nests before chipmunks.
        self.chipmunks.draw(self.screen_surf)
        self.acorns.draw(self.screen_surf)
        self.screen_surf.blit(self.acorn_surf, self.acorn_surf.get_rect())
        self.screen_surf.blit(self.timer_surf, self.timer_rect)

    def run(self):
        """Runs the main game loop.

        Note:
            Each iteration of this loop is called a frame.
        """
        while self.mode is WorldMode.run:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.fps_clock.tick(FPS)

    def end(self):
        """Displays the end game screen."""
        # Update all the things.
        end_font = pygame.font.SysFont(*END_FONT)
        final_score = self.player.nest.acorn_count
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
        while self.mode is WorldMode.end:
            self.handle_events()

if __name__ == "__main__":
    world = World()
    world.run()
    if world.mode is WorldMode.end:
        world.end()
    pygame.quit()