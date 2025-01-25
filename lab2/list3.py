a = ["apple", "banana", "cherry"]
for i in a:
    print(i , end=" ")

print('\n') 

for i in range(len(a)):
    print(a[i] , end=" ")

print('\n')

i = 0
while i<len(a):
    print(a[i] , end=" ")
    i += 1

print("\n")

[print(x , end=" ") for x in a]

print("\n")

a = ["apple", "banana", "cherry", "kiwi", "mango"]
b = [x for x in a if "a" in x]
print(b)


a = [i for i in range(1,6)]
print(a)

a = [i for i in a if i%2==0]
print(a)