from player import Player
import random


class Ai(Player):
    def __init__(self):
        super().__init__()


    def user_input(self):
        self.gesture = random.choice(self.list).lower()