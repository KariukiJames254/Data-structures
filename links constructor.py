class Node:
    def __int__(self, value):
        self.value = value
        self.next = None


class myLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.next = new_node
            self.head = new_node
            self.length += 1


my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.print_list()
