from physics_component import PhysicsComponent
from settings import CHIP_HITBOX


class ChipmunkPhysicsComponent(PhysicsComponent):
    def __init__(self):
        super().__init__(CHIP_HITBOX)

    def update(self, chipmunk, world):
        """Updates the chipmunk's position and throws an acorn."""
        super().update(chipmunk, world)

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

        # Throw an acorn.
        # throw_pos = chipmunk.throw_pos
        # if throw_pos:
        #     acorn = world.acorn_pool.check_out()
        #     acorn.rect.center = chipmunk.rect.center
        #     acorn.input_comp.next_pos = throw_pos