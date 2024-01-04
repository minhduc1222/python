from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    
    # only import the algorithm if the function is not 'sorted'(a built-in function)

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=10, number=100)
    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    
ARRAY_LENGTH = 1000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting value from 0 - 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # Call the timing function using the name(function) you want to time that takes above array as its parameter 
    run_sorting_algorithm(algorithm="sorted", array=array)