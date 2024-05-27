import numpy as np

class TicTacToeBot:
    def __init__(self):
        self.symbols = {'0': ' ', 'x': 'x', 'o': 'o'}

    def initial_state(self):
        return np.array([['x', 'o', 'x'], ['o', 'x', '0'], ['0', '0', 'o']])

    def print_board(self, board):
        symbols = [self.symbols[item] for row in board for item in row]
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(symbols[0], symbols[1], symbols[2]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(symbols[3], symbols[4], symbols[5]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(symbols[6], symbols[7], symbols[8]))
        print("\t     |     |")
        print("\n")

    def player_turn(self, board):
        x_count = np.count_nonzero(board == 'x')
        o_count = np.count_nonzero(board == 'o')
        return 'x' if x_count == o_count else 'o'

    def actions(self, board):
        return list(zip(*np.where(board == '0')))

    def result(self, board, action, player):
        new_board = np.copy(board)
        new_board[action] = player
        return new_board

    def winner(self, board):
        # Check rows, columns, and diagonals
        lines = list(board) + list(board.T) + [np.diag(board), np.diag(np.fliplr(board))]
        for line in lines:
            if len(set(line)) == 1 and line[0] != '0':
                return line[0]
        return None

    #If the game is over retrieve True or False
    def terminal(self, board):
        return self.winner(board) is not None or np.all(board != '0')

    def utility(self, board):
        win = self.winner(board)
        if win == 'x':
            return 1
        elif win == 'o':
            return -1
        else:
            return 0

    def minimax(self, board, player):
        if self.terminal(board):
            return self.utility(board), None

        if player == 'x':
            value = float('-inf')
            best_move = None
            for action in self.actions(board):
                new_board = self.result(board, action, player)
                score, _ = self.minimax(new_board, 'o')
                if score > value:
                    value, best_move = score, action
            return value, best_move
        else:
            value = float('inf')
            best_move = None
            for action in self.actions(board):
                new_board = self.result(board, action, player)
                score, _ = self.minimax(new_board, 'x')
                if score < value:
                    value, best_move = score, action
            return value, best_move

    def best_move(self, board):
        _, move = self.minimax(board, self.player_turn(board))
        return move

# Example usage
bot = TicTacToeBot()
initial_board = bot.initial_state()
bot.print_board(initial_board)
move = bot.best_move(initial_board)
print(f"Best move for '{bot.player_turn(initial_board)}':", move)

