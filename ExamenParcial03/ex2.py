# def alpha_beta(node, depth, alpha, beta, maximizing_player, pruned):
#     # Check if the node is a terminal node (i.e., an integer that represents a leaf value)
#     if type(node) == int:
#         return node
    
#     if maximizing_player:
#         max_eval = float('-inf')
#         children = tree[node]  # Get children of the current node
#         for child in children:
#             eval = alpha_beta(tree[child] if type(tree[child]) == int else child, depth - 1, alpha, beta, False, pruned)
#             max_eval = max(max_eval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 # Record the pruned nodes' values
#                 pruned.extend([tree[x] for x in children if children.index(x) > children.index(child)])
#                 break
#         return max_eval
#     else:
#         min_eval = float('inf')
#         children = tree[node]  # Get children of the current node
#         for child in children:
#             eval = alpha_beta(tree[child] if type(tree[child]) == int else child, depth - 1, alpha, beta, True, pruned)
#             min_eval = min(min_eval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 # Record the pruned nodes' values
#                 pruned.extend([tree[x] for x in children if children.index(x) > children.index(child)])
#                 break
#         return min_eval

# # Correct tree structure with leaf values
# tree = {
#     'A': ['B', 'C', 'D'],
#     'B': ['E', 'F', 'G'],
#     'C': ['H', 'I', 'J'],
#     'D': ['K', 'L', 'M'],
#     'E': 4, 'F': 8, 'G': 5, 'H': 9, 'I': 3, 'J': 7, 'K': 2, 'L': 4, 'M': 6
# }

# pruned = []

# # Start the alpha-beta pruning
# result = alpha_beta('A', 3, float('-inf'), float('inf'), True, pruned)

# print("Value:", result)
# print("Pruned nodes values:",)
def alpha_beta(node, depth, alpha, beta, maximizing_player, pruned):
    if isinstance(node, int):
        return node

    if maximizing_player:
        max_eval = float('-inf')
        children = tree[node]  # Get children of the current node
        for child in children:
            child_value = tree[child] if isinstance(child, str) and isinstance(tree[child], int) else child
            eval = alpha_beta(child_value, depth - 1, alpha, beta, False, pruned)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                # Add values directly to pruned list when pruning occurs
                pruned.extend([tree[x] for x in children if children.index(x) > children.index(child)])
                break
        return max_eval
    else:
        min_eval = float('inf')
        children = tree[node]  # Get children of the current node
        for child in children:
            child_value = tree[child] if isinstance(child, str) and isinstance(tree[child], int) else child
            eval = alpha_beta(child_value, depth - 1, alpha, beta, True, pruned)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                # Add values directly to pruned list when pruning occurs
                pruned.extend([tree[x] for x in children if children.index(x) > children.index(child)])
                break
        return min_eval

# Correct tree structure with leaf values
tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'I', 'J'],
    'D': ['K', 'L', 'M'],
    'E': 4, 'F': 8, 'G': 5, 'H': 9, 'I': 3, 'J': 7, 'K': 2, 'L': 4, 'M': 6
}

pruned = []

# Start the alpha-beta pruning
result = alpha_beta('A', 3, float('-inf'), float('inf'), True, pruned)

print("Value:", result)
print("Pruned nodes values:", pruned)
