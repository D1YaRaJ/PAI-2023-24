import random
x=int(input("Guess number between 1 to 100:"))
y=random.randrange(1, 100)
if x==y:
    print("Your guess is correct")
else:
    print("Your guess is wrong the number was",y)