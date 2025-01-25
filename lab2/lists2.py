a = ['banana' , 'apple' , 'cherry' , 'lemon']
a.append('a car')
print(a)

a.insert(0 , 'fruit')
print(a)

b = [1 , 2 , 3 , 4]
a.extend(b)
print(a)

a.remove('fruit')
print(a)

a.pop(0)
a.pop()
print(a)

del a[0]
print(a)

a.clear()
print(a)