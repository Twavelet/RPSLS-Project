from player import Player
import random
from gestures import Gestures


class Ai(Player):
    def __init__(self):
        super().__init__()
        self.list = Gestures()


    def user_input(self):
        self.gesture = random.choice(self.list.list)