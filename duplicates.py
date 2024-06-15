a=[1,2,2,3,3,3,4,4,4,4]
b=set()  
#set can handle duplicate elements
for i in a:
    if a.count(i)>1:
        b.add(i)

print("Duplicates:",b)