class Queue:
    """
    Queue Data Structure (FIFO - First In First Out)
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Insert item at the rear."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return front item."""
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        """Return front item without removing."""
        if self.items:
            return self.items[0]
        return None

    def size(self):
        """Return number of items."""
        return len(self.items)
