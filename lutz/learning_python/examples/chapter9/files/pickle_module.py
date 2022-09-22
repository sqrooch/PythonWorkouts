import pickle

someDict = {'a': 1, 'b': 2, 'c': 3}
f = open('datafile.pkl', 'wb')
pickle.dump(someDict, f)
f.close()

f = open('datafile.pkl', 'rb')
print(f.read())
f.close()

f = open('datafile.pkl', 'rb')
print(pickle.load(f))
f.close()
