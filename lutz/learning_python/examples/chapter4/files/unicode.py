S = "sp\xc4m"
print(S, S[2])
file = open("unidata.txt", 'w', encoding="utf-8")
file.write(S)
file.close()

text = open("unidata.txt", encoding="utf-8").read()
print(text)
print(text.encode("utf-8"))
print(text.encode("latin-1"))
print(text.encode("utf-16"))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode("utf-16"))

raw = open("unidata.txt", "rb").read()
print(raw)
print(raw.decode("utf-8"))
