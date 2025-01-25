a = [0 , 1]
b = [2 , 3]
for i in a:
    for j in b:
        print(i , j)


c = []
for i in range(1 , 30 , 3):
    c.append(i)
    if i == 25:
        break
print(c)