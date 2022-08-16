from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.second_player = random.choice(gestures_list)