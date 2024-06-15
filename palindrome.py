#for string
a=input("enter a string:")
if a==a[::-1]:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")

#for numbers
n=int(input("enter a number:"))
n=str(n)
if n==n[::-1]:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")