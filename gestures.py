

class Gestures:
    def __init__(self):
        self.list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def comparison(self, player_one, player_two):
        if player_one.gesture == player_two.gesture:
            print("Tie. Play again.")

        elif player_one.gesture == "rock":
            if player_two.gesture == "scissors" or player_two.gesture == "lizard":
                player_one.tally += 1
                print(f"rock beats {player_two.gesture}, player one wins")
            else:
                player_two.tally += 1
                print(f"{player_two.gesture} beats rock, player 2 wins!")

        elif player_one.gesture == "scissors":
            if player_two.gesture =="paper" or player_two.gesture == "lizard":
                player_one.tally += 1
                print(f"scissors beats {player_two.gesture}, player one wins")
            else:
                player_two.tally += 1
                print(f"{player_two.gesture} beats scissors, player 2 wins!")

        elif player_one.gesture == "paper":
            if player_two.gesture == "rock" or player_two.gesture == "spock":
                player_one.tally += 1
                print(f"Paper beats {player_two.gesture}, player one wins")
            else:
                player_two.tally += 1
                print(f"{player_two.gesture} beats paper, player 2 wins!")

        elif player_one.gesture == "lizard":
            if player_two.gesture == "paper" or player_two.gesture == "spock":
                player_one.tally += 1
                print(f"Lizard beats {player_two.gesture}, player one wins")
            else:
                player_two.tally += 1
                print(f"{player_two.gesture} beats lizard, player two wins!")

        elif player_one.gesture == "spock":
            if player_two.gesture == "scissors" or player_two.gesture == "rock":
                player_one.tally += 1
                print(f"Spock beats {player_two.gesture}, player one wins")
            else:
                player_two.tally += 1
                print(f"{player_two.gesture} beats spock, player two wins!")