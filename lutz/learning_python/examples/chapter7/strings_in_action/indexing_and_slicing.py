someString = 'some string'
otherString = someString[:]
print(someString is otherString)
someString += ' concat'
print(someString is otherString)
print('someString = ' + someString, 'otherString = ' + otherString, sep='\n')

S = 'abcdef'
print(S)
print(S[5:1:-1])

print('spam'[1:3], 'spam'[slice(1, 3)])
print('spam'[::-1], 'spam'[slice(None, None, -1)])
