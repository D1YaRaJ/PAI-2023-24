import math
a,b,c=map(int,input("Enter 3 sides of triangle:").split())

#semi-perimeter
s=(a+b+c)/2
#Heron's formula
area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of triangle=",area)