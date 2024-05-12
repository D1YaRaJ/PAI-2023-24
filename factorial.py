def factorial(x):
    if(x==0):
        return 1
    else:
        return x*factorial(x-1)

x=int(input("Enter number:"))
fact=factorial(x)
print(x,"!=",fact)


    