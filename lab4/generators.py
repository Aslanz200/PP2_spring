#1
def square_generator(n):
    for i in range(1 , n+1):
        yield i**2
    
"""a = int(input())
b = square_generator(a)
for i in b:
    print(i , end=" ")"""

#2
def even(n):
    for i in range(n+1):
        if i%2 == 0:
            yield str(i)
"""a = int(input())
b = ' , '.join(even(a)).split(' ')
for i in b:
    print(i , end=' ')"""

#3
def div34(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

#4
def squares(a , b):
    for i in range(a , b+1):
        yield i**2
"""a = int(input())
b = int(input())
c = squares(a , b)
for i in c:
    print(i , end=' ')"""

#5
def reverseFunc(n):
    i = n
    while i>=0:
        yield i
        i -= 1
"""a = int(input())
b = reverseFunc(a)
for i in b:
    print(i , end=' ')"""