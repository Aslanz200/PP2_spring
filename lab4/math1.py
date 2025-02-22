import math

#1
def toRadian(deg):
    return deg*(math.pi/180)


#2
def area(height , base1 , base2):
    return ((base1+base2)/2)*height

#3
def polygonArea(sides , lenght):
    apothem = lenght/(2*math.tan(math.radians(180)/sides))
    return sides*lenght*apothem*(1/2)

#4
def parallelogram(lenght , height):
    return lenght * height


