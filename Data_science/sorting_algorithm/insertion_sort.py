# insertion sort in python

# instead of compare 2 elements at a time( bubble sort), it compares one element to the rest of the list

def insertion_sort(array):
    for i in range(1, len(array)):  # the loop starts with the second item on the list
        key_item = array[i]
        
        j = i - 1 # help initialize a variable that points to the left of the key_item( consecutively be compared to key item)
        
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array [j] # don't directly relate line 12 to line 13( confused)
            j -= 1
            
        array[j+1] = key_item # position item to the right place( before the last larger item to the key item)
        
    return array

# timing the insertion_sort
from random import randint
from timing.timing_sort_any_function import run_sorting_algorithm
if __name__ == '__main__':
    array = [randint(0, 1000) for i in range(0, 100)]
    run_sorting_algorithm(algorithm="insertion_sort",array=array)