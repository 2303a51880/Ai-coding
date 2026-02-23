class CafeteriaQueue:
    """
    Cafeteria Order System using Queue (FIFO).
    """

    def __init__(self):
        self.orders = []

    def place_order(self, student_name):
        """Add order to queue."""
        self.orders.append(student_name)
        print(f"Order placed by {student_name}")

    def serve_order(self):
        """Serve next student."""
        if self.orders:
            student = self.orders.pop(0)
            print(f"Serving order for {student}")
        else:
            print("No pending orders.")

    def display_orders(self):
        """Show all pending orders."""
        print("Pending Orders:", self.orders)


# Example
queue = CafeteriaQueue()
queue.place_order("Alice")
queue.place_order("Bob")
queue.serve_order()
queue.display_orders()
