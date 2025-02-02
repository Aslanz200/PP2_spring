#1
class String:
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
    
#2
class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length ** 2

#3
class Shape:
    def area(self):
        return 0
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


#4
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x , self.y)
    def move(self , x1 , y1):
        self.x = x1
        self.y = y1
    def dist(self , p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        distance = (dx**2 + dy**2)**(1/2)
        return distance

#5
class Account:
    def __init__(self , person , money):
        self.person = person
        self.money = money
    def balance(self):
        return self.money
    def owner(self):
        return self.person
    def deposit(self, money):
        self.money += money
        return money
    def withdraw(self , money):
        if self.money - money < 0:
            print('Error')
        else:
                self.money-=money
                return money
        bank = Account("Bekzat", 1000)
a = Account('Aslan' , 1000)
print(a.balance())
print(a.owner())
print(a.deposit(1000))
print(a.withdraw(3000))
print(a.withdraw(2000))
  
    

#6
class Prime:
    def __init__(self, numbs):
        self.numbs = numbs
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
    def filtered(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))
