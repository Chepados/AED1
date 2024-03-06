from Node import Node

class Stack:
    def __init__(self):
        self.__size: int = 0
        self.__top: Node = None

    def __str__(self) -> str:
        result: str = 'Top: ['
        current: Node = self.__top
        while current is not None:
            result += ' ' + str(current)
            current = current.get_next()
        result += ' ]'
        return result

    def __len__(self) -> int:
        return self.__size

    def empty(self) -> bool:
        return self.__size == 0

    def push(self, item):
        new_node: Node = Node(item)
        new_node.set_next(self.__top)
        self.__top = new_node
        self.__size += 1

    def pop(self) -> any:
        assert not self.empty(), "Pila vacía"
        item: any = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return item

    def peek(self) -> any:
        assert not self.empty(), "Pila vacía"
        return self.__top.get_value()



