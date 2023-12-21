import os

def listing_file(path, level = 0):
    file = path.split('/')[-1]
    print(' ' * level *2, end=' ')
    if os.path.isfile(path):
        print('+', file)
    else:
        print('-', file)
    if os.path.isdir(path):
        for f in os.listdir(path):
            listing_file(path + "/" + f, level + 1)

        
path = input('enter path: ')
listing_file(path)