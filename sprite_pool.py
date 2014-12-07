class SpritePool(object):
    def __init__(self, sprite_class,
                 input_comp, physics_comp, graphics_comp, place_rect):
        self._sprite_class = sprite_class
        self._input_comp = input_comp
        self._physics_comp = physics_comp
        self._graphics_comp = graphics_comp
        self._place_rect = place_rect
        self._pool = list()
        self.max_size = 0  # For logging purposes only. Not actually used.

    def check_out(self):
        if len(self._pool) > 0:
            sprite = self._pool.pop()
            print("[{}/{}] Reused a dead sprite.".format(len(self._pool),
                                                         self.max_size))
        else:
            self.max_size += 1
            sprite = self._sprite_class()
            print("[{}/{}] Created a new sprite.".format(len(self._pool),
                                                         self.max_size))

        sprite.revive(self._input_comp, self._physics_comp,
                      self._graphics_comp, self._place_rect)
        return sprite

    def check_in(self, sprite):
        sprite.kill()
        self._pool.append(sprite)