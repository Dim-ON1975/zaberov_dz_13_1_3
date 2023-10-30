"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList


def test_linked_list_1():
    # Создаем пустой односвязный список.
    ll = LinkedList()

    # Добавляем данные
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})

    assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_linked_list_2():
    # Создаем пустой односвязный список.
    ll = LinkedList()

    # Добавляем данные
    ll.insert_at_end({'id': 30})
    ll.insert_at_end({'id': 40})
    ll.insert_beginning({'id': 20})
    ll.insert_beginning({'id': 10})

    assert str(ll) == "{'id': 10} -> {'id': 20} -> {'id': 30} -> {'id': 40} -> None"


def test_linked_list_3():
    # Создаем пустой односвязный список.
    ll = LinkedList()

    assert str(ll) == 'None'
