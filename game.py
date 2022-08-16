from human import Human
from ai import Ai

class Game:
    def __init__(self):
        pass

    def welcome_player(self):
        pass

    def instructions(self):
        pass

    def game_mode(self):
        number_of_players = int(input("How many players?"))
        while True:
            if number_of_players == 1:
                self.player_one = Ai()
                self.player_two = Human()
                break
            elif number_of_players == 2:
                self.player_one = Human()
                self.player_two = Human()
                break
            else:
                number_of_players = int(input("Enter 1 or 2 for number of players."))

    def run_game(self):
        self.game_mode()
        self.game_round()

    def game_round(self):
        self.player_one.user_input()
        self.player_two.user_input()

    def display_winner(self):
        pass