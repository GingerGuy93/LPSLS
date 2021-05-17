from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.gesture = random.choice(self.gestures)