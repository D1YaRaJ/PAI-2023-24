n=input("enter decimal number:")
b='01'

if not all(char in b for char in n):
    print("invalid input")
else:
    #convert n of base 2 to integer
    dec=int(n,2) 
    print("decimal of",n,"is",dec)