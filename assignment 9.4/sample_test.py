"""Sample module for testing docstring injection."""

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def calculate_sum(a, b):
    return a + b

class Calculator:
    
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, num):
        self.value += num
        return self.value
    
    def multiply(self, num):
        self.value *= num
        return self.value

def process_data(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result

class DataProcessor:
    
    def __init__(self, name):
        self.name = name
    
    def process(self, items):
        return [x.upper() if isinstance(x, str) else x for x in items]
    
    def filter_items(self, items, condition):
        return [x for x in items if condition(x)]

async def async_fetch(url):
    pass
