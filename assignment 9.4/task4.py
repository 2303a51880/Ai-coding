def analyze_numbers(nums):
    """Compute comprehensive statistics for a list of numbers in a single pass.
    
    This function calculates multiple statistics (sum, average, min, max, and a
    derived metric) by iterating through the list once instead of using multiple
    passes. All state variables are updated simultaneously during iteration.
    
    The function initializes smallest and largest to the first element, avoiding
    sentinels but implicitly assuming a non-empty list. A derived metric combines
    each value's offset from minimum with its position for additional analysis.
    
    Args:
        nums (list): A non-empty list of numeric values. Function assumes valid
                     numbers and performs no error checking.
    
    Returns:
        dict: Dictionary containing computed statistics:
            - 'sum' (numeric): Total sum of all numbers
            - 'avg' (float): Arithmetic mean of the numbers
            - 'min' (numeric): Smallest value in the list
            - 'max' (numeric): Largest value in the list
            - 'derived' (numeric): Cumulative metric combining each value's offset
                                   from minimum with its position index
    
    Example:
        >>> analyze_numbers([1, 2, 3, 4, 5])
        {'sum': 15, 'avg': 3.0, 'min': 1, 'max': 5, 'derived': 20}
        >>> analyze_numbers([10.0, 20.0])
        {'sum': 30.0, 'avg': 15.0, 'min': 10.0, 'max': 20.0, 'derived': 10.0}
    """
    total = 0
    smallest = largest = nums[0]
    index = 0
    derived = 0

    for n in nums:
        total += n

        if n < smallest:
            smallest = n

        if n > largest:
            largest = n

        derived += (n - smallest) * (index + 1)

        index += 1

    average = total / index

    return {
        "sum": total,
        "avg": average,
        "min": smallest,
        "max": largest,
        "derived": derived
    }


def main():
    """Main entry point for the number analysis tool.
    
    Prompts the user to enter space-separated numbers and displays
    comprehensive statistics including sum, average, min, max, and derived metrics.
    """
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    print(analyze_numbers(nums))


if __name__ == "__main__":
    main()
