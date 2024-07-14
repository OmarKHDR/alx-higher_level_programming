#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def next_node(self):
        return self.__data

    @next_node.setter
    def next_node(self, next_node):
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("data must be an integer")
        else:
            self.__next_node = next_node

class SinglyLinkedList(Node):

    def __init__(self):
        self.__head = None
    def __str__(self) -> str:
        nodes = ""
        node = self.__head
        while node is not None:
            nodes += str(node._Node__data) +"\n"
            node = node._Node__next_node
        return nodes

    def sorted_insert(self, value):
        cur = self.__head
        node = Node(value)
        if self.__head is None or self.__head._Node__data > value:
            node._Node__next_node = self.__head
            self.__head = node

        else:
            while cur._Node__next_node is not None and cur._Node__next_node._Node__data < value:
                cur = cur._Node__next_node
            node._Node__next_node = cur._Node__next_node
            cur._Node__next_node  = node
        
            
            
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)