class Player:
    def __init__(self):
        self.tally = 0
        self.gesture = ''
        self.list = ["rock", "paper", "scissors", "lizard", "spock"]

    def user_input(self):
        self.gesture = input("Choose your gesture: ").lower()
        while True:
            if self.gesture in self.list:
                return self.gesture
            else:
                self.gesture = input("Your choice is not an option. Please choose Rock, Paper, Scissors, Lizard, or Spock.").lower()



