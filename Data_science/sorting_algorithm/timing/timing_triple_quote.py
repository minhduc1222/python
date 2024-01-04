# testing timeit
import timeit
math_module = 'from math import sqrt'
algorithm = '''def square_number():
    result_list = []
    for i in range(1, 100):
        n = sqrt(i)
        if n.is_integer():
            result_list.append(i)
        else:
            continue
    print(result_list)'''
# code snippet( mau code) need to be executed
print(timeit.timeit(setup=math_module, stmt = algorithm, number = 10000))