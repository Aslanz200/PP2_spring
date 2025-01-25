thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for i in thisdict.values():
    print(i)

for i in thisdict.keys():
    print(i)

print('\n')

for i, j in thisdict.items():
    print(i , j)


a = thisdict.copy()
print(a)

b = dict(thisdict)
print(b)
