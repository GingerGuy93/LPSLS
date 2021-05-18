
from player import *
from human import *
from ai import *
import time


class PlayGame:
    def __init__(self):
        self.run = True
        self.rounds = 0
        self.player_1 = None
        self.player_2 = None
        self.rock = Rock()
        self.paper = Paper()
        self.scissor = Scissor()
        self.lizard = Lizard()
        self.spock = Spock()
        self.gestures = [self.rock, self.paper, self.scissor, self.lizard, self.spock]

    def start_game(self):
        self.welcome()
        self.run = True
        while self.run == True:
            self.current_round()
            self.winner()

    def welcome(self):
        print("Welcome to the Thunderdome!")
        print()
        time.sleep(3)
        print("Today we will be playing the glorious game of rock, paper, scissors, lizard, spock")
        print()
        time.sleep(3)
        print("The rules are simple")
        print()
        time.sleep(1)
        print("There are 5 choices to choose from, the goal is to beat your opponent with a gesture that beats theirs")
        print()
        time.sleep(3)
        print("Rock beats scissors and lizard")
        print("Paper beats spock and rock")
        print("Scissors beats paper and lizard")
        print("Lizard beats spock and paper")
        print("Spock beats scissors and rock")
        print()
        time.sleep(3)
        players = int(input('How many people are playing? 1 or 2?:'))
        if players == 1:
            self.player_1 = Human()
            self.player_1.user_name()
            print(f"Player 1's name is: {self.player_1.name}")
            self.player_2 = Computer()
        else:
            self.player_1 = Human()
            self.player_1.user_name()
            print(f"Player 1's name is: {self.player_1.name}")
            print()
            self.player_2 = Human()
            self.player_2.user_name()
            print(f"Player 2's name is: {self.player_2.name}")
            print()

    def player1_choice(self):
        valid = False
        while valid == False:
            player1_gesture = int(input('Choose a gesture to use this round Rock = 0, Paper = 1, Scissors = 2, '
                                        'Lizard = 3, Spock = 4: '))
            if player1_gesture != 0 and player1_gesture != 1 and player1_gesture != 2 and player1_gesture !=3 and player1_gesture != 4:
                print("Please enter a valid input!")
            else:
                valid = True
            gesture_chosen = self.gestures[player1_gesture]
            return gesture_chosen

    def player2_choice(self):
        if self.player_2.name == 'AI':
            player_2_choice = random.randint(0, 4)
            gesture_chosen = self.gestures[player_2_choice]
            return gesture_chosen
        else:
            valid = False
            while valid == False:
                player2_gesture = int(input('Choose a gesture to use this round Rock = 0, Paper = 1, Scissors = 2, '
                                            'Lizard = 3, Spock = 4: '))
                if player2_gesture != 0 and player2_gesture != 1 and player2_gesture != 2 and player2_gesture != 3 \
                        and player2_gesture != 4:
                    print("Please enter a valid input!")
                else:
                    valid = True
                gesture_chosen = self.gestures[player2_gesture]
                return gesture_chosen

    def current_round(self):
        p1_gesture = self.player1_choice()
        p2_gesture = self.player2_choice()

        if p1_gesture == p2_gesture:
            print("TIE, TRY AGAIN!")
            self.rounds += 1
        elif p2_gesture in self.player_1.wins_against:
            print(f"{self.player_1.name} Wins this round!")
            self.rounds += 1
            self.player_1.score += 1
        else:
            print(f"{self.player_2.name} Wins this round!")
            self.rounds += 1
            self.player_2.score += 1

    def winner(self):
        if self.player_1.score == 3:
            print(f"{self.player_1.name} Beat {self.player_2.name}")
        elif self.player_2.score == 3:
            print(f"{self.player_2.name} Beat {self.player_1.name}")

    def rematch(self):
        validation = input("Would you like to rematch?")
        if validation == "y":
            self.player_1.score = 0
            self.player_2.score = 0
        else:
            self.run = False
