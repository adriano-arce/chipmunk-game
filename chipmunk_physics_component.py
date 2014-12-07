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

        # TODO: Make the components abstract. Reuse for both chipmunks/acorns.
        # acorn = world.acorn_pool.check_out()
        # self.throw(acorn, chipmunk.throw_pos)