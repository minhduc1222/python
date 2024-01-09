def uppercase_decorator(function):
    return function().upper()
def say_hi():
    return 'hi'

x = uppercase_decorator(say_hi)
x()
