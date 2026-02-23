import heapq

class PriorityQueue:
    """
    Priority Queue using heapq (min-heap).
    """

    def __init__(self):
        self.heap = []

    def enqueue(self, priority, item):
        """Insert item with priority."""
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        """Remove highest priority item."""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def display(self):
        """Display queue contents."""
        print(self.heap)
