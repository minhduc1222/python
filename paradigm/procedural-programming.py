# procedural programming language: series of steps are organized into modules(each contains  a set of related functions, methods),
# then all are serially executed step by step
#-> modularization done by functional implementation
    # modularity can be interpreted by breaking a program into smaller part( functions) - each for a specific task
    
# advantage: portable source code
            # general purpose programming
            # code reusability
            
# disadvantage: not suitable for real world project

# procedural way of finding sum of a list

mylist = [10, 20, 30, 40]
# modulization done by functional approach
def sum_of_list(array):
    res = 0
    for item in array:
        res += item
    return res

print(sum_of_list(mylist))