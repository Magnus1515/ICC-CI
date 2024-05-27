from collections import deque

import matplotlib.pyplot as plt

# maze = [
#     ['0', '1', '1', '1', '1', '1'],
#     ['0', '0', '0', '0', '0', '0'],
#     ['0', '1', '1', '0', '1', '1'],
#     ['0', '1', '1', '0', '1', '1'],
#     ['0', '1', '0', '0', '1', '1'],
#     ['0', '1', '0', '1', '1', '1'],
#     ['0', '0', '0', '1', '1', '1']
# ]

# def dfs_maze_path(maze, start, end):
#     stack = [(start, [start])]  # Each stack element is a tuple of current position and path
#     visited = set()

#     while stack:
#         (row, col), path = stack.pop()

#         if (row, col) == end:
#             print("Maze is solvable. Path:")
#             for position in path:
#                 print(position)
#             return True

#         if (row, col) not in visited and maze[row][col] == '0':
#             visited.add((row, col))

#             # Explore neighbors (up, down, left, right)
#             neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
#             for neighbor in neighbors:
#                 if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
#                     stack.append((neighbor, path + [neighbor]))

#     print("Maze is not solvable.")
#     return False



# # Example usage:
# start_position = (6, 0)
# end_position = (3, 3)
# result = dfs_maze_path(maze, start_position, end_position)
maze = []
with open("maze_02.csv", "r") as file:
    for line in file:
        line = line.split(",")
        row = []
        for c in line:
            if "1" in c:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)



start = (6, 0) #our start node
obj = (3, 3) # final node 

path = []
stack = []

def check_direction(node, queue):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for move in directions:
        new_row = node[0] + move[0]
        new_col = node[1] + move[1]

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
            path.append((new_row, new_col))  # Append the new position to the path
            maze[new_row][new_col] = 2 # This is the way to know is already visited
            queue.append((new_row, new_col)) # Updating the queue

#DFS using stack 
def DFS_stack(start, obj):
    stack = [start] # Get the first value in the queue
    counter = 0 #initialize our counter 

    while stack:
        current_node = stack.pop() # The correct way to remove the first value [0] al the times
        if current_node == obj: # check if our current node is the final
            return counter, path  # Return the counter, visited cells, and the path

        check_direction(current_node, stack) #check our directions that are correct 
        counter += 1 #and increase our counter

    return None


def main():
    result = DFS_stack(start, obj) 

    if result is not None:
        steps, final_path = result
        print("Number of steps:", steps)
        print("Final path:", final_path)
        plt.imshow(maze, cmap='viridis', origin='upper')
        plt.show()

    else:
        print("No path found.")


if __name__ == "__main__":
    main()




# def bfs_maze_path(maze, start, end):
#     queue = deque([(start, [start])])
#     visited = set()

#     while queue:
#         (row, col), path = queue.popleft()

#         if (row, col) == end:
#             print("Maze is solvable. Path:")
#             for position in path:
#                 print(position)
#             return True

#         if (row, col) not in visited and maze[row][col] == '0':
#             visited.add((row, col))

#             neighbors = [
#                 (row - 1, col),  # Up
#                 (row + 1, col),  # Down
#                 (row, col - 1),  # Left
#                 (row, col + 1)   # Right
#             ]

#             for neighbor in neighbors:
#                 n_row, n_col = neighbor
#                 if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]):
#                     queue.append(((n_row, n_col), path + [(n_row, n_col)]))

#     print("Maze is not solvable.")
#     return False



