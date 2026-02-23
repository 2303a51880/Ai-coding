class Node:
    """Node of a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly Linked List
    Methods:
        insert(data)
        display()
    """

    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert at end of list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display all elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
