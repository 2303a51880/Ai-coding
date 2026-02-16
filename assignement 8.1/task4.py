# Inventory Class – Simple Real-World Simulation

class Inventory:
    """
    A class to manage inventory with stock management operations.
    
    Methods:
        - add_item(name, quantity): Add items to inventory
        - remove_item(name, quantity): Remove items from inventory
        - get_stock(name): Get current stock of an item
        - update_stock(name, quantity): Update stock to specific quantity
        - is_available(name, quantity): Check if enough stock exists
        - list_items(): Get all items and their quantities
        - clear(): Clear entire inventory
    """
    
    def __init__(self):
        # Dictionary to store items and their quantities
        self.items = {}
    
    def add_item(self, name, quantity):
        """
        Add items to inventory.
        
        Args:
            name: Item name (string)
            quantity: Number of items to add (int > 0)
        
        Returns:
            True if successful, False otherwise
        """
        if quantity <= 0:
            return False
        
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        
        return True
    
    def remove_item(self, name, quantity):
        """
        Remove items from inventory.
        
        Args:
            name: Item name (string)
            quantity: Number of items to remove (int > 0)
        
        Returns:
            True if successful, False otherwise
        """
        if name not in self.items:
            return False
        
        if quantity <= 0:
            return False
        
        if self.items[name] < quantity:
            return False
        
        self.items[name] -= quantity
        
        # Remove item if quantity becomes 0
        if self.items[name] == 0:
            del self.items[name]
        
        return True
    
    def get_stock(self, name):
        """Get current stock of an item. Returns 0 if not found."""
        return self.items.get(name, 0)
    
    def update_stock(self, name, quantity):
        """
        Update stock to specific quantity.
        
        Returns:
            True if successful, False otherwise
        """
        if quantity < 0:
            return False
        
        if quantity == 0:
            if name in self.items:
                del self.items[name]
        else:
            self.items[name] = quantity
        
        return True
    
    def is_available(self, name, quantity):
        """
        Check if enough stock exists.
        
        Returns:
            True if available, False otherwise
        """
        return self.get_stock(name) >= quantity
    
    def list_items(self):
        """Get all items and their quantities."""
        return dict(self.items)
    
    def clear(self):
        """Clear entire inventory."""
        self.items = {}
        return True


# ============================================================================
# GENERAL TEST CASES
# ============================================================================

def test_inventory_general():
    """General test cases for Inventory class."""
    print("\n=== GENERAL TEST CASES ===")
    
    # Test Case 1: Add and retrieve items
    inv1 = Inventory()
    inv1.add_item("Apple", 10)
    inv1.add_item("Banana", 5)
    result1 = inv1.get_stock("Apple") == 10 and inv1.get_stock("Banana") == 5
    print(f"Test 1 - Add items and retrieve: {result1}")
    assert result1, "Should add and retrieve items correctly"
    
    # Test Case 2: Remove items
    inv2 = Inventory()
    inv2.add_item("Orange", 8)
    success = inv2.remove_item("Orange", 3)
    result2 = success and inv2.get_stock("Orange") == 5
    print(f"Test 2 - Remove items: {result2}")
    assert result2, "Should remove items correctly"
    
    # Test Case 3: Check availability
    inv3 = Inventory()
    inv3.add_item("Grapes", 20)
    result3 = inv3.is_available("Grapes", 10) and not inv3.is_available("Grapes", 25)
    print(f"Test 3 - Check availability: {result3}")
    assert result3, "Should check availability correctly"
    
    print("✅ All general tests passed!\n")


# ============================================================================
# UNIT TEST CASES
# ============================================================================

def test_inventory_unit():
    """Unit test cases for individual Inventory operations."""
    print("=== UNIT TEST CASES ===")
    
    # Test Case 1: Invalid quantity handling
    inv1 = Inventory()
    result1 = not inv1.add_item("Item", -5) and not inv1.add_item("Item", 0)
    print(f"Unit Test 1 - Reject invalid quantities: {result1}")
    assert result1, "Should reject negative and zero quantities on add"
    
    # Test Case 2: Remove from empty inventory
    inv2 = Inventory()
    result2 = not inv2.remove_item("NonExistent", 5)
    print(f"Unit Test 2 - Remove from empty inventory: {result2}")
    assert result2, "Should return False when removing from empty inventory"
    
    # Test Case 3: Update stock operation
    inv3 = Inventory()
    inv3.add_item("Widget", 10)
    success = inv3.update_stock("Widget", 15)
    result3 = success and inv3.get_stock("Widget") == 15
    print(f"Unit Test 3 - Update stock: {result3}")
    assert result3, "Should update stock correctly"
    
    print("✅ All unit tests passed!\n")


# ============================================================================
# PYTEST TEST CASES
# ============================================================================

def test_inventory_pytest_add_operations():
    """Pytest test case 1: Add operations."""
    inv = Inventory()
    assert inv.add_item("Item1", 5) == True
    assert inv.add_item("Item1", 3) == True  # Add more to existing
    assert inv.get_stock("Item1") == 8
    assert inv.add_item("Item2", 0) == False  # Invalid quantity

def test_inventory_pytest_remove_operations():
    """Pytest test case 2: Remove operations."""
    inv = Inventory()
    inv.add_item("Laptop", 5)
    assert inv.remove_item("Laptop", 2) == True
    assert inv.get_stock("Laptop") == 3
    assert inv.remove_item("Laptop", 10) == False  # Not enough stock
    assert inv.remove_item("NonExistent", 1) == False  # Doesn't exist

def test_inventory_pytest_availability_and_list():
    """Pytest test case 3: Availability and listing operations."""
    inv = Inventory()
    inv.add_item("Book", 7)
    inv.add_item("Pen", 20)
    assert inv.is_available("Book", 5) == True
    assert inv.is_available("Book", 10) == False
    assert inv.is_available("Missing", 1) == False
    assert len(inv.list_items()) == 2


# ============================================================================
# ASSERTION TEST CASES
# ============================================================================

def test_inventory_assertions():
    """Assertion test cases for Inventory class."""
    print("\n=== ASSERTION TEST CASES ===")
    
    # Test Case 1: Complete stock management workflow
    inv1 = Inventory()
    assert inv1.add_item("Laptop", 5) == True, "Should add laptop successfully"
    assert inv1.get_stock("Laptop") == 5, "Should have 5 laptops"
    assert inv1.add_item("Laptop", 3) == True, "Should add more laptops"
    assert inv1.get_stock("Laptop") == 8, "Should have 8 laptops total"
    assert inv1.remove_item("Laptop", 2) == True, "Should remove 2 laptops"
    assert inv1.get_stock("Laptop") == 6, "Should have 6 laptops left"
    print("✅ Assertion Test 1 (Complete workflow): PASSED")
    
    # Test Case 2: Multiple items management
    inv2 = Inventory()
    assert inv2.add_item("Mouse", 10) == True, "Should add mice"
    assert inv2.add_item("Keyboard", 8) == True, "Should add keyboards"
    assert inv2.add_item("Monitor", 4) == True, "Should add monitors"
    assert inv2.is_available("Mouse", 5) == True, "Should have 5 mice available"
    assert inv2.is_available("Keyboard", 8) == True, "Should have 8 keyboards available"
    assert inv2.is_available("Monitor", 5) == False, "Should not have 5 monitors"
    assert len(inv2.list_items()) == 3, "Should have 3 different items"
    print("✅ Assertion Test 2 (Multiple items): PASSED")
    
    # Test Case 3: Edge cases and error handling
    inv3 = Inventory()
    assert inv3.add_item("Phone", 5) == True, "Should add phones"
    assert inv3.remove_item("Phone", 5) == True, "Should remove all phones"
    assert inv3.get_stock("Phone") == 0, "Should have 0 phones (removed from dict)"
    assert inv3.update_stock("Tablet", 20) == True, "Should update new item"
    assert inv3.get_stock("Tablet") == 20, "Should have 20 tablets"
    assert inv3.update_stock("Tablet", 0) == True, "Should set to 0"
    assert inv3.get_stock("Tablet") == 0, "Should have 0 tablets"
    assert inv3.add_item("Item", -5) == False, "Should reject negative quantity"
    print("✅ Assertion Test 3 (Edge cases): PASSED")
    
    print("✅ All assertion tests passed!\n")


# Example Usage
if __name__ == "__main__":
    # Run all test suites
    test_inventory_general()
    test_inventory_unit()
    test_inventory_assertions()
    
    print("=" * 50)
    print("INTERACTIVE INVENTORY MANAGEMENT")
    print("=" * 50)
    
    inventory = Inventory()
    
    # Demo operations
    inventory.add_item("Apple", 10)
    inventory.add_item("Banana", 5)
    
    print(f"\nInitial inventory: {inventory.list_items()}")
    
    inventory.remove_item("Apple", 3)
    print(f"After removing 3 apples: {inventory.list_items()}")
    
    print(f"\nStock of Apple: {inventory.get_stock('Apple')}")
    print(f"Stock of Banana: {inventory.get_stock('Banana')}")
    print(f"Stock of Orange: {inventory.get_stock('Orange')}")
    
    print(f"\nIs 5 Apples available? {inventory.is_available('Apple', 5)}")
    print(f"Is 10 Bananas available? {inventory.is_available('Banana', 10)}")