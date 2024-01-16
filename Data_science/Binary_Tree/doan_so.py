from random import randint
from check_if_integer import is_integer
from runtime_calculating import runtime_calculating

def choose_number():
    random_number = randint(1, 10)
    x = 0
    while x < 3:
        number = input('Nhap so can tim tu 1-10: ')
        if not number.isdigit() or not 1 <= int(number) <= 10:
            print(f'Gia tri {number} can la mot so tu nhien trong khoang 1-10')
            x += 1
        else:
            number = int(number)
            if number > random_number:
                print(f'Gia tri {number} dang lon hon gia tri can tim')
                x += 1
            elif number < random_number:
                print(f'Gia tri {number} dang nho hon gia tri can tim')
                x += 1
            else:
                print(f'Chuc mung ban, ban da doan dung gia tri can tim: {random_number}')
                x += 1
                break
    print("Het")
    play_option()

def play_option():
    while True:
        choice = input("Ban co muon choi nua? (1: Co, 0: Khong): ")
        if choice in ('0', '1'):
            break
        print("Ban phai chon 1 hoac 0")
    if choice == '1':
        choose_number()
    else:
        exit()
        
if __name__ == '__main__':
    runtime_calculating(algorithm='choose_number')

