a,b=map(int,input("Enter 2 numbers:").split())
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
x=int(input("Enter your choice:"))
if x==1:
    print(a+b)
elif x==2:
    print(a-b)
elif x==3:
    print(a*b)
elif x==4:
    if b==0:
        print("division by zero error")
    else:
        print(round(a/b,2))
else:
    print("invalid choice")