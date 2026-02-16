# Date Validation & Formatting – Data Validation

from datetime import datetime

def validate_and_format_date(date_str):
    """
    Validates and formats a date string.
    
    Accepts multiple date formats:
    - MM/DD/YYYY
    - YYYY-MM-DD
    - DD-MM-YYYY
    - MM-DD-YYYY
    
    Returns a dictionary with:
    - 'valid': True if valid date, False otherwise
    - 'formatted': Formatted date in YYYY-MM-DD format (if valid)
    - 'message': Description or error message
    
    Args:
        date_str: Date string to validate
    
    Returns:
        Dictionary with validation results
    """
    
    if not date_str or not isinstance(date_str, str):
        return {
            'valid': False,
            'formatted': None,
            'message': 'Invalid input: must be a non-empty string'
        }
    
    # List of formats to try
    formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y"]
    
    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_str.strip(), fmt)
            formatted_date = date_obj.strftime("%Y-%m-%d")
            
            return {
                'valid': True,
                'formatted': formatted_date,
                'message': f'Valid date in {fmt} format',
                'original_format': fmt
            }
        except ValueError:
            continue
    
    # If no format matched
    return {
        'valid': False,
        'formatted': None,
        'message': 'Invalid date format. Accepted formats: MM/DD/YYYY, YYYY-MM-DD, DD-MM-YYYY, MM-DD-YYYY'
    }


# ============================================================================
# GENERAL TEST CASES
# ============================================================================

def test_validate_and_format_date_general():
    """General test cases for validate_and_format_date function."""
    print("\n=== GENERAL TEST CASES ===")
    
    # Test Case 1: Valid date in MM/DD/YYYY format
    result1 = validate_and_format_date("12/25/2023")
    print(f"Test 1 - Valid MM/DD/YYYY '12/25/2023': {result1['valid']} -> {result1['formatted']}")
    assert result1['valid'] == True and result1['formatted'] == "2023-12-25", "Should validate MM/DD/YYYY format"
    
    # Test Case 2: Valid date in YYYY-MM-DD format
    result2 = validate_and_format_date("2024-01-15")
    print(f"Test 2 - Valid YYYY-MM-DD '2024-01-15': {result2['valid']} -> {result2['formatted']}")
    assert result2['valid'] == True and result2['formatted'] == "2024-01-15", "Should validate YYYY-MM-DD format"
    
    # Test Case 3: Invalid date
    result3 = validate_and_format_date("13/32/2023")
    print(f"Test 3 - Invalid date '13/32/2023': {result3['valid']}")
    assert result3['valid'] == False, "Should reject invalid date"
    
    print("✅ All general tests passed!\n")


# ============================================================================
# UNIT TEST CASES
# ============================================================================

def test_validate_and_format_date_unit():
    """Unit test cases for individual date validation features."""
    print("=== UNIT TEST CASES ===")
    
    # Test Case 1: Format conversion accuracy
    result1 = validate_and_format_date("01/01/2020")
    print(f"Unit Test 1 - Format conversion '01/01/2020': {result1['formatted']}")
    assert result1['formatted'] == "2020-01-01", "Should format correctly to YYYY-MM-DD"
    
    # Test Case 2: Leap year validation
    result2 = validate_and_format_date("02/29/2020")
    print(f"Unit Test 2 - Leap year '02/29/2020': {result2['valid']}")
    assert result2['valid'] == True, "Should accept valid leap year date"
    
    # Test Case 3: Invalid leap year
    result3 = validate_and_format_date("02/29/2021")
    print(f"Unit Test 3 - Invalid leap year '02/29/2021': {result3['valid']}")
    assert result3['valid'] == False, "Should reject invalid leap year date"
    
    print("✅ All unit tests passed!\n")


# ============================================================================
# PYTEST TEST CASES
# ============================================================================

def test_validate_and_format_date_pytest_valid_formats():
    """Pytest test case 1: Valid date formats."""
    assert validate_and_format_date("12/31/2023")['valid'] == True
    assert validate_and_format_date("2023-12-31")['valid'] == True
    assert validate_and_format_date("31-12-2023")['valid'] == True

def test_validate_and_format_date_pytest_formatting():
    """Pytest test case 2: Correct formatting output."""
    assert validate_and_format_date("06/15/2022")['formatted'] == "2022-06-15"
    assert validate_and_format_date("2021-03-10")['formatted'] == "2021-03-10"
    assert validate_and_format_date("25-05-2020")['formatted'] == "2020-05-25"

def test_validate_and_format_date_pytest_invalid_dates():
    """Pytest test case 3: Invalid and edge case dates."""
    assert validate_and_format_date("13/01/2023")['valid'] == False  # Invalid month
    assert validate_and_format_date("02/30/2023")['valid'] == False  # Invalid day
    assert validate_and_format_date("")['valid'] == False  # Empty string


# ============================================================================
# ASSERTION TEST CASES
# ============================================================================

def test_validate_and_format_date_assertions():
    """Assertion test cases for validate_and_format_date function."""
    print("\n=== ASSERTION TEST CASES ===")
    
    # Test Case 1: Multiple valid format conversions
    result1a = validate_and_format_date("03/17/2025")
    assert result1a['valid'] == True, "Should validate MM/DD/YYYY format"
    assert result1a['formatted'] == "2025-03-17", "Should format to YYYY-MM-DD"
    
    result1b = validate_and_format_date("2025-03-17")
    assert result1b['valid'] == True, "Should validate YYYY-MM-DD format"
    assert result1b['formatted'] == "2025-03-17", "Should keep YYYY-MM-DD format"
    
    result1c = validate_and_format_date("17-03-2025")
    assert result1c['valid'] == True, "Should validate DD-MM-YYYY format"
    assert result1c['formatted'] == "2025-03-17", "Should convert DD-MM-YYYY to YYYY-MM-DD"
    
    print("✅ Assertion Test 1 (Multiple valid formats): PASSED")
    
    # Test Case 2: Boundary and edge case dates
    result2a = validate_and_format_date("01/01/2000")
    assert result2a['valid'] == True, "Should accept 01/01/2000"
    assert result2a['formatted'] == "2000-01-01", "Should format correctly"
    
    result2b = validate_and_format_date("12/31/2099")
    assert result2b['valid'] == True, "Should accept 12/31/2099"
    assert result2b['formatted'] == "2099-12-31", "Should format correctly"
    
    result2c = validate_and_format_date("02/29/2000")
    assert result2c['valid'] == True, "Should accept leap day in leap year"
    assert result2c['formatted'] == "2000-02-29", "Should format leap day correctly"
    
    print("✅ Assertion Test 2 (Boundary dates): PASSED")
    
    # Test Case 3: Invalid dates and error handling
    result3a = validate_and_format_date("00/15/2023")
    assert result3a['valid'] == False, "Should reject month 00"
    
    result3b = validate_and_format_date("13/15/2023")
    assert result3b['valid'] == False, "Should reject month 13"
    
    result3c = validate_and_format_date("02/30/2023")
    assert result3c['valid'] == False, "Should reject Feb 30"
    
    result3d = validate_and_format_date("   ")
    assert result3d['valid'] == False, "Should reject whitespace only"
    
    result3e = validate_and_format_date(None)
    assert result3e['valid'] == False, "Should reject None input"
    
    print("✅ Assertion Test 3 (Invalid dates): PASSED")
    
    print("✅ All assertion tests passed!\n")


# Example usage
if __name__ == "__main__":
    # Run all test suites
    test_validate_and_format_date_general()
    test_validate_and_format_date_unit()
    test_validate_and_format_date_assertions()
    
    print("=" * 60)
    print("INTERACTIVE DATE VALIDATOR & FORMATTER")
    print("=" * 60)
    print("Accepted formats: MM/DD/YYYY, YYYY-MM-DD, DD-MM-YYYY, MM-DD-YYYY")
    print("-" * 60)
    
    date_input = input("Enter a date: ")
    
    result = validate_and_format_date(date_input)
    
    print(f"\nValidation Result: {'✅ VALID' if result['valid'] else '❌ INVALID'}")
    if result['valid']:
        print(f"Original format: {result.get('original_format', 'Unknown')}")
        print(f"Formatted date: {result['formatted']}")
    print(f"Message: {result['message']}")
