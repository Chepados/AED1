class Node:
    def __init__(self, value):
        self.__value: any = value
        self.__next: Node = None

    def __str__(self) -> str:
        return str(self.__value)

    def get_value(self) -> any:
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next


if __name__ == '__main__':
    myNode = Node('Hi')
    print(myNode)
    myOtherNode = Node(777)
    print(myOtherNode)
    myNode.set_value('By')
    myNode.set_next(myOtherNode)
    print(myNode)
    print(myNode.get_next())
