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


def test_to_list():
    """
    Тестирование метода test_to_list,
    возвращающего список с данными.
    """
    ll = LinkedList()

    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})

    # метод to_list()
    lst = ll.to_list()
    assert lst == [{'id': 0, 'username': 'serebro'},
                   {'id': 1, 'username': 'lazzy508509'},
                   {'id': 2, 'username': 'mik.roz'},
                   {'id': 3, 'username': 'mosh_s'}]


def test_get_data_by_id(capsys):
    """
    Тестирование метода test_get_data_by_id,
    возвращающего словарь по индексу.
    """
    ll = LinkedList()

    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})

    user_data = ll.get_data_by_id(3)
    assert user_data == {'id': 3, 'username': 'mosh_s'}

    # работа блока try/except
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    user_data = ll.get_data_by_id(2)

    # Используем фикстуру pytest - capsys builtin,
    # которая обеспечивает две функциональные возможности:
    # позволяет получить stdout и stderr из некоторого кода,
    # и временно отключить захват вывода (print).
    out, err = capsys.readouterr()
    assert out == ('Данные не являются словарем или в словаре нет id.\n'
                   'Данные не являются словарем или в словаре нет id.\n')
    assert err == ''

    # Функция возвращает словарь с id == 2.
    assert user_data == {'id': 2, 'username': 'mosh_s'}

