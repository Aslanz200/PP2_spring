thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


thisdict.update({"year": 2020})
print(thisdict)

thisdict["color"] = 'red'
print(thisdict)
thisdict.update({"length" : "3m"})
print(thisdict)


thisdict.pop("model")
print(thisdict)


for i in thisdict:
    print(i)


for i in thisdict:
    print(thisdict[i])

