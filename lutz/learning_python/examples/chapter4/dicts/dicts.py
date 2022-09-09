D = {"food": "spam", "quantity": 4, "color": "pink"}
print(D)
print(D["food"])
D["quantity"] += 1
print(D)

D = {}
print(D)
D["name"] = "Bob"
D["job"] = "dev"
D["age"] = 40
print(D)
print(D["name"])

bob1 = dict(name="Bob1", job="dev1", age=41)
print(bob1)
bob2 = dict(zip(["name", "job", "age"], ["Bob2", "dev2", 42]))
print(bob2)

rec = {"name": {"first": "Bob", "last": "Smith"},
       "jobs": ["dev", "mgr"],
       "age": 40}
print(rec)
print(rec["name"])
print(rec["name"]["last"])
print(rec["jobs"])
print(rec["jobs"][-1])
rec["jobs"].append("janitor")
print(rec)

D = {'a': 1, 'b': 2, 'c': 3}
D['e'] = 99
print(D)
print('f' in D)
if 'f' not in D:
    print("missing")
    print("no, really...")

value = D.get('x', "no")
print(value)
value = D['c'] if 'c' in D else 0
print(value)
value = D['x'] if 'x' in D else 0
print(value)

ks = list(D.keys())
print(ks)
ks.reverse()
print(ks)
for key in ks:
    print(key, "=>", D[key])
print()
for key in sorted(ks):
    print(key, "=>", D[key])

x = 4
while x > 0:
    print("spam" * x)
    x -= 1

squares = [i ** 2 for i in [0, 1, 2, 3]]
print(squares)
squares = []
print(squares)
for x in [0, 1, 2, 3]:
    squares.append(x ** 2)
print(squares)
