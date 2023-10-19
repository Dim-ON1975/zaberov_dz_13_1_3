from src.stack import Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стек стал пустой
    assert stack.top is None

    # pop() удаляет элемент и возвращает данные удалённого элемента.
    assert data == 'data1'

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    assert stack.top.data == 'data1'

    # данные удалённого элемента
    assert data == 'data2'
