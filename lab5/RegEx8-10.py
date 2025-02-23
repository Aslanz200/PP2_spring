import re
with open("/Users/azenilmes/Desktop/git/lab5/row8.txt" , "r") as f:
    data = f.read()

print("\n8th exercise: ")
x = re.split(r"(?=[A-Z])" , data)
print(x)


print("\n9th exercise: ")
x = re.sub(r"([a-z])([A-Z])" , r"\1 \2" , data)
print(x)


print("\n10th exercise: ")
x = re.sub(r"([a-z])([A-Z])" , r"\1_\2" , data)
print(x)