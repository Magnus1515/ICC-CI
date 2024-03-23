import numpy as np

my_array = np.array([3,5,2,9])
my_array_2 = np.array([3, 5, 2, 9, 12, 5, 23, 23])
my_array_3 = np.array([-1 , 4 ,2 , 6, -3, -5, 0, 7])

def split_list(a_list):
    half = len(a_list)//2
    return np.array_split(a_list, 2)




# print(first_arr)
# print(second_arr)


def min_value(left_list, right_list):
    # and right_list[0] <= right_list [1] or right_list[0] >= right_list [1]:
    # Minumun value part
    if left_list[0] <= left_list [1]:
        x = left_list[0]
    else:
        x = left_list[1]

    if right_list[0] <= right_list [1]:
        y = right_list[0]
    else:
        y = left_list[0]
    #Maximun value part 
    if x >= y:
        return x
    else:
        return y
    

def min_value_2(left_list, right_list):
    # Max value part
    if left_list[0] >= left_list [1]:
        x = left_list[0]
    else:
        x = left_list[1]

    if right_list[0] >= right_list [1]:
        y = right_list[0]
    else:
        y = left_list[1]

    # Minimum value part 
    if x < y:
        
        return x
    else:
        return y
    


def max_value(array):
    first_t, second_t = split_list(array)

    first_arr, second_arr = split_list(first_t)
    third_arr, fourth_arr = split_list(second_t)
   
    left_value = min_value_2(first_arr, second_arr)

    right_value = min_value_2(third_arr,fourth_arr)
    
    if left_value >= right_value:
        return left_value
    else: 
        
        return right_value


first_arr, second_arr = split_list(my_array)
print("SOLUCION 2.02\n",min_value(first_arr,second_arr))
print("SOLUCION 2.03\n",max_value(my_array_2))
print("SOLUCION 2.04\n",max_value(my_array_3))