from check_if_float import check_if_float
from Data_science.Binary_Tree.runtime_calculating import runtime_calculating
def square_number():
    a = input('nhap so vao: ')
    if not check_if_float(a):
        return square_number()
    print(pow(int(a), 2))

if __name__ == '__main__':
    square_number()
    runtime_calculating('square_number')