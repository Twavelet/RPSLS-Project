from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()


    def user_input(self):
        self.gesture = input("Choose")
        self.gesture2 = random.choice(gestures_list)