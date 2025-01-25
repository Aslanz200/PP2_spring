a = {1 , 2 , 3, 4 , 5}
for i in a:
    print(i)

set1 = {1 , 2 , 3 , 4 , 5}
set2 = {3 , 4 , 5 , 6 , 7}

set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

set3 = set1.symmetric_difference(set2)
print(set3)
