from merging_sort import merge
def insertion_sort(array, left=0, right=None): # using left and right to sort the resulted array in place without having to create the new one
    if right == None:
        right = len(array) - 1
        
    for i in range(left+1, right+1):
        key_item = array[i]
        j = i-1
        
        while j>=0 and array[j] > key_item:
            array[j+1] = array[j]
            j -= 1
            
        array[j+1] = key_item
        
    return array


def tim_sort(array):
    min_run = 32
    n = len(array)
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1)) # create small slices, runs and sort using insertion sort( insertion sort work best in small array)
        
    size = min_run
    while size < n: # start to merge each pair of small runs(run-size = 32 items), after each for iteration, the run-size will double(-proceed to merge 2 double large pair of runs till one single sorted run remains)
        for start in range(0, n, size * 2): 
            midpoint = start + size - 1
            end = min(start + size * 2 - 1, (n-1))

            merge_array = merge(left = array[start:midpoint+1], right = array[midpoint+1:end+1]) 
            array[start:start + len(merge_array)] = merge_array
            
        size *= 2
        
    return array

# timing the tim_sort
from random import randint
from timing.timing_sort_any_function import run_sorting_algorithm

if __name__ == '__main__':
    array = [randint(0, 1000) for i in range(100)]
    run_sorting_algorithm(algorithm="tim_sort", array=array)
    