def classify_number(n):
    """
    Classifies a number based on multiple criteria using loops.
    
    Returns a dictionary with classifications:
    - sign: "positive", "negative", or "zero"
    - parity: "even" or "odd"
    - digit_sum: sum of digits
    - is_prime: True if prime, False otherwise
    """
    
    classifications = {}
    
    # Classification 1: Sign (using loop for demonstration)
    sign = None
    if n > 0:
        sign = "positive"
    elif n < 0:
        sign = "negative"
    else:
        sign = "zero"
    classifications["sign"] = sign
    
    # Classification 2: Parity
    parity = "even" if n % 2 == 0 else "odd"
    classifications["parity"] = parity
    
    # Classification 3: Digit sum (using loop)
    digit_sum = 0
    temp = abs(n)
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    classifications["digit_sum"] = digit_sum
    
    # Classification 4: Prime check (using loop)
    is_prime = False
    if n > 1:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    classifications["is_prime"] = is_prime
    
    return classifications


# ============================================================================
# GENERAL TEST CASES
# ============================================================================

def test_classify_number_general():
    """General test cases for classify_number function."""
    print("\n=== GENERAL TEST CASES ===")
    
    # Test Case 1: Positive even number
    result1 = classify_number(8)
    print(f"Test 1 - Number 8: {result1}")
    assert result1["sign"] == "positive", "8 should be positive"
    assert result1["parity"] == "even", "8 should be even"
    
    # Test Case 2: Negative odd number
    result2 = classify_number(-7)
    print(f"Test 2 - Number -7: {result2}")
    assert result2["sign"] == "negative", "-7 should be negative"
    assert result2["parity"] == "odd", "-7 should be odd"
    
    # Test Case 3: Zero
    result3 = classify_number(0)
    print(f"Test 3 - Number 0: {result3}")
    assert result3["sign"] == "zero", "0 should be zero"
    assert result3["parity"] == "even", "0 should be even"
    
    print("✅ All general tests passed!\n")


# ============================================================================
# UNIT TEST CASES
# ============================================================================

def test_classify_number_unit():
    """Unit test cases for individual classifications."""
    print("=== UNIT TEST CASES ===")
    
    # Test Case 1: Digit sum calculation
    result1 = classify_number(123)
    print(f"Unit Test 1 - Digit sum of 123: {result1['digit_sum']}")
    assert result1["digit_sum"] == 6, "Digit sum of 123 should be 1+2+3=6"
    
    # Test Case 2: Prime number detection
    result2 = classify_number(17)
    print(f"Unit Test 2 - Is 17 prime?: {result2['is_prime']}")
    assert result2["is_prime"] == True, "17 should be prime"
    
    # Test Case 3: Non-prime number
    result3 = classify_number(15)
    print(f"Unit Test 3 - Is 15 prime?: {result3['is_prime']}")
    assert result3["is_prime"] == False, "15 should not be prime"
    
    print("✅ All unit tests passed!\n")


# ============================================================================
# PYTEST TEST CASES
# ============================================================================

def test_classify_number_pytest_sign():
    """Pytest test case 1: Sign classification."""
    assert classify_number(42)["sign"] == "positive"
    assert classify_number(-10)["sign"] == "negative"
    assert classify_number(0)["sign"] == "zero"

def test_classify_number_pytest_parity():
    """Pytest test case 2: Parity classification."""
    assert classify_number(4)["parity"] == "even"
    assert classify_number(9)["parity"] == "odd"
    assert classify_number(-6)["parity"] == "even"

def test_classify_number_pytest_digit_and_prime():
    """Pytest test case 3: Digit sum and prime classification."""
    assert classify_number(111)["digit_sum"] == 3
    assert classify_number(2)["is_prime"] == True
    assert classify_number(20)["is_prime"] == False


# ============================================================================
# ASSERTION TEST CASES
# ============================================================================

def test_classify_number_assertions():
    """Assertion test cases for classify_number function."""
    print("\n=== ASSERTION TEST CASES ===")
    
    # Test Case 1: Complete classification of positive prime
    result1 = classify_number(13)
    assert result1["sign"] == "positive", "13 should be positive"
    assert result1["parity"] == "odd", "13 should be odd"
    assert result1["is_prime"] == True, "13 should be prime"
    print("✅ Assertion Test 1 (Positive prime 13): PASSED")
    
    # Test Case 2: Negative number with digit sum
    result2 = classify_number(-45)
    assert result2["sign"] == "negative", "-45 should be negative"
    assert result2["digit_sum"] == 9, "Digit sum of 45 should be 9"
    assert result2["is_prime"] == False, "45 should not be prime"
    print("✅ Assertion Test 2 (Negative -45): PASSED")
    
    # Test Case 3: Even composite number
    result3 = classify_number(100)
    assert result3["sign"] == "positive", "100 should be positive"
    assert result3["parity"] == "even", "100 should be even"
    assert result3["digit_sum"] == 1, "Digit sum of 100 should be 1"
    assert result3["is_prime"] == False, "100 should not be prime"
    print("✅ Assertion Test 3 (Even composite 100): PASSED")
    
    print("✅ All assertion tests passed!\n")


# Example usage
if __name__ == "__main__":
    # Run all test suites
    test_classify_number_general()
    test_classify_number_unit()
    test_classify_number_assertions()
    
    print("=" * 50)
    print("INTERACTIVE NUMBER CLASSIFIER")
    print("=" * 50)
    
    n = 3  # how many valid numbers you want to classify
    count = 0
    
    while count < n:
        user_input = input(f"Enter number {count + 1}: ")
        
        # Handle empty input
        if user_input.strip() == "":
            print("Invalid input! Please enter a number.\n")
            continue
        
        try:
            num = int(user_input)
        except ValueError:
            print("Invalid input! Only integers are allowed.\n")
            continue
        
        # Classify and display results
        result = classify_number(num)
        print(f"\nClassification of {num}:")
        print(f"  Sign: {result['sign']}")
        print(f"  Parity: {result['parity']}")
        print(f"  Digit Sum: {result['digit_sum']}")
        print(f"  Is Prime: {result['is_prime']}")
        print("-" * 40)
        
        count += 1
