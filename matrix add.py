m,n=map(int,input("enter rows and colums:").split())
a={}
print("enter the elements of matrix A:")
for i in range(m):
    a[i] = {}
    for j in range(n):
        a[i][j]=int(input("enter element:"))
b={}
print("enter the elements of matrix B:")
for i in range(m):
    b[i] = {}
    for j in range(n):
        b[i][j]=int(input("enter element:"))
s={}
for i in range(m):
    s[i]={}
    for j in range(n):
        s[i][j]=a[i][j]+b[i][j]
print("sum of matrix of A and B:")
for i in range(m):
    for j in range(n):
        print(s[i][j],end=" ")
    print(end="\n")