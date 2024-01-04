def insertion_sort(array, left=0, right=None):
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
        insertion_sort(array, i, min(i + min_run - 1), n - 1)
        
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min(start + size * 2 - 1, (n-1))
            
            merge_array = merge
    