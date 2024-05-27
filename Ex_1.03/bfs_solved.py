from collections import deque
import numpy as np

maze = [
    ['0', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '0', '1', '1'],
    ['0', '1', '1', '0', '1', '1'],
    ['0', '1', '0', '0', '1', '1'],
    ['0', '1', '0', '1', '1', '1'],
    ['0', '0', '0', '1', '1', '1']
]


# FORWARD_SEARCH
# Q.Insert(x1) and mark x_1 as visited

# while Q not empty do
# 	x- Q.GetFirst()
# 	if x belong to Xa
# 		return SUCCESS
# 	forall u belong to U(x)
# 		x < f(x,U)
# 		if x' not visited
# 			Mark x' as visited
# 			QuInsert(x')
# 		else
# 			Resolve duplicate x'
# return FAILURE

# LIFO 
# Last In First Out
 


def is_valid_move(row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == '0'


def BFS_queue(start, goal):
    visited = []
    queue = deque()
    path = []
    queue.append(start)
    visited.append(start)
    print("before enter while", queue)
    #NOW HERE WE NEED TO EXPLORE BOTH SIDES
    while queue:
        
        current_pos = queue[0]
        
        if current_pos == goal:
            return path   # Return the path if the goal is reached

        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for move in moves:
            new_row = current_pos[0] + move[0]
            new_col = current_pos[1] + move[1]
            current_pos = (new_row,new_col)


            if is_valid_move(new_row, new_col) and current_pos not in visited:
                visited.append(current_pos)
                #print("visited list: ", visited)
                queue.append(current_pos)
                #print("queue: ", queue)
                path.append(current_pos)
            
    return None

# Example usage
start_position = (6, 0)
goal_position = (3, 3)

result_path = BFS_queue( start_position, goal_position)


print(result_path)





