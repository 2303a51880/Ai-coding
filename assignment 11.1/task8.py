from collections import deque

class DequeDS:
    """
    Double-ended Queue implementation.
    """

    def __init__(self):
        self.deque = deque()

    def add_front(self, item):
        """Insert at front."""
        self.deque.appendleft(item)

    def add_rear(self, item):
        """Insert at rear."""
        self.deque.append(item)

    def remove_front(self):
        """Remove from front."""
        if self.deque:
            return self.deque.popleft()
        return None

    def remove_rear(self):
        """Remove from rear."""
        if self.deque:
            return self.deque.pop()
        return None
