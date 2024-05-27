#Codigo que corre bien con el valor correcto
# def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
#     if depth == 0 or "children" not in node:
#         return node['value'], 0  # Return the value of the node and no pruning initially

#     pruning_count = 0

#     if maximizingPlayer:
#         maxEval = float('-inf')
#         for child in node['children']:
#             eval, pruned = alpha_beta(child, depth-1, alpha, beta, False)
#             maxEval = max(maxEval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 pruning_count += 1 + sum(len(c['children']) for c in node['children'][node['children'].index(child)+1:])
#                 break
#         return maxEval, pruning_count
#     else:
#         minEval = float('inf')
#         for child in node['children']:
#             eval, pruned = alpha_beta(child, depth-1, alpha, beta, True)
#             minEval = min(minEval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 pruning_count += 1 + sum(len(c['children']) for c in node['children'][node['children'].index(child)+1:])
#                 break
#         return minEval, pruning_count

# # Example tree construction
# tree = {
#     'children': [
#         {'children': [
#             {'children': [
#                 {'value': 3},
#                 {'value': 1}
#             ]},
#             {'children': [
#                 {'value': 4},
#                 {'value': 1}
#             ]}
#         ]},
#         {'children': [
#             {'children': [
#                 {'value': 5},
#                 {'value': 9}
#             ]},
#             {'children': [
#                 {'value': 2},
#                 {'value': 6}
#             ]}
#         ]}
#     ]
# }

# # Perform alpha-beta pruning
# result, pruned_nodes = alpha_beta(tree, 3, float('-inf'), float('inf'), True)
# print("Resulting value:", result)
# print("Number of pruned nodes:", pruned_nodes)

# VERSION QUE DA RESULTADO Y NUMERO DE NODOS CORTADOS

# def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
#     if 'value' in node:
#         return node['value'], 0  # Return the value of the node and no pruning initially

#     pruning_count = 0

#     if maximizingPlayer:
#         maxEval = float('-inf')
#         for child in node['children']:
#             eval, pruned = alpha_beta(child, depth-1, alpha, beta, False)
#             maxEval = max(maxEval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 remaining_children = node['children'][node['children'].index(child)+1:]
#                 pruning_count += sum(1 + count_nodes(c) for c in remaining_children)
#                 break
#             pruning_count += pruned
#         return maxEval, pruning_count
#     else:
#         minEval = float('inf')
#         for child in node['children']:
#             eval, pruned = alpha_beta(child, depth-1, alpha, beta, True)
#             minEval = min(minEval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 remaining_children = node['children'][node['children'].index(child)+1:]
#                 pruning_count += sum(1 + count_nodes(c) for c in remaining_children)
#                 break
#             pruning_count += pruned
#         return minEval, pruning_count

# def count_nodes(node):
#     """ Count all nodes in this subtree """
#     if 'value' in node:
#         return 0  # Leaf nodes have no further children
#     return sum(1 + count_nodes(c) for c in node.get('children', []))

# # Tree definition remains the same
# tree = {
#     'children': [
#         {'children': [
#             {'children': [
#                 {'value': 3},
#                 {'value': 1}
#             ]},
#             {'children': [
#                 {'value': 4},
#                 {'value': 1}
#             ]}
#         ]},
#         {'children': [
#             {'children': [
#                 {'value': 5},
#                 {'value': 9}
#             ]},
#             {'children': [
#                 {'value': 2},
#                 {'value': 6}
#             ]}
#         ]}
#     ]
# }

# # Perform alpha-beta pruning
# result, pruned_nodes = alpha_beta(tree, 3, float('-inf'), float('inf'), True)
# print("Resulting value:", result)
# print("Number of pruned nodes:", pruned_nodes)
# def find_first_leaf_value(nodes):
#     """ Recursively finds the first leaf node value in a list of nodes. """
#     if isinstance(nodes, dict):  # If the input is a single node dictionary
#         if 'value' in nodes:
#             return nodes['value']
#         return find_first_leaf_value(nodes['children'])
#     elif isinstance(nodes, list):  # If the input is a list of nodes
#         for node in nodes:
#             if 'value' in node:
#                 return node['value']
#             elif 'children' in node:
#                 result = find_first_leaf_value(node['children'])
#                 if result is not None:
#                     return result
#     return None

# # Make sure to call find_first_leaf_value correctly in the alpha-beta function
# # This part of the code remains the same as before
# def count_nodes(node):
#     if 'value' in node:
#         return 0
#     return sum(1 + count_nodes(c) for c in node.get('children', []))


# def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
#     if 'value' in node:
#         return node['value'], 0, None  # No pruning here, so no pruned node value.

#     pruning_count = 0
#     pruned_value = None  # This will store the value of the first pruned node.

#     if maximizingPlayer:
#         maxEval = float('-inf')
#         for child in node['children']:
#             eval, pruned, pruned_val = alpha_beta(child, depth-1, alpha, beta, False)
#             maxEval = max(maxEval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 remaining_children = node['children'][node['children'].index(child)+1:]
#                 if remaining_children:
#                     pruning_count += sum(1 + count_nodes(c) for c in remaining_children)
#                     pruned_value = find_first_leaf_value(remaining_children)
#                 break
#             pruning_count += pruned
#         return maxEval, pruning_count, pruned_value
#     else:
#         minEval = float('inf')
#         for child in node['children']:
#             eval, pruned, pruned_val = alpha_beta(child, depth-1, alpha, beta, True)
#             minEval = min(minEval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 remaining_children = node['children'][node['children'].index(child)+1:]
#                 if remaining_children:
#                     pruning_count += sum(1 + count_nodes(c) for c in remaining_children)
#                     pruned_value = find_first_leaf_value(remaining_children)
#                 break
#             pruning_count += pruned
#         return minEval, pruning_count, pruned_value

# # Given the tree structure
# tree = {
#     'children': [
#         {   # B
#             'children': [
#                 {'children': [{'value': 3}, {'value': 1}]},  # D
#                 {'children': [{'value': 4}, {'value': 1}]}   # E
#             ]
#         },
#         {   # C
#             'children': [
#                 {'children': [{'value': 5}, {'value': 9}]},  # F
#                 {'children': [{'value': 2}, {'value': 6}]}   # G
#             ]
#         }
#     ]
# }

# result, pruned_nodes, pruned_value = alpha_beta(tree, 3, float('-inf'), float('inf'), True)
# print("Resulting value:", result)
# print("Number of pruned nodes:", pruned_nodes)
# print("Value of pruned node:", pruned_value)

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isinstance(node, int):  # leaf node or max depth reached
        return node, None  # Return the node value, no pruning occurred

    pruned = []
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node:
            eval, pruned_child = alpha_beta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                pruned.extend(node[node.index(child)+1:])  # Add remaining nodes to pruned list
                break
            if pruned_child:
                pruned.append(pruned_child)
        return maxEval, pruned
    else:
        minEval = float('inf')
        for child in node:
            eval, pruned_child = alpha_beta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                pruned.extend(node[node.index(child)+1:])  # Add remaining nodes to pruned list
                break
            if pruned_child:
                pruned.append(pruned_child)
        return minEval, pruned

# Example usage:
# Define the tree as nested lists where each inner list represents child nodes.
tree = [[[3, 1], [4, 1]], [[5, 9], [2, 6]]]

# Call the alpha_beta function starting with infinite alpha and beta values.
value, pruned_nodes = alpha_beta(tree, 3, float('-inf'), float('inf'), True)
print("Value at the root:", value)
print("Pruned nodes:", pruned_nodes)
