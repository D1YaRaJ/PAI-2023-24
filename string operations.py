a=" String Operations in Python "
print(len(a))
print("in" in a)
if "Operations" in a:
    print("'Operations' present in string")
if "hi" not in a:
    print("'hi' not in string")
print(a[2:10])
print(a[:5])
print(a[4:])
print(a[-8:-3])
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("s"," "))
print(a.split(" "))
b="hello"
c="hi"
print(a+b)
print(a+" "+b)