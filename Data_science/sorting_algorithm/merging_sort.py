# merging sort function
def merge(left, right):
    if len(left) == 0: # check if the left array has no item, return the whole other array as final result
        return right
    
    if len(right) == 0:
        return left
    
    result = []
    index_left = index_right = 0
    
    while len(result) < len(left) + len(right):
        if left[index_left] > right[index_right]: # compare element from the head of each array and push the smaller
            result.append(right[index_right])
            index_right +=1
        else:
            result.append(left[index_left])
            index_left +=1
        
        if index_left == len(left): # if one array reach its end, the rest of the other array will be added immediately
            result.append(right[:index_right])
            break
        if index_right == len(right):
            result.append(left[:index_left])
            break
    
    return result

array = [randint(1,1000) for i in range(1000)]
def division_merge(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    
    return merge(left = division_merge(array[:midpoint]), right = division_merge(array[midpoint:]))


# timing the insertion_sort
from pdb import run
from timing.timing_sort_any_function import run_sorting_algorithm
from random import randint

run_sorting_algorithm(merge,array)
run_sorting_algorithm(division_merge,array)
