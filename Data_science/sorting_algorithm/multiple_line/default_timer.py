import random
import timeit

def fun():
    return random.randint(1, 800)

start = timeit.default_timer() # return the highest resolution timer on your system - most appropriate, accurate and also make code more portable
print(f'the start time is: {start}')
fun()
print(f'the time-gap between is: {timeit.default_timer() - start}') # 
