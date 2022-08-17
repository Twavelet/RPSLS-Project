from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def user_input(self):
        self.gesture = input("Choose your gesture: ").lower()

    

        




