def calculate_total(price, tax):
    """Return the total price after applying tax."""
    total = price + price * tax
    return total


def print_receipt(name, price, tax):
    """Print a simple receipt for the given customer."""
    print("Customer:", name)
    total = calculate_total(price, tax)
    print("Total amount:", total)


if __name__ == "__main__":
    price = 100
    tax = 0.1

    print_receipt("John", price, tax)