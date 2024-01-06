# doan so
from random import randint
while True:
    input_number = int(input('nhap so: '))
    random = randint(0,50)
    if input_number != random:
        print(f'so ban nhap {input_number} khac voi so can tim {random}')
        continue
    else:
        print(f'chuc mung ban, ban da doan dung {random}')
        break