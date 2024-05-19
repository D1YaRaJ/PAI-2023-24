a=["bmw","swift","audi","bmw"]
b=["honda","ktm","tvs","vespa"]
print(a)
print(len(a))
print(type(a))
print(a[2])
print(a[-3])
print(a[1:3])
print(a[2:])
print(a[:3])
a[3]="skoda"
a.insert(2,"audi")
a.append("tata")
print(a)
print(a.extend(b))
b.remove("vespa")
b.pop(2)
del b[1]
print(a,b)
b.clear()
print(a,b)
for x in a:
    print(x)
c=[34,76,12,100]
d=c.copy()
c.sort()
print(c,d)  
