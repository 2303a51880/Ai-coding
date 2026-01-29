# Basic User Data Collection Script
# This script collects name, age, and email address from the user.
# It also includes comments on best practices for protecting and anonymizing sensitive data.

# Import necessary libraries for hashing and encryption
import sys
import subprocess

def install_if_missing(package):
	try:
		__import__(package)
	except ImportError:
		print(f"Installing missing package: {package}")
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install 'cryptography' if not present
install_if_missing('cryptography')

import hashlib

# Import Fernet only after ensuring cryptography is installed
from cryptography.fernet import Fernet

# Prompt user for basic information
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email address: ")

# --- Data Protection and Anonymization Best Practices ---
# 1. Avoid storing sensitive data in plaintext. Use hashing or encryption.
# 2. Hash email addresses to anonymize them (irreversible, good for privacy-preserving analytics).
# 3. Encrypt data if you need to recover the original value later (e.g., for user login).
# 4. Never log or print sensitive data in plaintext.
# 5. Store encryption keys securely (not hardcoded in code).

# Example: Hash the email address (anonymization)
hashed_email = hashlib.sha256(email.encode()).hexdigest()
# Now, hashed_email can be stored instead of the plaintext email for privacy.

# Example: Encrypt the name and age (if you need to recover them later)
# In practice, store the key securely (e.g., environment variable, key vault)
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted_name = cipher_suite.encrypt(name.encode())
encrypted_age = cipher_suite.encrypt(age.encode())

# Example output (do not print sensitive data in production)
print("\n--- Data Collected (for demonstration only) ---")
print(f"Hashed Email: {hashed_email}")
print(f"Encrypted Name: {encrypted_name}")
print(f"Encrypted Age: {encrypted_age}")
# Note: In a real application, do not print or log sensitive data.

# --- Summary of Best Practices ---
# - Use strong cryptographic algorithms (e.g., SHA-256 for hashing, Fernet for encryption).
# - Never store or transmit sensitive data in plaintext.
# - Store encryption keys securely and separately from the data.
# - Regularly audit and update your security practices.
