import re
with open("/Users/azenilmes/Desktop/git/lab5/row.txt" , "r") as f:
    data = f.read()

print('1st exercise: ')
x = re.findall("a{1}b*" , data)
print(x)


print('\n2nd exercise: ')
x = re.findall("a{1}b{2,3}" , data)
print(x)


print("\n3rd exercise: ")
x = re.findall("[a-z]+_[a-z]+" , data)
print(x)


print("\n4th exercise: ")
x = re.findall("[A-Z]{1}[a-z]+" , data)
print(x)


print("\n5th exercise: ")
x = re.findall("a.\S*b" , data)
print(x)


print("\n6th exercise: ")
x = re.sub("[,. ]" , ":" , data)
print(x)


print("7th exercise: ")
x = re.sub("[_]" , "" , data)
print(x)
