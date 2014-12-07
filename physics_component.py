from pygame.rect import Rect


class PhysicsComponent(object):
    def __init__(self, hitbox_size):
        self.hitbox = Rect((0, 0), hitbox_size)

    def update(self, sprite, world):
        """Updates the sprite's position."""
        (dx, dy) = sprite.velocity
        wall_rects = [w.rect for w in world.wall_tiles]
        self.move(dx, dy, sprite.rect, wall_rects)

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