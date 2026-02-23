class ProductSearch:
    """
    Product Search using Hash Table.
    """

    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name):
        """Add product."""
        self.products[product_id] = name

    def search_product(self, product_id):
        """Search product by ID."""
        return self.products.get(product_id, "Product not found")

    def remove_product(self, product_id):
        """Remove product."""
        if product_id in self.products:
            del self.products[product_id]


# Example
store = ProductSearch()
store.add_product(101, "Laptop")
store.add_product(102, "Smartphone")

print(store.search_product(101))
store.remove_product(102)
