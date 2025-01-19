a = """
multiline 
string
"""
print(a)

a = '''
the same 
thing
'''
print(a)

print(a[5]) #string is an array that contains multiple characters


for i in range(len(a)):   # we can iterate through the string using its length
    print(a[i] , end='')

for i in a:     # or like this
    print(i , end='')

#checking if substring is in string
txt = 'aboba'
print('bob' in txt)
if('aaa' not in txt):
    print("not in the txt")
