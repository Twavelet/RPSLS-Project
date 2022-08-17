from human import Human
from ai import Ai

class Game:
    def __init__(self):
        pass

    def welcome_player(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def instructions(self):
        print("Choose numbers of players you would like to have (1/2)")
        print(f"Each player will choose either Rock, Paper, Scissors, Lizard, or Spock.")

    def game_mode(self):
        number_of_players = int(input("How many players? "))
        while True:
            if number_of_players == 1:
                self.player_one = Ai()
                self.player_two = Human()
                print("You are Player Two.")
                break
            elif number_of_players == 2:
                self.player_one = Human()
                self.player_two = Human()
                break
            else:
                number_of_players = int(input("Enter 1 or 2 for number of players: "))

    def run_game(self):
        self.welcome_player()
        self.instructions()
        self.game_mode()
        self.game_round()
        self.display_winner()
        

    def game_round(self):
        while True:
            if self.player_one.tally < 2 and self.player_two.tally < 2:
                self.player_one.user_input()
                self.player_two.user_input()
                self.comparison()
            else:
                break
                
    def comparison(self):
        if self.player_one.gesture == self.player_two.gesture:
            print("Tie. Play again.")

        elif self.player_one.gesture == "rock":
            if self.player_two.gesture == "scissors" or self.player_two.gesture == "lizard":
                self.player_one.tally += 1
                print(f"rock beats {self.player_two.gesture}, player one wins")
            else:
                self.player_two.tally += 1
                print(f"{self.player_two.gesture} beats rock, player two wins!")

        elif self.player_one.gesture == "scissors":
            if self.player_two.gesture =="paper" or self.player_two.gesture == "lizard":
                self.player_one.tally += 1
                print(f"scissors beats {self.player_two.gesture}, player one wins")
            else:
                self.player_two.tally += 1
                print(f"{self.player_two.gesture} beats scissors, player two wins!")

        elif self.player_one.gesture == "paper":
            if self.player_two.gesture == "rock" or self.player_two.gesture == "spock":
                self.player_one.tally += 1
                print(f"Paper beats {self.player_two.gesture}, player one wins")
            else:
                self.player_two.tally += 1
                print(f"{self.player_two.gesture} beats paper, player two wins!")

        elif self.player_one.gesture == "lizard":
            if self.player_two.gesture == "paper" or self.player_two.gesture == "spock":
                self.player_one.tally += 1
                print(f"Lizard beats {self.player_two.gesture}, player one wins")
            else:
                self.player_two.tally += 1
                print(f"{self.player_two.gesture} beats lizard, player two wins!")

        elif self.player_one.gesture == "spock":
            if self.player_two.gesture == "scissors" or self.player_two.gesture == "rock":
                self.player_one.tally += 1
                print(f"Spock beats {self.player_two.gesture}, player one wins")
            else:
                self.player_two.tally += 1
                print(f"{self.player_two.gesture} beats spock, player two wins!")    

    def display_winner(self):
        if self.player_one.tally > self.player_two.tally:
            print("Player One Wins!")
        else:
            print("Player Two Wins!")