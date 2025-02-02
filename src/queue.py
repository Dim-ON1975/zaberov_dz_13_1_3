class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data  # Данные, хранящиеся в узле очереди
        self.next_node = next_node  # Ссылка на следующий элемент очереди


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None  # голова
        self.tail = None  # хвост
        self.size = 0  # счётчик размера очереди

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь.

        :param data: Данные, которые будут добавлены в очередь
        """
        # Создание нового узла с данными
        new_node = Node(data)
        # Если размер очереди пуст,
        # то добавляем в неё поочереди элементы "головы" и "хвоста",
        # представляющие собой экземпляры созданного класса.
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        # добавляем экземпляры класса в "хвост", устанавливая ссылку на новый узел
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди.
        Возвращает данные удалённого элемента.

        :return: Данные удалённого элемента.
        """
        # если количество экземпляров в очереди = 0
        if self.size == 0:
            return None
        else:
            # Получаем значение первого узла в очереди, который находится "голове".
            temp_data = self.head.data

            # Теперь головой элемент содержит узел, который был предпоследним.
            self.head = self.head.next_node

            # Если нет узла в голове очереди, то его не должно быть и в хвосте.
            # Очищаем очередь, не содержащую узлов.
            if self.head is None:
                self.tail = None

            # Уменьшаем счётчик размера очереди
            self.size -= 1

            # Возвращаем значение удалённого элемента
            return temp_data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = ''
        node = self.head
        # перебираем значения, хранящиеся в очереди по порядку.
        while node:
            result += str(node.data) + '\n'
            node = node.next_node
        # Берём строку без последнего символа переноса.
        if result != '':
            result = result[:-1]
        return result
