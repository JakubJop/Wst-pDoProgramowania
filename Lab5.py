'*** zad1 ***'
values = [10, 20, 30]
keys = ["ten", "twent", "thirty"]

print(zip(values, keys))

z1= dict(zip(values, keys))
print(z1)

z1 = {}
for i in range(len(values)):
    z1[keys[i]] = values [i]
print(z1)

z2 = dict(thiirty=30, forty=40, fifty=50)
print(z2)
print()
z3 = z1.copy()
z3.update(z2)
print(z3)
"*** Zad 2  ***"

sample_dict = {"name": "Kelly", "surname": "Jones", "age": 25,"salary": 8000,"city": "New york"}







