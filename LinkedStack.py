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

    def __iter__(self):
        if self.empty():
            return iter()
        else:
            list_form = []
            current_node = self.__top
            while current_node != None:
                list_form.append(current_node.get_value())
                current_node = current_node.get_next()

        return iter(list_form)


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

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    for node in stack:
        print(node)

    print(list(stack))

if __name__ == "__main__":
    main()
