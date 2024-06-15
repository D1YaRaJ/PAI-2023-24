x,y,z=map(int,input("Enter 3 numbers:").split())
if (x>=y) and (x>=z):
    maxi=x
elif (y>=x) and (y>=z):
    maxi=y
else:
    maxi=z
print("largest no. is",maxi)

