def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(min_idx+1, len(input_list)): # comparing the specified element(at index idx) with those remaining elements to the right-most
            if input_list[min_idx] > input_list[j]: 
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx] # finding the smallest element, arrange it after the specified element
    return input_list

list = [19,2,31,45,30,11,121,27]
print(selection_sort(list))

             