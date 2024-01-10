def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(min_idx+1, len(input_list)): # comparing the specified element(at index idx) with those remaining elements to the right-most
            if input_list[min_idx] > input_list[j]: 
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx] # finding the smallest element, arrange it after the specified element
    return input_list

# timing the tim_sort
from random import randint
from timing.timing_sort_any_function import run_sorting_algorithm

if __name__ == '__main__':
    array = [randint(0, 1000) for i in range(100)]
    run_sorting_algorithm(algorithm="selection_sort", array=array)
             