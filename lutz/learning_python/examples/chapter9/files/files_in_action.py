myFile = open(r'myFile.txt', 'w')
myFile.write(r'Hello text file\n')
myFile.write(r'Goodbye text file')
myFile.close()

myFile = open(r'myFile.txt')
print(myFile.read())

for line in open(r'myFile.txt'):
    print(line, end='')

myFile.close()
