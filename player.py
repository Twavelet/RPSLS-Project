class Player:
    def __init__(self):
        self.name = ""
        self.count = 0

    def user_input(self):
        self.first_player = input("What would you like to choose?")
        self.second_player = input("what would you like to choose?")