a = (1 , 2 , 3 , 4 , 5)
b = list(a)
b.remove(1)
a = tuple(b)
print(a)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

b = (5 , 6 , 7 , 8 , 9)
(first , *second , third) = b
print(first)
print(second)
print(third)

for i in b:
    print(i , end=" ")

print('\n')

print(b*2)