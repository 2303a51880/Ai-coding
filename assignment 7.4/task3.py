def read_data():
    with open("/Ai coding/assignment 7.4/data.txt", "r") as file:
        data = file.read()
    return data


# Simulating repeated file access
for _ in range(10000):
    read_data()
