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
        Принимает данные (словарь) и добавляет узел
        в начало связанного списка.
        """
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)
        self._size += 1

    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь)
        и добавляет узел в конец связанного списка.
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

    def to_list(self) -> list:
        """
        Возвращает список с данными, содержащимися в LinkedList.
        """
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def get_data_by_id(self, id_: int) -> object:
        """
        Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному.
        """
        current_node = self.head
        while current_node:
            try:
                if current_node.data['id'] == id_:
                    return current_node.data
                else:
                    current_node = current_node.next
            except TypeError:
                current_node = current_node.next
                print('Данные не являются словарем или в словаре нет id.')
                continue

