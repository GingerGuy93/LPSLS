import random
from player import Player
from human import Human
from ai import Computer


class PlayGame:
    def __init__(self):
        self.round = 0
        self.player_1 = None
        self.player_2 = None
        self.run = False


