s={"apple","mango","banana","apple"}
s1={"apple", 34, True, 10, "mango"}
s2=set(("apple","mango","banana"))
print(s2)
print(len(s))
s.add("orange")
print(type(s2))
for x in s:
    print(x)
s.update(s1)
print(s)
s.remove("banana")
s3=s.union(s1,s2)
s4=s|s1
print(s3,"\n",s4)
s5=s.intersection(s1)
print(s5)
s.difference_update(s1)
print(s1)
s2.clear()
del s2
