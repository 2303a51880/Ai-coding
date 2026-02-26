def insertion_sort(arr):
    
    # Start from second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Shift larger elements
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        
    return arr


# INPUT
roll_numbers = [101, 102, 103, 105, 104, 106]

print("Insertion Sort Output:", insertion_sort(roll_numbers.copy()))






def insertion_sort(arr):
    
    # Start from second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Shift larger elements
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        
    return arr


# INPUT
roll_numbers = [101, 102, 103, 105, 104, 106]

print("Insertion Sort Output:", insertion_sort(roll_numbers.copy()))