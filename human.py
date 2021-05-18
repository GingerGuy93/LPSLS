from player import Player
from player import Rock
from player import Paper
from player import Scissor
from player import Lizard
from player import Spock


class Human(Player, Rock, Paper, Scissor, Lizard, Spock):
    def __init__(self):
        super().__init__()

    def user_name(self):
        name = input("Please enter your name:")
        self.name = name


