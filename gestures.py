

class Gestures:
    def __init__(self):
        pass

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