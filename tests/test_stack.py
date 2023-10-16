"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import pytest

from src.stack import Node, Stack


def test_class_node():
    """Тест работы класса Node"""
    n1 = Node(5, None)
    n2 = Node('a', n1)
    assert n1.data == 5
    assert n2.data == 'a'
    assert id(n1) == id(n2.next_node)


def test_class_stack():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    stack.push('data4')
    assert stack.top.data == 'data4'
    assert stack.top.next_node.data == 'data3'
    assert stack.top.next_node.next_node.data == 'data2'
    assert stack.top.next_node.next_node.next_node.data == 'data1'
    assert stack.top.next_node.next_node.next_node.next_node is None
    with pytest.raises(AttributeError) as exif:
        str(stack.top.next_node.next_node.next_node.next_node.data)
    assert "'NoneType' object has no attribute 'data'" in str(exif.value)
