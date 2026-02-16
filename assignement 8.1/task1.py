import re

def is_strong_password(password):
    """
    Returns True if the password is strong, otherwise False.
    
    Rules for a strong password:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    
    if len(password) < 8:
        return False
    
    if not re.search(r"[A-Z]", password):
        return False
    
    if not re.search(r"[a-z]", password):
        return False
    
    if not re.search(r"[0-9]", password):
        return False
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True


# ============================================================================
# GENERAL TEST CASES
# ============================================================================

def test_is_strong_password_general():
    """General test cases for is_strong_password function."""
    print("\n=== GENERAL TEST CASES ===")
    
    # Test Case 1: Valid strong password
    result1 = is_strong_password("SecurePass123!")
    print(f"Test 1 - Valid strong password 'SecurePass123!': {result1}")
    assert result1 == True, "Should return True for strong password"
    
    # Test Case 2: Password too short
    result2 = is_strong_password("Pass1!")
    print(f"Test 2 - Too short password 'Pass1!': {result2}")
    assert result2 == False, "Should return False for password < 8 chars"
    
    # Test Case 3: Missing special character
    result3 = is_strong_password("Secure123Pass")
    print(f"Test 3 - Missing special char 'Secure123Pass': {result3}")
    assert result3 == False, "Should return False without special character"
    
    print("✅ All general tests passed!\n")


# ============================================================================
# UNIT TEST CASES
# ============================================================================

def test_is_strong_password_unit():
    """Unit test cases for individual password requirements."""
    print("=== UNIT TEST CASES ===")
    
    # Test Case 1: Valid password with all requirements
    password1 = "MyPassword123!"
    result1 = is_strong_password(password1)
    print(f"Unit Test 1 - All requirements met 'MyPassword123!': {result1}")
    assert result1 == True, "Password with all requirements should be strong"
    
    # Test Case 2: Missing uppercase letter
    password2 = "mypassword123!"
    result2 = is_strong_password(password2)
    print(f"Unit Test 2 - No uppercase 'mypassword123!': {result2}")
    assert result2 == False, "Password without uppercase should fail"
    
    # Test Case 3: Missing lowercase letter
    password3 = "MYPASSWORD123!"
    result3 = is_strong_password(password3)
    print(f"Unit Test 3 - No lowercase 'MYPASSWORD123!': {result3}")
    assert result3 == False, "Password without lowercase should fail"
    
    print("✅ All unit tests passed!\n")


# ============================================================================
# PYTEST TEST CASES
# ============================================================================

def test_is_strong_password_pytest_valid():
    """Pytest test case 1: Valid strong passwords."""
    assert is_strong_password("TestPass123!") == True
    assert is_strong_password("Secure#Password456") == True
    assert is_strong_password("Complex@Pass789") == True

def test_is_strong_password_pytest_missing_requirements():
    """Pytest test case 2: Missing individual requirements."""
    assert is_strong_password("testpass123!") == False  # No uppercase
    assert is_strong_password("TESTPASS123!") == False  # No lowercase
    assert is_strong_password("TestPassword!") == False  # No digit

def test_is_strong_password_pytest_invalid():
    """Pytest test case 3: Invalid passwords."""
    assert is_strong_password("Pass1!") == False  # Too short
    assert is_strong_password("Pass123Pass") == False  # No special char
    assert is_strong_password("") == False  # Empty password


# ============================================================================
# ASSERTION TEST CASES
# ============================================================================

def test_is_strong_password_assertions():
    """Assertion test cases for is_strong_password function."""
    print("\n=== ASSERTION TEST CASES ===")
    
    # Test Case 1: Various strong passwords
    assert is_strong_password("Abc123!@") == True, "Abc123!@ should be strong"
    assert is_strong_password("ValidPass2024#") == True, "ValidPass2024# should be strong"
    assert is_strong_password("XyZ@9876") == True, "XyZ@9876 should be strong"
    print("✅ Assertion Test 1 (Strong passwords): PASSED")
    
    # Test Case 2: Missing digit
    assert is_strong_password("SecurePass!") == False, "Password without digit should be weak"
    assert is_strong_password("NoNumbers!@") == False, "Password without digit should be weak"
    assert is_strong_password("OnlyLetters!@") == False, "Password without digit should be weak"
    print("✅ Assertion Test 2 (Missing digit): PASSED")
    
    # Test Case 3: Length validation
    assert is_strong_password("Short1!") == False, "Password with < 8 chars should be weak"
    assert is_strong_password("Mini@2") == False, "Password with < 8 chars should be weak"
    assert is_strong_password("A1@") == False, "Password with < 8 chars should be weak"
    print("✅ Assertion Test 3 (Length validation): PASSED")
    
    print("✅ All assertion tests passed!\n")


# Example usage
if __name__ == "__main__":
    # Run all test suites
    test_is_strong_password_general()
    test_is_strong_password_unit()
    test_is_strong_password_assertions()
    
    print("=" * 50)
    print("INTERACTIVE PASSWORD VALIDATOR")
    print("=" * 50)
    pwd = input("Enter your password: ")
    
    if is_strong_password(pwd):
        print("Strong Password ✅")
    else:
        print("Weak Password ❌")
