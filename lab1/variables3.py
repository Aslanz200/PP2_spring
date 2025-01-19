a = 5
def func():
    print(a+10)
func()



def func2():
    global x
    x = 5
func2()
print(10 + x)