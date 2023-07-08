"""
Вам дан узел, являющийся началом связанного списка. Этот список содержит оборванный кусок и петлю.
Ваша цель — определить длину петли. Пример на картинке во вложении.
Используйте атрибут next, чтобы получить следующий узел: node.next
Узлы нельзя видоизменять!
В некоторых случаях может быть только петля без болтающегося куска.
"""


def loop_size(node):
    chain_dict = {}
    counter = 0
    while True:
        if node in chain_dict:
            return counter - chain_dict[node]
        chain_dict[node] = counter

        counter += 1
        node = node.next
