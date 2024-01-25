def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer() # is_integer is not a built-in function but a method available for floating point number(float value can access to that function)
    
from runtime_calculating import runtime_calculating
if __name__ == '__main__':
    runtime_calculating(algorithm='is_integer', arg=2.2)