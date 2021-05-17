from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.chosen_gesture = input(f'Please select a chosen gesture to use this round {self.gestures}')
