import json

someDict = {'a': 1, 'b': 2, 'c': 3}

s = json.dumps(someDict)
o = json.loads(s)
print(o)
print(someDict == o)

json.dump(someDict, fp=open('testJson.txt', 'w'), indent=4)
print(open('testJson.txt').read())

print(json.load(open('testJson.txt')))
