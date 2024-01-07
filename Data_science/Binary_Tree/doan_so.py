from random import randint
from check_if_integer import is_integer
random = randint(1,10)
while True:
    number = input('nhap so can tim tu 1-10: ')
    if (is_integer(number) != True):
        print(f'gia tri {number} can la mot so tu nhien')
    elif (int(number)>10 or int(number)<1):
        print(f'gia tri {number} can trong khoang 1-10')
    else:
        number = int(number)
        if number > random:
            print(f'gia tri {number} dang lon hon gia tri can tim')
        elif number < random:
            print(f'gia tri {number} dang nho hon gia tri can tim')
        else:
            print(f'chuc mung ban, ban da doan dung gia tri can tim {random}')
            break
            
