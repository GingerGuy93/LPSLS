class Player:
    def __init__(self):
        self.name = ""
        self.score = 0


class Rock:
    def __init__(self):
        self.name = "rock"
        self.wins_against = ['lizard', 'scissors']


class Paper:
    def __init__(self):
        self.name = "paper"
        self.wins_against = ['spock', 'rock']


class Scissor:
    def __init__(self):
        self.name = "scissor"
        self.wins_against = ['lizard', 'paper']


class Lizard:
    def __init__(self):
        self.name = "lizard"
        self.wins_against = ['spock', 'paper']


class Spock:
    def __init__(self):
        self.name = 'spock'
        self.wins_against = ['scissors', 'rock']

