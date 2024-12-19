from ursina import *
class Rod:
    def __init__(self, position=(0, 0, 0)):
        self.entity = entity(
            model='cube'
            color=color.orange,
            scale=(0.2, 1, 0.2),
            position=position
        )

def move(self):
    self.entity.x += held_keys['d'] * 0.05
    self.entity.x += held_keys['a'] * 0.05
