print("find area of 1.triangle 2.circle 3.rectangle")
n=int(input("enter your choice:"))
if n==1:
    a,b=map(int,input("enter base and height of triangle:").split())
    print("area=",0.5*a*b)
elif n==2:
    r=int(input("enter radius of circle:"))
    print("area=",(22/7)*r*r)
elif n==3:
    a,b=map(int,input("enter length and breadth of rectangle:").split())
    print("area=",a*b)
else:
    print("invalid input")