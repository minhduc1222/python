# implementation of bubble sort in python
def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        # create a flag, allow the function to terminate if there's nothing to be sorted
        al_sorting = True
        for j in range(n-i-1): # push the largest element to the end, then second element and so on, traversing range getting smaller after each j iteration
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                al_sorting = False # set the flag to False if there's required elements to swap
            
        if al_sorting: # break when if condition above does not happen in the last iteration( all'd been sorted perfectly)
            break
        
    return array

# timing the bubble_sort function

from timing.timing_sort_any_function import run_sorting_algorithm
from random import randint
array = [randint(1, 1000) for i in range(1000)]
if __name__ == '__main__':
    run_sorting_algorithm(algorithm=bubble_sort, array=array) # cant run??