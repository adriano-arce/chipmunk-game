from pygame.rect import Rect
from settings import CHIP_HITBOX


class PhysicsComponent(object):
    def __init__(self):
        self.hitbox = Rect((0, 0), CHIP_HITBOX)

    def update(self, chipmunk, world):
        """Updates the chipmunk's position and throws an acorn."""
        (dx, dy) = chipmunk.velocity
        wall_rects = [w.rect for w in world.wall_tiles]
        self.move(dx, dy, chipmunk.rect, wall_rects)

        # Check for acorn collisions.
        for acorn in world.acorns:
            if self.hitbox.colliderect(acorn.rect):
                chipmunk.acorn_count += 1
                world.acorn_pool.check_in(acorn)

        # Check for nest collisions.
        for nest in world.nests:
            if self.hitbox.colliderect(nest.rect):
                nest.acorn_count += chipmunk.acorn_count
                chipmunk.acorn_count = 0
                nest.update()

        # TODO: Make the components abstract. Reuse for both chipmunks/acorns.
        # acorn = world.acorn_pool.check_out()
        # self.throw(acorn, chipmunk.throw_pos)

    def move(self, dx, dy, rect, wall_rects):
        """Moves each axis separately, checking for wall collisions twice."""
        if dx != 0:
            self.move_single_axis(dx, 0, rect, wall_rects)
        if dy != 0:
            self.move_single_axis(0, dy, rect, wall_rects)

    def move_single_axis(self, dx, dy, rect, wall_rects):
        """Moves the rect in a single axis, checking for collisions."""
        rect.move_ip(dx, dy)
        self.hitbox.midbottom = rect.midbottom

        indices = self.hitbox.collidelistall(wall_rects)
        if indices:  # There was a collision.
            other_rects = (wall_rects[i] for i in indices)
            if dx > 0:
                self.hitbox.right = min(r.left for r in other_rects)
            if dx < 0:
                self.hitbox.left = max(r.right for r in other_rects)
            if dy > 0:
                self.hitbox.bottom = min(r.top for r in other_rects)
            if dy < 0:
                self.hitbox.top = max(r.bottom for r in other_rects)

        rect.midbottom = self.hitbox.midbottom

    def throw(self, acorn, throw_pos):
        pass