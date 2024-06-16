n=int(input("enter a number:"))
sum=0
temp=n
while temp>0:
    r=temp%10
    sum+=r**3  #r to the power 3
    temp//=10  #temp = temp // 10 .// discards fractional part
if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")