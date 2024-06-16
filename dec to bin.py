n=int(input("enter decimal number:"))
a=n
bin=0
base=1
while(n!=0):
        r=n%2
        bin=bin+(r*base)
        base=base*10
        n=n//2
print("binary of",a,"is",bin)