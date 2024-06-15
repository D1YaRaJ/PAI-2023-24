m,n=map(int,input("enter no. of rows and colums:").split())
a={}
print("enter the elements of matrix A:")
for i in range(m):
    a[i] = {}
    for j in range(n):
        a[i][j]=int(input("enter element:"))
print("matrix A:")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print(end="\n")