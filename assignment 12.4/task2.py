def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# INPUT
roll_numbers = [101, 102, 103, 105, 104, 106]

print("Bubble Sort Output:", bubble_sort(roll_numbers.copy()))





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
