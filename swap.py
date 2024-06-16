#using temporary variable
a,b=map(int,input("Enter a and b value:").split())
temp=a
a=b
b=temp
print("a=",a,"b=",b)

#without temp variable
a,b=map(int,input("Enter a and b value:").split())
a=a+b
b=a-b
a=a-b
print("a=",a,"b=",b)