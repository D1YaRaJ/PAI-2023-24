a=("bmw","swift","audi","bmw")
#a[4]="skoda"  #gives error as tuple is unchangable
print(a)
#to replace or add or remove items ,tuple should be converted to list
x=list(a)
x.append("skoda")
x.remove("audi")
y=tuple(x)
print(y)
(grey,red,white,blue)=a
print(grey,red,white,blue)
z=a+y
print(z)
w=a*2
print(w)