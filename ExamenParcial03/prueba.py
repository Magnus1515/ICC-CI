import numpy as np

def split_list(a_list, n):
    return np.array_split(a_list, n)


def prunning_figure_2(array, alpha, beta):
    first_part, second_part, third_part = split_list(array, 3)

    #array_1, array_2 = split_list(first_part, 2)

    min_lvalues = []

    for arr in [first_part]:
        local_min = min(arr)
        min_lvalues.append(local_min)
        
        beta = min(beta, local_min)
        if beta <= alpha:
            break

    if beta <= alpha:
        min_left = beta
    else:
        #min_val_123 = [min_lvalues]
        max_values = [min_lvalues]
        min_left = max(max_values)
    alpha = min(alpha, min_left[0])

    # Right side
    min_mvalues = []
    for arr in [second_part]:
        local_min = min(arr)
        min_mvalues.append(local_min)
        
        beta = min(beta, local_min)
        if beta <= alpha:
            break

    if beta <= alpha:
        min_middle = beta
    else:
        #min_val_456 = min(min_values)
        max_values = [min_mvalues]
        min_middle= max(max_values)
    alpha = min(alpha, min_middle[0])

    #right side 
    min_rvalues = []
    for arr in [third_part]:
        local_min = min(arr)
        min_rvalues.append(local_min)
        
        beta = min(beta, local_min)
        if beta <= alpha:
            break

    if beta <= alpha:
        min_right = beta
    else:
        #max_val_789 = min(min_values)
        max_values = [min_rvalues]
        min_right= max(max_values)
    alpha = min(alpha, min_right[0])

    print("min_left ->",min_left,"min_middle ->",min_middle,"min_right ->",min_right)
    return max(min_left,min_middle, min_right)


ex_input_2 = np.array([4,8,5,9,3,7,2,4,6])
value_2 = prunning_figure_2(ex_input_2, float('-inf'), float('inf'))
print("SOLUCION FIGURA 2\n",value_2)
