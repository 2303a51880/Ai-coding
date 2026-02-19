def divide_numbers(dividend, divisor):
    """
    Divides two numbers and returns the result.

    Parameters:
        dividend (int or float): The number to be divided.
        divisor (int or float): The number to divide by.

    Returns:
        float: The division result.

    Raises:
        ZeroDivisionError: If divisor is zero.
        TypeError: If inputs are not numeric.
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both inputs must be numeric.")

    if divisor == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    return dividend / divisor


try:
    result = divide_numbers(10, 2)
    print(result)
except Exception as error:
    print("Error:", error)
