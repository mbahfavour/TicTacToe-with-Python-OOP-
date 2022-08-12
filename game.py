
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_game_winner = None
    

    def print_game_board(self):
        game_board = [self.board[r*3:(r+1)*3] for r in range(3)]
        for row in game_board :
            print(" |" + " |".join(row) + " |")

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(" |" + " |".join(row) + " |")

    def available_moves_left(self):
        available_moves = []

        for index, slot in enumerate(self.board):
            if slot == "":
                available_moves.append(index)
        return available_moves

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()

