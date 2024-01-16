from random import randint
from timeit import repeat

def runtime_calculating(algorithm, arg=None):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != 'sorted' else ' '
    if arg is not None:
        stmt = f"{algorithm}({arg})"
    else:
        stmt = f"{algorithm}"
    times = repeat(setup=setup_code, stmt=stmt, repeat=10, number=100)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

if __name__ == '__main__':
    ARRAY_LENGTH = 1000
    array = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    runtime_calculating(algorithm="sorted", arg=array)