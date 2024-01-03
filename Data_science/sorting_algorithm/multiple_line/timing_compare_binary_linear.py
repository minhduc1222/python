# binary search
import timeit

def binary_search(my_list, find):
    while len(my_list) > 0:      
        center = len(my_list) // 2
        if find == center:
            return True
        elif find < center:
            my_list = my_list[:center]
        elif find > center:
            my_list = my_list[center+1:]
    return False

# linear search
def linear_search(my_list, find):
    for x in my_list:
        if x == find:
            return True
    return False

# compute binary_search time
def binary_time():
    SETUP_CODE = '''
from random import randint
from __main__ import binary_search'''
    
    TEST_CODE = '''
my_list = [x for x in range(1000)]
find = randint(0, len(my_list))
binary_search(my_list, find)'''
    
    times = timeit.repeat(setup= SETUP_CODE, stmt= TEST_CODE, repeat = 5, number = 100)
    print('the minimum run-time: {}'.format(min(times)))
    
def linear_time():
    SETUP_CODE = '''
from random import randint
from __main__ import linear_search'''
    
    TEST_CODE = '''
my_list = [x for x in range(1000)]
find = randint(0, len(my_list))
linear_search(my_list, find)'''
    
    times = timeit.repeat(setup= SETUP_CODE, stmt= TEST_CODE, repeat = 5, number = 100)
    print('the minimum run-time: {}'.format(min(times)))
    
if __name__ == '__main__':
    binary_time()
    linear_time()
    