import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_next_move(self, game):
        pass


class ComputerPlayer:
    def __init__(self, letter):
        super.__init__(letter)

    def get_next_move(self, game):
        square = random.choice(game.available_next_moves())
        return square


class HumanPlayer:
    def __init(self, letter):
        super.__init__(letter)

    def get_next_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + "\s turn. Input moves between 0 to 9:")
            try:
                val = int(square)
                if value not in game.avaailable_next_moves():
                    raise ValueError
            except ValueError:
                print("Invalid Square. Try Again")