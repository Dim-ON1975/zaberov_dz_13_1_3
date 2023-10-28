"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest

from src.queue import Node, Queue


def test_class_node():
    """Тест работы класса Node"""
    n1 = Node(5, None)
    n2 = Node('a', n1)
    assert n1.data == 5
    assert n2.data == 'a'
    assert id(n1) == id(n2.next_node)


def test_class_queue():
    queue = Queue()

    # Магический метод __str__ возвращает пустую строку
    assert str(Queue()) == ""

    # Добавляем данные в очередь
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    queue.enqueue('data4')
    queue.enqueue('data5')
    queue.enqueue('data6')

    # Проверяем очередность хранения данных
    assert queue.head.data == 'data1'
    assert queue.head.next_node.data == 'data2'
    assert queue.head.next_node.next_node.data == 'data3'
    assert queue.head.next_node.next_node.next_node.data == 'data4'
    assert queue.head.next_node.next_node.next_node.next_node.data == 'data5'
    assert queue.tail.data == 'data6'
    assert queue.tail.next_node is None
    with pytest.raises(AttributeError) as exif:
        str(queue.tail.next_node.data)
    assert "'NoneType' object has no attribute 'data'" in str(exif.value)

    # Проверяем магический метод __str__
    assert str(queue) == 'data1\ndata2\ndata3\ndata4\ndata5\ndata6'

    # Проверяем удаление элементов из очереди
    # и возвращение удалённого элемента очереди в виде значения.
    assert queue.dequeue() == 'data1'
    assert queue.size == 5
    assert queue.head.data == 'data2'
    assert str(queue) == 'data2\ndata3\ndata4\ndata5\ndata6'
    # Удаляем все элементы в очереди
    while queue.head:
        queue.dequeue()
    # Вывод при отсутствии элементов
    assert queue.dequeue() is None

