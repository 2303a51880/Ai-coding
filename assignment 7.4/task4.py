def process_values(values):
    results = []
    for v in values:
        try:
            result = 100 / v
            results.append(result)
        except ZeroDivisionError:
            results.append(None)  # or 0, or skip it
        except (TypeError, ValueError):
            results.append(None)  # Handle invalid types
    return results


data = [10, 5, 0, 20, 4]

# Program stops at v == 0
output = process_values(data)
print(output)
