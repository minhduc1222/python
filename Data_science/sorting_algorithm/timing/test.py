from random import randint
from timeit import repeat

def sorting_al(algorithm, array):
    setup_code = f'from __main__ import {algorithm}' \
        if algorithm != 'sorted' else ''
        
    stmt = f'{algorithm}({array})'
    
    time_repeat = repeat(setup=setup_code, stmt=stmt, repeat = 10, number = 100)
    
    print(f'the minimum execution time is: {min(time_repeat)}')
    
ARRAY_LENGTH1 = 1000
array = {randint(1,1000) for i in range(ARRAY_LENGTH1)}
if __name__ == '__main__':
    sorting_al(algorithm='sorted', array = array)