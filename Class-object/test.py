print((7.5+8+10)/3)
this_list = [['a', 5, 7.5], ['b', 2, 8], ['c', 4, 10]]
total = 0
for i in this_list:
    total += i[2]
average = total/len(this_list)
print(average)