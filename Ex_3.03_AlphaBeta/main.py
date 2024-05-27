import matplotlib.pyplot as plt
import numpy as np 


class TicTacToe:
    def __init__(self):
        self.symbols = {'0': ' ', 'x': 'x', 'o': 'o'}
        self.board = self.initial_state()  # Store the board as an instance variable

    def initial_state(self):
        return np.array([['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']])

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

    def checkRows(self):
        for row in self.board:
            #print("Checking row:", row)  # Debug statement
            if len(set(row)) == 1 and row[0] != '0':
                return row[0]
        return None

    def checkDiagonals(self):
        # Main diagonal
        main_diag = [self.board[i][i] for i in range(len(self.board))]
        #print("Checking main diagonal:", main_diag)  # Debug statement
        if len(set(main_diag)) == 1 and self.board[0][0] != '0':
            return self.board[0][0]

        # Second diagonal
        sec_diag = [self.board[i][len(self.board)-i-1] for i in range(len(self.board))]
        
        if len(set(sec_diag)) == 1 and self.board[0][len(self.board)-1] != '0':
            return self.board[0][len(self.board)-1]

        return None

    def checkWin(self):
        # check original rows if someone has won
        result = self.checkRows()
        if result:
            return result
        
        # check columns as rows of the transposed board
        transposed_board = np.transpose(self.board)
        
        for row in transposed_board:
            
            if len(set(row)) == 1 and row[0] != '0':
                return row[0]
        
        # Check diagonals
        return self.checkDiagonals()

    def terminals(self):
        winner = self.checkWin()
            
        if winner or np.count_nonzero(self.board == '0') == 0:  # check if someone has won or the board is full
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

        if self.terminals(): # firts check is game is over
            return self.utility(), None # just return the utility of it
        
        if player == 'x': # in case of player is x we start here
            max_eval = float('-inf') # this is the same as - x number but a little bit more complex 
            best_move = None # declare our best_move as None to use it in our for loop
            for action in self.actions(): # with self.actions() we get our posible actions in that position 
                new_board = np.copy(self.board) # i get a copy of the board to work on it
                self.results(action, player) # now, we apply the move for that use results is that transition results(action, player)
                score, _ = self.minimax('o') # we do a recursion run and just save score, the only thing we need but now for the other player
                self.board = new_board  # restore the board in our local board as self.board
                if score > max_eval: # the most complex thing and hard to get to is compare the score to the max_eval and replace them, to get te max values in this case
                    max_eval, best_move = score, action
            return max_eval, best_move
        else: # in case of player is o we start here
            min_eval = float('inf') # this is the same as - x number but a little bit more complex 
            best_move = None # declare our best_move as None to use it in our for loop
            for action in self.actions():  # with self.actions() we get our posible actions in that position 
                new_board = np.copy(self.board) # i get a copy of the board to work on it
                self.results(action, player) # now, we apply the move for that use results is that transition results(action, player)
                score, _ = self.minimax('x') # we do a recursion run and just save score, the only thing we need but now for the other player
                self.board = new_board  # restore the board in our local board as self.board
                if score < min_eval: # the most complex thing and hard to get to is compare the score to the max_eval and replace them, to get te min values in this case now is min
                    min_eval, best_move = score, action
            return min_eval, best_move # and finally just return those values
        
    def best_move(self): # in order to get the best move we use this funtion to call our minimax function
        return self.minimax(self.player_turn())[1] # and just return the call of the information of player turn, our only parameter and just get the second parameter which is just the best move
    
# initilize the bot    
bot = TicTacToe()
player_var = str(input("Which player want to be, enter 'x' or 'o', please enter in lowercase -> "))


if player_var == 'x':
    while bot.terminals() == False:
        
        print(f"Enter your movement one digit at a time for '{bot.player_turn()}'")
        try:
            x_1 = int(input("Enter the row index:"))
            x_2 = int(input("Enter the column index:"))
            if bot.board[x_1,x_2] == '0':
                bot.results((x_1,x_2),bot.player_turn())
                bot.print_tic_tac_toe()
                break
                
        except ValueError:
            print("Invalid input! Please enter numeric indices.")
        except IndexError:
            print("Index out of bounds! Please enter correct indices.")

        # Necesitaremos checar despues de haber introducido nuestro ultimo moviemiento en caso de estar en el
        # 
        if bot.terminals():
            break
        
        move = bot.best_move()
        print(f"Best move for '{bot.player_turn()}':", move)
        bot.results(move ,bot.player_turn())
        bot.print_tic_tac_toe()
        
        

    winner = bot.checkWin()
    if winner:
        print("The game has ended, the winner is", winner)
    else:
        print("The game has ended in a draw.")

elif player_var == "o":
    while bot.terminals() == False:
        

        move = bot.best_move()
        print(f"Best move for '{bot.player_turn()}':", move)
        bot.results(move ,bot.player_turn())
        bot.print_tic_tac_toe()

        # Necesitamos checar de nuevo si le juego termino porque si jugamos con o, el ultimo en poner sera el bot 
        # por lo tanto despues del bot checaremos de nuevo si ya termino y haremos un break para salir del while
        if bot.terminals():
            break

        print(f"Enter your movement one digit at a time for '{bot.player_turn()}'")
        try:
            x_1 = int(input("Enter the row index:"))
            x_2 = int(input("Enter the column index:"))
            if bot.board[x_1,x_2] == '0':
                bot.results((x_1,x_2),bot.player_turn())
                bot.print_tic_tac_toe()
                
        except ValueError:
            print("Invalid input! Please enter numeric indices.")
        except IndexError:
            print("Index out of bounds! Please enter correct indices.")


    winner = bot.checkWin()
    if winner:
        print("The game has ended, the winner is", winner)
    else:
        print("The game has ended in a draw.")

