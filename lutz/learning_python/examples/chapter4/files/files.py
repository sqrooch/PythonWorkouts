f = open("data.txt", 'w')
f.write("Hello\n")
f.write("dear\n")
f.write("Sqrooch!")
f.close()

f = open("data.txt")
text = f.read()
print(text)
print(text.split())
for line in open("data.txt"):
    print(line)

print(dir(f))
print(type(f))
print(help(f.flush))
f.close()
