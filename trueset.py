set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
def calculating_set():
    print(f'set1 has {len(set2)} elements')
    union = set1.union(set2)
    print('union', union)

    intersection = set1.intersection(set2)
    print('intersection', intersection)

    difference = set1.difference(set2)
    print('difference', difference)

    # elements in either set1 or set2 but not in both
    symmetric_difference = set1.symmetric_difference(set2)
    print('symmetric difference', symmetric_difference)

    is_subset = set1.issubset(set2)
    print('is set1 a subset of set2', is_subset)

    is_superset = set1.issuperset(set2)
    print('is set1 a superset of set2: ', is_superset)


from random import randint
from Data_science.Binary_Tree.runtime_calculating import runtime_calculating

if __name__ == '__main__':
    calculating_set()
    runtime_calculating('calculating_set')