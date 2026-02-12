import random
import string

def generate_password(length):
    """Generate a random password with specified length.
    
    Creates a password containing uppercase letters, lowercase letters,
    digits, and special characters randomly selected from the available
    character set.
    
    Args:
        length (int): The desired length of the generated password.
    
    Returns:
        str: A randomly generated password of the specified length.
    
    Example:
        >>> password = generate_password(12)
        >>> len(password)
        12
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def is_strong_password(password):
    """Check if a password meets strong security criteria.
    
    A password is considered strong if it contains at least 8 characters
    and includes at least one uppercase letter, one lowercase letter,
    one digit, and one special character.
    
    Args:
        password (str): The password string to validate.
    
    Returns:
        bool: True if the password is strong, False otherwise.
    
    Example:
        >>> is_strong_password('Weak')
        False
        >>> is_strong_password('StrongP@ss123')
        True
    """
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return len(password) >= 8 and has_upper and has_lower and has_digit and has_special

def hash_password(password):
    """Generate a hash value for a password using polynomial rolling hash.
    
    Applies a polynomial rolling hash algorithm to convert a password
    into a numeric hash value. Uses a base of 31 and modulo 1000000007
    to keep the result manageable.
    
    Args:
        password (str): The password string to hash.
    
    Returns:
        int: A numeric hash value of the password.
    
    Example:
        >>> hash_val = hash_password('test123')
        >>> isinstance(hash_val, int)
        True
    """
    value = 0
    for char in password:
        value = (value * 31 + ord(char)) % 1000000007
    return value

def main():
    """Main function to demonstrate password generation and validation.
    
    Generates a random password, checks its strength, and computes its hash.
    Outputs the generated password, its strength status, and hash value.
    
    Returns:
        None
    
    Example:
        >>> main()
        Password: <generated_password>
        Strong: True
        Hash: <hash_value>
    """
    pwd = generate_password(12)
    strength = is_strong_password(pwd)
    hashed = hash_password(pwd)
    print("Password:", pwd)
    print("Strong:", strength)
    print("Hash:", hashed)

if __name__ == "__main__":
    main()
