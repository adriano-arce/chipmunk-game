class SpritePool(object):
    def __init__(self, sprite_class, place_rect):
        self._sprite_class = sprite_class
        self._place_rect = place_rect
        self._pool = list()
        # self._max_size = 0  # For logging purposes only. Not actually used.

    def check_out(self):
        """Checks out a freshly revived sprite.

        Returns:
            A freshly revived sprite.
        """
        if self._pool:
            sprite = self._pool.pop()
            # print("[{}/{}] Reused a dead sprite.".format(len(self._pool),
            #                                              self._max_size))
        else:
            sprite = self._sprite_class()
            # self._max_size += 1
            # print("[{}/{}] Created a new sprite.".format(len(self._pool),
            #                                              self._max_size))

        sprite.revive(self._place_rect)
        return sprite

    def check_in(self, sprite):
        """Kills then checks in the given sprite to the sprite pool."""
        sprite.kill()
        self._pool.append(sprite)