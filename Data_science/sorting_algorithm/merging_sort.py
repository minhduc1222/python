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
            index_right += 1
        else:
            result.append(left[index_left])
            index_left += 1
        
        if index_left == len(left): # if one array reach its end, the rest of the other array will be added immediately
            result.extend(right[index_right:]) # push the remaining elements as integer one by one( not a list when using append())
            break
        if index_right == len(right):
            result.extend(left[index_left:])
            break
    
    return result

def division_merge(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    
    return merge(left = division_merge(array[:midpoint]), right = division_merge(array[midpoint:]))


# timing the insertion_sort

from random import randint
from timing.timing_sort_any_function import run_sorting_algorithm

if __name__ == '__main__':
    array = [randint(0, 1000) for i in range(1000)]
    run_sorting_algorithm(algorithm="division_merge", array=array)
    