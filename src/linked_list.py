class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка
        """
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)
        self._size += 1

    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка
        """
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self._size += 1

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += ' None'
        return ll_string.strip()
