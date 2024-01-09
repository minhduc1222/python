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

list = [19,2,31,45,30,11,121,27]
print(shellSort(list))