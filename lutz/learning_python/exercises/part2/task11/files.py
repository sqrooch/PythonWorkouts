inputPhrase = open('myFile.txt', 'w')
inputPhrase.write('Hello, sqrooch!!!')
inputPhrase.close()

outputPhrase = open('myFile.txt')
print(outputPhrase.read())
outputPhrase.close()

with open('myFile.txt') as otherPhrase:
    print(otherPhrase.read())
