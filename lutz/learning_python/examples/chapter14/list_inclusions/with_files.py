f = open('some_file.txt', 'w')
f.write('one\n')
f.write('two\n')
f.write('\n')
f.write('four')

f.close()

print([line.rstrip() for line in open('some_file.txt')])
print([line for line in open('some_file.txt') if line.strip() != ''])

print([x + y for x in 'abc' if x != 'c' for y in 'lmn'])

print({i: line for i, line in enumerate(open('some_file.txt'))})
