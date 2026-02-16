# Anagram Checker – String Analysis

import string

def clean_text(text):
    """
    Convert to lowercase and remove spaces & punctuation.
    """
    text = text.lower()
    cleaned = ""
    
    for char in text:
        if char.isalnum():  # Keep only letters and numbers
            cleaned += char
    
    return cleaned


# Anagram Checker – String Analysis

import string

def clean_text(text):
    """
    Convert to lowercase and remove spaces & punctuation.
    """
    text = text.lower()
    cleaned = ""
    
    for char in text:
        if char.isalnum():  # Keep only letters and numbers
            cleaned += char
    
    return cleaned


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams of each other.
    
    An anagram is a word formed by rearranging the letters of another word,
    using all the original letters exactly once.
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        True if strings are anagrams, False otherwise
    """
    # Clean both strings
    str1_cleaned = clean_text(str1)
    str2_cleaned = clean_text(str2)
    
    # Edge case: both empty after cleaning
    if str1_cleaned == "" and str2_cleaned == "":
        return False
    
    # Edge case: identical words (not true anagrams)
    if str1_cleaned == str2_cleaned and str1_cleaned != "":
        return False
    
    # Compare sorted characters
    return sorted(str1_cleaned) == sorted(str2_cleaned)


# ============================================================================
# GENERAL TEST CASES
# ============================================================================

def test_is_anagram_general():
    """General test cases for is_anagram function."""
    print("\n=== GENERAL TEST CASES ===")
    
    # Test Case 1: Classic anagram
    result1 = is_anagram("listen", "silent")
    print(f"Test 1 - 'listen' and 'silent': {result1}")
    assert result1 == True, "listen and silent should be anagrams"
    
    # Test Case 2: Not an anagram
    result2 = is_anagram("hello", "world")
    print(f"Test 2 - 'hello' and 'world': {result2}")
    assert result2 == False, "hello and world should not be anagrams"
    
    # Test Case 3: Case insensitive anagram
    result3 = is_anagram("The Eyes", "They See")
    print(f"Test 3 - 'The Eyes' and 'They See': {result3}")
    assert result3 == True, "The Eyes and They See should be anagrams"
    
    print("✅ All general tests passed!\n")


# ============================================================================
# UNIT TEST CASES
# ============================================================================

def test_is_anagram_unit():
    """Unit test cases for individual anagram features."""
    print("=== UNIT TEST CASES ===")
    
    # Test Case 1: Simple single-letter words
    result1 = is_anagram("a", "a")
    print(f"Unit Test 1 - Same single letter 'a' and 'a': {result1}")
    assert result1 == False, "Identical strings should return False"
    
    # Test Case 2: Anagram with special characters/spaces
    result2 = is_anagram("Dormitory", "Dirty room")
    print(f"Unit Test 2 - 'Dormitory' and 'Dirty room': {result2}")
    assert result2 == True, "Dormitory and Dirty room should be anagrams"
    
    # Test Case 3: Different lengths
    result3 = is_anagram("cat", "dog")
    print(f"Unit Test 3 - Different length 'cat' and 'dog': {result3}")
    assert result3 == False, "Different strings should not be anagrams"
    
    print("✅ All unit tests passed!\n")


# ============================================================================
# PYTEST TEST CASES
# ============================================================================

def test_is_anagram_pytest_valid_anagrams():
    """Pytest test case 1: Valid anagrams."""
    assert is_anagram("act", "cat") == True
    assert is_anagram("evil", "vile") == True
    assert is_anagram("Astronomer", "Moon starer") == True

def test_is_anagram_pytest_invalid_anagrams():
    """Pytest test case 2: Invalid anagrams."""
    assert is_anagram("python", "java") == False
    assert is_anagram("abc", "def") == False
    assert is_anagram("test", "best") == False

def test_is_anagram_pytest_edge_cases():
    """Pytest test case 3: Edge cases."""
    assert is_anagram("", "") == False
    assert is_anagram("a", "b") == False
    assert is_anagram("  ", "  ") == False


# ============================================================================
# ASSERTION TEST CASES
# ============================================================================

def test_is_anagram_assertions():
    """Assertion test cases for is_anagram function."""
    print("\n=== ASSERTION TEST CASES ===")
    
    # Test Case 1: Classic famous anagrams
    assert is_anagram("Astronomer", "Moon starer") == True, "Astronomer and Moon starer should be anagrams"
    assert is_anagram("The Eyes", "They See") == True, "The Eyes and They See should be anagrams"
    assert is_anagram("Eleven plus two", "Twelve plus one") == True, "Eleven plus two and Twelve plus one should be anagrams"
    print("✅ Assertion Test 1 (Famous anagrams): PASSED")
    
    # Test Case 2: Non-anagrams with common letters
    assert is_anagram("writing", "reading") == False, "writing and reading should not be anagrams"
    assert is_anagram("silent", "listen2") == False, "silent and listen2 should not be anagrams"
    assert is_anagram("heart", "earth") == False, "heart and earth should not be anagrams"
    print("✅ Assertion Test 2 (Non-anagrams): PASSED")
    
    # Test Case 3: Special cases with numbers and punctuation
    assert is_anagram("a1b2c3", "3c2b1a") == True, "a1b2c3 and 3c2b1a should be anagrams"
    assert is_anagram("hello!", "o!lleh") == True, "hello! and o!lleh should be anagrams"
    assert is_anagram("123", "321") == True, "123 and 321 should be anagrams"
    print("✅ Assertion Test 3 (Numbers and punctuation): PASSED")
    
    print("✅ All assertion tests passed!\n")


# Example usage
if __name__ == "__main__":
    # Run all test suites
    test_is_anagram_general()
    test_is_anagram_unit()
    test_is_anagram_assertions()
    
    print("=" * 50)
    print("INTERACTIVE ANAGRAM CHECKER")
    print("=" * 50)
    
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    
    result = is_anagram(word1, word2)
    
    if result:
        print(f"✅ '{word1}' and '{word2}' are Anagrams!")
    else:
        print(f"❌ '{word1}' and '{word2}' are NOT Anagrams!")
