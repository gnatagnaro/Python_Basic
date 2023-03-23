from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:

        """
        Переопределение метода __str__ для красивого вывода списка

        :return: str
        """

        return f'Node: {self.value}'


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:

        """
        Переопределение метода __str__ для красивого вывода списка

        :return: str
        """

        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'[{" ".join(values)}]'
        return 'LinkedList []'

    def __iter__(self):

        """
        Переопределение метода __iter__ для итерации по списку

        :return:
        """

        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def get(self, index: Any) -> Optional[int]:  # или просто int?

        """
        Получение элемента по индексу

        :param index:
        :return: current_node.value
        """

        if index >= self.length or index < 0:
            raise IndexError('Ошибка индекса')

        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.value

    def append(self, elem: Any) -> None:

        """
        Добавление элемента в конец списка

        :param elem:
        :return: None
        """

        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.length += 1

    def remove(self, index: int) -> None:

        """
        Удаление элемента по индексу

        :param index:
        :return: None
        """

        cur_node = self.head
        cur_index = 0
        if self.length == 0 or index >= self.length:
            raise IndexError('Ошибка индекса')

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("Текущий список:", my_list)
print("Получение третьего элемента:", my_list.get(2))
print("Удаление второго элемента.")
my_list.remove(1)
print("Новый список:", my_list)

print("Итерация по списку:")
for elem in my_list:
    print(elem)
