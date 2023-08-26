# Given an array of integers arr[] of size N and an integer, 
# the task is to rotate the array elements to the left by d positions
# After rotation d positions to the left, the first d elements become 
# the last d elements of the array.



# ============= APPROACH 1 ================ #
import numpy as np

def rotate(arr_list, d, n):
    k = arr_list.index(d)
    narr_list1 = np.array(arr_list[k+1:])
    narr_list2 = np.array(arr_list[0:k+1])
    concatenated_array = np.concatenate([narr_list1, narr_list2])
    return concatenated_array
        
        
arr = [1, 2, 3, 4, 5, 6, 7]
print(Rotate(arr, 3, len(arr)))