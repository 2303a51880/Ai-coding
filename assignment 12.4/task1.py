# Bubble Sort for sorting student exam scores

def bubble_sort(scores):
    n = len(scores)
    
    # Outer loop for passes
    for i in range(n):
        swapped = False  # To check if any swapping occurs
        
        # Inner loop for comparison
        for j in range(0, n - i - 1):
            
            # Compare adjacent elements
            if scores[j] > scores[j + 1]:
                
                # Swap if they are in wrong order
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
                swapped = True
        
        # Early termination if no swap happens
        if not swapped:
            break
            
    return scores


# -------- INPUT --------
scores = [78, 45, 90, 62, 84]

# -------- OUTPUT --------
print("Original Scores:", scores)
print("Sorted Scores:", bubble_sort(scores))