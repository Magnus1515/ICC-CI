from collections import deque
import matplotlib.pyplot as plt
import heapq
from math import dist

#1.13
start = (2, 1)
end = (8, 7)

#1.12
# start = (8 ,2)
# end = (3, 7)

path = []
maze = []
visited = []
coordinate_costs = {}



with open("/Users/davidroldanmachado/Desktop/ICC/8/ICC-CI/Ex/EjercicioBestSearch/maze_04.csv", "r") as file:
    for line in file:
        line = line.split(",")
        row = []
        for c in line:
            if "1" in c:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)


def reconstruct_path(start, current, predecessors):
    path = [] 
    

    while current != start:
        path.insert(0, current)  # Add current to the beginning of our path 
        current = predecessors[current] # upate the current node to predeccesors so in this way we do the path towards start node
        
    path.insert(0, start)  # Add start to the beginning of path
    return path



def best_search_2(start, goal, maze):
    queue = []  # This will be a queue of visited nodes
    queue_dist = []
    heapq.heappush(queue, (0, start))  # Push the start node with priority 0
    heapq.heappush(queue_dist, (0, start)) #push the temp node with priority 0
    predecessors = {start: None}
    costs = {start: 0}

    while queue:
        current_cost, current_node = heapq.heappop(queue) # get the node with the lowest cost fromo our queue
        current_dist, current_node = heapq.heappop(queue_dist)
        # print(current_node) 
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]: 
            next_node_dist = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= next_node_dist[0] < len(maze) and 0 <= next_node_dist[1] < len(maze[0]) and maze[next_node_dist[0]][next_node_dist[1]] == 0:
                new_dist = dist(next_node_dist,end)
                heapq.heappush(queue_dist, (new_dist, next_node_dist)) 


        if current_node == goal: #if get to our goal we restruct the path for our final result
            return reconstruct_path(start, goal, predecessors)
        # 
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]: 
            next_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            
            
            if 0 <= next_node[0] < len(maze) and 0 <= next_node[1] < len(maze[0]) and maze[next_node[0]][next_node[1]] == 0:
                #print(next_node)
                # new_cost = dist(next_node,end) # way to calculate eucladiane distance
                new_cost = current_cost + 1
                if next_node not in costs or new_cost < costs[next_node]:
                    costs[next_node] = new_cost 
                    priority = new_cost #thats going to be our priority
                    heapq.heappush(queue, (priority, next_node))
                    predecessors[next_node] = current_node
                    # bmaze[next_node] = 2

    return None  # If goal is not reachable

#My codes is visiting all the path instead of just visting the final path

def main():
    result = best_search_2(start, end, maze)

    if result is not None:
        final_path = result
        print("Number of steps:", len(final_path))
        print("Final path:", final_path)
        # plt.imshow(maze, cmap='viridis', origin='upper')
        # plt.show()

    else:
        print("No path found.")


if __name__ == "__main__":
    main()
