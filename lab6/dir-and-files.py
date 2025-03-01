import os

#1
all = list(os.listdir())
#print(all)


#2
def checkAccess(s : str):
    if os.path.exists(s):
        print("path exists")
        if os.access(s , os.R_OK):
            print("readable")
        else:
            print("not readable")
        if os.access(s , os.W_OK):
            print("writable")
        else:
            print("not writable")
        if os.access(s , os.W_OK):
            print("executable")
        else:
            print("not executable")
    else:
        print("path does not exists")
    return 0


#3
def check(s : str):
    if os.path.exists(s):
        print("path exists")
        print(os.path.basename(s))
        print(os.path.dirname(s))
    else:
        print("path does not exists")
    return 0
s = '/Users/azenilmes/Desktop/git/lab5/RegEx8-10.py'
#check(s)


#4
s = "/Users/azenilmes/Desktop/git/lab6/example4.txt"
def countLines(s : str):
    with open(s) as f:
        x = 0
        for i in f:
            x += 1
    return x
#print(countLines(s))

#5
a = ["result" , "is" , ":" , "text"]
b = "/Users/azenilmes/Desktop/git/lab6/example5.txt"
def listToFile(a : list , b : str):
    with open(b , "w") as f:
        for i in a:
            f.write(i)


#6
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def createFiles():
    for i in letters:
        x = open(f"{i}.txt" , "x")
        x.close()
    return 0
#createFiles()


#7
first = "/Users/azenilmes/Desktop/git/lab6/example7_1.txt"
second = "/Users/azenilmes/Desktop/git/lab6/example7_2.txt"
def copyOneToAnother(s1 : str , s2 : str):
    a = open(s1 , 'r')
    b = open(s2 , 'w')
    x = a.read()
    b.write(x)
    a.close()
    b.close()
    return 0
#copyOneToAnother(first , second)


#8
def deleteFile(s : str):
    if os.path.exists(s):
        os.remove(s)
    else:
        print("No such file or directory exists")
s = "/Users/azenilmes/Desktop/git/example.txt"
#deleteFile(s)