import pytest


def test_reverse_string():
    stack = []  # В Python стек реализован через список
    not stack  # Список пуст
    # True
    stack.append(1)  # [1]
    stack.append(2)  # [1, 2]
    stack.append(3)  # [1, 2, 3]
    not stack  # Список не пустой
    # False
    stack
    # [1, 2, 3]
    stack.pop()  # В стеке [1, 2]
    # 3
    stack.pop()  # В стеке [1]
    # 2
    stack.pop()  # В стеке пусто
    # 1
    not stack
    # True


def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'


def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'


# Следующим тестом будет тест на дополнительные функции стека.
# К таким у нас относится проверка на пустоту
def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


# Поведение функции pop(), когда в стеке нет ни одного элемента
def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
