#1
from functools import reduce
a = [1 ,2 , 3 , 4 , 5]
def multList(x , y):
    return x*y
result = reduce(multList , a)
print(result)




#2
def countUpLow(s : str):
    up = low = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    return up , low

#3
def palindrome(s : str):
    rev = ''.join(reversed(s))
    if rev.lower() == s.lower():
        return True
    return False

#4
import math
import time
a = int(input())
b = int(input())
sec = b/1000
time.sleep(sec)
print(f"square root of {a} after {b} miliseconds is {math.sqrt(a)}")


#5
def allTrue(t : tuple):
    return all(t)
x = (True , True , True)
print(allTrue(x))