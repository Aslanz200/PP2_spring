#1
def ounces(grams):
    return grams/28.3495231

#2 
def centigrade(F):
    return (5 / 9) * (F - 32)

#3 
def solve(numheads, numlegs):
    fourleg = (numlegs/2)-numheads
    twoleg = numheads - fourleg
    return twoleg , fourleg

#4
def filter_prime(arr):
    for i in arr:
        if i==1:
            arr.remove(1)
        for j in range(2 , int(i)-1):
            if int(i)%j==0:
                arr.remove(i)
    return arr

#5
import itertools
def permutations(str):
    itertools.permutations(str, r=None)

#6
def reverse_sentence(str):
    words = str.split(" ")
    result = words[::-1]
    return ' '.join(result)

#7
def has_33(nums):
    for i in range(len(nums)):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

#8
def spy_game(nums):
    a = [0, 0 , 7]
    index = 0
    for i in nums:
        if i==a[index]:
            index += 1
            if index == len(a):
                return True
    return False

#9
def volume(radius):
    PI = 3.14
    return (4/3)*PI*(radius**3)

#10
def unique_list(arr):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    return a

#11
def palindrome(a):
    if str(a)[::-1] == str(a):
        return True
    return False

#12
def histogram(arr):
    for i in arr:
        print("*"*i)
    return 0

#13
from random import randint
def guess():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    random_number = randint(1 , 21)
    count = 1
    while True:
        print("Take a guess.")
        num = int(input())
        if num>random_number:
            print("Your guess is too high.")
        elif num<random_number:
            print("Your guess is too low.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            return 0
        count += 1


