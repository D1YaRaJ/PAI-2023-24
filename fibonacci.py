n=int(input("enter the no. of terms:"))
a,b=0,1
count=0
if n<=0:
    print("invalid input")
elif n==1:
    print("fibonacci sequence is",a)
else:
    print("fibonacci sequence is ",end=' ')
    while count<n:
        print(a,end=' ')
        temp=a+b
        a=b
        b=temp
        count+=1