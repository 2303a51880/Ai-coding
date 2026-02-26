def find_duplicates_brute(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates


# INPUT
user_ids = [101, 203, 101, 405, 203, 506]
print("Brute Force Duplicates:", find_duplicates_brute(user_ids))





def find_duplicates_optimized(data):
    seen = set()
    duplicates = set()
    
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)


# INPUT
user_ids = [101, 203, 101, 405, 203, 506]
print("Optimized Duplicates:", find_duplicates_optimized(user_ids))