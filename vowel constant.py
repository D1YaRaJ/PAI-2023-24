a=input("Enter a character:")
if a.isalpha() and len(a)==1:
    vowels='aeiouAEIOU'
    if a in vowels:
        print(a,"is a vowel")
    else:
        print(a,"is a consonant.")
else:
    print("Invalid input.enter a single alphabet")
