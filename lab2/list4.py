a = [3 , 1 , 2 , 5 , 4]
print(sorted(a))
a.sort(reverse=True)
print(a)


def func(x):
    return abs(x-2)
b = [3 , 1 , 2 , 5 , 4]
b.sort(key = func)
print(b)

c = [5 , 6 , 7 , 8 ,  9]
x = c.copy()
print(x)


d = [10 , 11 , 12 , 13 , 14]
z = list(d)
print(z)

print(b + c + x)

for i in c:
    d.append(i)
print(d)

