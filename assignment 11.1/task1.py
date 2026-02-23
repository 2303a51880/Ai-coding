class Stack:
    """
    Stack Data Structure (LIFO - Last In First Out)
    Methods:
        push(item)  - Add item to top
        pop()       - Remove and return top item
        peek()      - Return top item without removing
        is_empty()  - Check if stack is empty
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Return True if stack is empty."""
        return len(self.items) == 0
