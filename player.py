class Player:
    def __init__(self, gesture):
        self.name = ""
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.chosen_gesture = gesture

    def win(self):
        self.score += 1

