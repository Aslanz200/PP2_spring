a = ['banana' , 'apple' , 'cherry' , 'lemon']
print(a)
print(a[2])
print(a[0:3])
if 'banana' in a:
    print("True")

a[0] = 'orange'
print(a)

a[0:2] = ['banana' , 'orange']
print(a)