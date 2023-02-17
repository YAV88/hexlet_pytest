def reverse_string(string):
    # создаем пустой стек
    stack = []

    # кладем каждый символ строки на стек
    for char in string:
        stack.append(char)

    # извлекаем символы из стека и добавляем их в новую строку
    reversed_string = ""
    while len(stack) > 0:
        reversed_string += stack.pop()

    return reversed_string
