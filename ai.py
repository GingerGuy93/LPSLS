from player import Player
import random


class Computer(Player):

    def __init__(self):
        super().__init__()
        self.name = "AI"
        self.score = 0
