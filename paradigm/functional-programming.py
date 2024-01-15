# functional programming( often known as declarative paradigm as it uses declaration over statement), is when everything embraces a pure mathematical function style
    # treat every statement as functional expression (lambda, recursion)
    # treat function as value

# advantage: simple, improve the comprehension of code
# disadvantage: low readability, performance

import functools

mylist = [11, 22, 33, 44]
def sum_the_list(my_list):
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] + sum_the_list(mylist[1:])
    
# lambda function is used
print(functools.reduce(lambda x, y: x + y, mylist))
# apply a function that takes 2 initial items of a sequence as arguments,
# return the result, then repeat the function with the result and the next item till the end, from left to right
# -> reduce the iterable to a single value