from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def user_name(self):
        name = input("Please enter your name:")
        self.name = name


