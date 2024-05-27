# import matplotlib.pyplot as plt
# import numpy as np 
# # def initial_state(x):
# #     if x == "s_0":
# #         return [0,0,0,0,0,0,0,0,0]
        

# # def initial_state():
# #     return ["0","0","0","0","0","0","0","0","0"]

# # def game_state():
# #     return ["o",0,"x","o","x",0,"x","o","x"]

# # def game_draw_state():
# #     return ["o",0,0,"o","x",0,"x","o","x"]


# # def game_draw_state():
# #     return ["o",0,0,"o","x",0,"x","o","x"]

# # def game_state_o():
# #     return ["x","o","o","o","x","o","x","x",0]

# # def game_state_x():
# #     return ["x","o","o","o","x","o","0","0","0"]

# class TicTacToe:
#     def __init__(self):
#         self.symbols = {'0': ' ', 'x': 'x', 'o': 'o'}

#     def initial_state(self):
#         return np.array([['x', 'o', 'x'], ['o', 'x', '0'], ['0', '0', 'o']])

#     def print_tic_tac_toe(self,board):
#         symbols = [self.symbols[item] for row in board for item in row]
#         print("\n")
#         print("\t     |     |")
#         print("\t  {}  |  {}  |  {}".format(symbols[0], symbols[1], symbols[2]))
#         print('\t_____|_____|_____')
#         print("\t     |     |")
#         print("\t  {}  |  {}  |  {}".format(symbols[3], symbols[4], symbols[5]))
#         print('\t_____|_____|_____')
#         print("\t     |     |")
#         print("\t  {}  |  {}  |  {}".format(symbols[6], symbols[7], symbols[8]))
#         print("\t     |     |")
#         print("\n")

#     def player_turn(self,board):
    
#         x_count = np.count_nonzero(board == 'x')
#         o_count = np.count_nonzero(board == 'o')

#         return 'x' if x_count == o_count else 'o'
    

#         # if x_value == o_value:
#         #     return "x"
#         # elif x_value > o_value:
#         #     return "o"
#         # else:
#         #     return "x"
#         # x_value = np.count_nonzero(board == "x")
#         # # np.count_nonzero(y == 1)
#         # o_value = np.count_nonzero(board == "o")
#         # # o_value = board.count("o")

#         # if x_value and o_value is None or x_value == o_value:
#         #     return "x"
#         # elif x_value > o_value:
#         #     return "o"
#         # else:
#         #     return "x"
        
#     # player_turn(np_game_state)

#     def actions(self,board):
#         return np.argwhere(board == '0')
#         # list_actions = []
#         # for i,value in enumerate(board):
#         #     if value == 0:
#         #         list_actions.append(i)
#         # return print(list_actions)
        

#     #actions(np_game_state)



#     def checkRows(self,board):
#         for row in board:
#             if len(set(row)) == 1:
#                 return row[0]
#         return 0

#     def checkDiagonals(self,board):
#         if len(set([board[i][i] for i in range(len(board))])) == 1:
#             return board[0][0]
#         if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
#             return board[0][len(board)-1]
#         return 0


#     def checkWin(self,board):
#         #transposition to check rows, then columns
#         for newBoard in [board, np.transpose(board)]:
#             result = self.checkRows(newBoard)
#             if result:
#                 return result
#         return self.checkDiagonals(board)

#     # temp_arr = np.asarray(game_state_1())
#     # board  = temp_arr.reshape(3,3)

#     # print(checkWin(np_game_state))

#     def results(self, board, action, player):

#         new_board = board.copy()
#         new_board[action] = player
#         # print(board)
#         return new_board
    
#     def terminals(self,board):
#         board = board[board != 0]
        
#         if len(board) == 9 or self.checkWin(board) == "x" or self.checkWin(board) == "o":
#             return True
#         return False
    
#     def utilitys(self,board):
    
#         win = self.checkWin(board)
#         if win == "x":
#             return 1
#         elif win == "o":
#             return -1
#         else:
#             return 0
    
#     def minimax(self, board, player):
    
#         if self.terminals(board) == True :
#             return self.utilitys(board), None
        
#         if player == 'x':
#             max_Eval = float('-inf')
#             best_move = None
#             # legal_moves = actions(board)
#             #if self.actions is not None:
#             for action in self.actions(board):
#                 # Make the move 
#                 new_board = self.results(board,action,player)
#                 score, _ = self.minimax(new_board, 'o') 
#                 # Debemos regresar el movimiento y el mejor movimiento 
#                 if score > max_Eval:
#                     max_Eval, best_move = score, action

#             return max_Eval, best_move
#         else: 
#             min_Eval = float('inf')
#             best_move = None
#             # legal_moves = actions(board)
#             #if self.actions is not None:
#             for action in self.actions(board):
#                 # Make the move 
#                 new_board = self.results(board,action,player)
#                 score, _ = self.minimax(new_board, 'x') 
#                 # Debemos regresar el movimiento y el mejor movimiento 
#                 if score < min_Eval:
#                     min_Eval, best_move = score, action

#             return min_Eval, best_move
        
#     def best_move(self, board):
#         _ , move = self.minimax(board, self.player_turn(board))
#         return move
    
# bot = TicTacToe()
# initial_board = bot.initial_state()
# bot.print_tic_tac_toe(initial_board)
# move = bot.best_move(initial_board)
# print(f"Best move for '{bot.player_turn(initial_board)}':", move)

import matplotlib.pyplot as plt
import numpy as np 


class TicTacToe:
    def __init__(self):
        self.symbols = {'0': ' ', 'x': 'x', 'o': 'o'}
        self.board = self.initial_state()  # Store the board as an instance variable

    def initial_state(self):
        return np.array([['o', 'o', 'o'], ['0', 'x', '0'], ['x', '0', 'x']])

    def print_tic_tac_toe(self):
        symbols = [self.symbols[item] for row in self.board for item in row]
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

    def player_turn(self):
        x_count = np.count_nonzero(self.board == 'x')
        o_count = np.count_nonzero(self.board == 'o')
        return 'x' if x_count == o_count else 'o'

    def actions(self):
        return list(zip(*np.where(self.board == '0')))

    def results(self, action, player):
        self.board[action] = player  # Update the board directly

    # Cambiar funcion de ganador
    # def checkRows(self):
    #     for row in self.board:
    #         if len(set(row)) == 1 and row[0] != '0':
    #             return row[0]
    #     return None

    # def checkDiagonals(self):
    #     # main diagonal
    #     if len(set([self.board[i][i] for i in range(len(self.board))])) == 1 and self.board[0][0] != '0':
    #         return self.board[0][0]
    #     # second diagonal
    #     if len(set(self.board[i][len(self.board)-i-1] for i in range(len(self.board)))) == 1 and self.board[0][len(self.board)-1] != '0':
    #         return self.board[0][len(self.board)-1]
    #     return None

    # def checkWin(self):
    #     #transposition to check rows, then columns
    #     for newBoard in [self.board, np.transpose(self.board)]:
    #         result = self.checkRows()
    #         if result:
    #             return result
    #     return self.checkDiagonals()
    def checkRows(self):
        for row in self.board:
            print("Checking row:", row)  # Debug statement
            if len(set(row)) == 1 and row[0] != '0':
                return row[0]
        return None

    def checkDiagonals(self):
        # Main diagonal
        main_diag = [self.board[i][i] for i in range(len(self.board))]
        print("Checking main diagonal:", main_diag)  # Debug statement
        if len(set(main_diag)) == 1 and self.board[0][0] != '0':
            return self.board[0][0]

        # Second diagonal
        sec_diag = [self.board[i][len(self.board)-i-1] for i in range(len(self.board))]
        print("Checking second diagonal:", sec_diag)  # Debug statement
        if len(set(sec_diag)) == 1 and self.board[0][len(self.board)-1] != '0':
            return self.board[0][len(self.board)-1]

        return None

    def checkWin(self):
        # Check original rows
        result = self.checkRows()
        if result:
            return result
        
        # Check columns (as rows of the transposed board)
        transposed_board = np.transpose(self.board)
        print("Board being checked (transposed):", transposed_board)  # Debug statement
        for row in transposed_board:
            print("Checking transposed row:", row)  # Debug statement
            if len(set(row)) == 1 and row[0] != '0':
                return row[0]
        
        # Check diagonals
        return self.checkDiagonals()


    def terminals(self):
        winner = self.checkWin()
            
        if winner or np.count_nonzero(self.board == '0') == 0:  # Check if someone has won or the board is full
            return True
        return False
    
    def utility(self):
        win = self.checkWin()
        if win == "x":
            return 1
        elif win == "o":
            return -1
        else:
            return 0

    def minimax(self, player):
        if self.terminals():
            return self.utility(), None
        
        if player == 'x':
            max_eval = float('-inf')
            best_move = None
            for action in self.actions():
                new_board = np.copy(self.board)
                self.results(action, player)
                score, _ = self.minimax('o')
                self.board = new_board  # Restore the board
                if score > max_eval:
                    max_eval, best_move = score, action
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for action in self.actions():
                new_board = np.copy(self.board)
                self.results(action, player)
                score, _ = self.minimax('x')
                self.board = new_board  # Restore the board
                if score < min_eval:
                    min_eval, best_move = score, action
            return min_eval, best_move
        
    def best_move(self):
        return self.minimax(self.player_turn())[1]
    
bot = TicTacToe()
bot.print_tic_tac_toe()
winner = bot.checkWin()
print("Winner is:", winner)


