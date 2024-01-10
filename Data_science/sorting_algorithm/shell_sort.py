def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap
            while j >= gap and input_list[j - gap] > temp: # temp element(index j) traverse from the right side of gap, compare itself with previous element at index j-gap, then swap place if the previous is greater
                input_list[j] = input_list[j - gap]
                j = j-gap # repeating the same process with previous element as temp element
                input_list[j] = temp
# Reduce the gap for the next element
        gap = gap//2
    return input_list

# timing the tim_sort
from random import randint
from timing.timing_sort_any_function import run_sorting_algorithm

if __name__ == '__main__':
    array = [randint(0, 1000) for i in range(100)]
    run_sorting_algorithm(algorithm="shellSort", array=array)