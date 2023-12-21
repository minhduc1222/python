import random as rd
# use sample function
general = rd.sample(range(1, 100), 5)
print(general)

# use for loop
from random import randint
random_list = []
for n in range(1, 5):
    n = rd.randint(1, 100)
    random_list.append(n)
print(random_list)