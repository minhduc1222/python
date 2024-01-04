from random import randint
def quicksort(array):
    if len(array) < 2:
        return array
    
    low, same, high = [], [], []
    
    pivot = array[randint(0, len(array) - 1)] # select a pivot(random item on the list) for partitioning
    
    for item in array:
        if item < pivot:
            low.append(i)
        elif item == pivot:
            same.append(i)
        elif item > pivot:
            high.append(i)
        
    return quicksort(low) + same + quicksort(high) # recursively sort the low and high list and combine with same list => final result

# timing the insertion_sort
from pdb import run
from timing.timing_sort_any_function import run_sorting_algorithm
from random import randint

array = [randint(1,1000) for i in range(1000)]
run_sorting_algorithm(quicksort,array)