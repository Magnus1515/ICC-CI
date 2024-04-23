import matplotlib.pyplot as plt
def initial_state(x):
    if x == "s_0":
        return [0,0,0,0,0,0,0,0,0]
    else:
        return [1,2,5,3,3,5,6,7,8]





def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


print(print_tic_tac_toe(initial_state("s_0")))


# maze = []
# with open("/Users/davidroldanmachado/Desktop/ICC/8/ICC-CI/Ex/Ejercicio2.04/maze_03.csv", "r") as file:
#     for line in file:
#         line = line.split(",")
#         row = []
#         for c in line:
#             if "1" in c:
#                 row.append(1)
#             else:
#                 row.append(0)
#         maze.append(row)


# def main():
#     # result,final_c = best_first_search(start, end, maze)
#     # if result is not None:
#     #     print("Number of steps: ", len(result))
#     #     print("Final Cost: ", final_c)
#     #     print("Final path: ", result)

#     #     for (x, y) in result:
#     #         maze[x][y] = 2  # Mark the final path

#         plt.imshow(maze, cmap='viridis', origin='upper')
#         plt.grid(True, which='both', linestyle='--', linewidth=1)  # Add grid with spacing of 3x3
#         plt.show()
        
        

#         #plt.colorbar()  # Optional: Adds a colorbar to help distinguish values
#     # else:
#     #     print("No path found.")

# if __name__ == "__main__":
#     main()
        
# import tkinter as tk
# from tkinter import messagebox, simpledialog

# window = tk.Tk()
# window.title("TicTacToe")

# btns = [for i in range(3):
#         row = []
#         for j in range(3):
#             btn = tk.Button(window, text=" ", width=10, height=5,
#                             command=lambda row=i, col=j: 
#                             handle_move(row, col))
#             btn.grid(row=i, column=j)
#             row.append(btn)
#             btns.append(row)]

# def reset_game():
#     global board, player, btns
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     player = "X"
#     for i in range(3):
#         for j in range(3):
#             btns[i][j].config(text=" ", state=tk.NORMAL):