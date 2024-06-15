a=[1,2,2,3,3,3,4,4,4,4]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Counts:",count)