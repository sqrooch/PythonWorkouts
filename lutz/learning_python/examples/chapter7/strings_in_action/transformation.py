print(str('spam'), repr('spam'))
print(ord('s'), chr(115))

binary = '11010'
decimal = 0
# ord('1') = 49, ord('0') = 48
while binary != '':
    decimal = (decimal << 1) + (ord(binary[0]) - ord('0'))
    binary = binary[1:]
print(decimal)
