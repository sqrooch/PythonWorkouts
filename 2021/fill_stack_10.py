"""
Эмулирует обычное поведение стэка.
"""

stack = [0] * 10
print(stack)
top = 0
x = int(input('Please, enter a number here and press Enter: '))
while x != 0:
    stack[top] = x
    top += 1
    x = int(input('Please, enter a number here and press Enter: '))
    print(stack)

for k in range(len(stack) - 1, -1, -1):
    print(stack[k], end=' ')
