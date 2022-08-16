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
        number_of_players = input("How many players?")
        while True:
            if number_of_players == 1:
                player_one = Ai()
            elif number_of_players == 2:
                player_one = Human()
            else:
                input("Enter 1 or 2 for number of players.")

    def run_game(self):
        pass

    def game_round(self):
        pass

    def display_winner(self):
        pass