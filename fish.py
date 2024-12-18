from ursina import *
import random

class Fish:
    def __init__(self, position=(0, 0, 0)):
        self.entity = entity(
            model='sphere',
            color=color.blue
            scale=0.3,
            position=position
        )

        def respawn(self):
            self.entity.position = (random.uniform(-3, 3), -2, 0)