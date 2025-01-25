a = {1 , 1 , 3 , 2}
print(a)

print(type(a))

c = {0 , 1 , True , False}
print(c)

for i in a:
    if i>2:
        print(i)
print(4 in a)


a.add(4)
print(a)

a.update(c)
print(a)

a.remove(0)
print(a)

a.discard(1)
print(a)

thisset = {"apple", "banana", "cherry"}

a.clear()
print(a)

del a