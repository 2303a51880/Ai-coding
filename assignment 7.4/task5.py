class User:
    def __init__(self, name, age):   
        self.name = name      
        self.age = age             

    def greet(self):
        return "Hello, my name is " + self.name  


# Attempt to create and use the object
u = User("Alice", 30)
print(u.name)
print(u.greet())
