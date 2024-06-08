car={"brand":"Ford","model":"ev567","year":2020,"year":2023,"colors":["black","white","grey"]}
print(car)
print(car["year"])
print(type(car))
print(len(car))
d1=dict(name="Ann",age=36,country="USA")
print(d1)
x=car.get("model")
y=car.keys()
z=car.values()
w=car.items()
print(w,x,y,z)
d1["age"]=33
d1["salary"]=35000
for x in car:
    print(x)
for x in car:
    print(car[x])
for x in car.keys():
    print(x)
for x in car.values():
    print(x)
for x,y in car.items():
    print(x,y)
d2=car.copy()
print(d2)
c1={"name":"Rohan","age":20}
c2={"name":"Ram","age":15}
c3={"name":"Diya","age":23}
fam={"child1":c1,"child2":c2,"child3":c3}
print(fam["child1"]["age"])
for x,obj in fam.items():
    print(x)
    for y in obj:
        print(y,":",obj[y])
car.popitem()
car.pop("model")
print(car)