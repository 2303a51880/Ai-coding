# --- Secure Logging Setup for a Python Web Application ---
import logging

# Ethical Logging Practices:
# - Never log sensitive or personally identifiable information (PII) such as passwords, emails, tokens, or credit card numbers.
# - Use data minimization: only log what is necessary for debugging, monitoring, or auditing.
# - Regularly review log content and access permissions.
# - Mask or redact any data that could be sensitive if logging user input or errors.

# Configure logging
logging.basicConfig(
	level=logging.INFO,  # Use INFO or WARNING in production
	format='%(asctime)s %(levelname)s %(message)s',
	handlers=[
		logging.FileHandler('app.log'),
		logging.StreamHandler()
	]
)

# Example of safe logging (do NOT log sensitive data)
def login_user(username):
	# DO NOT log passwords, emails, or tokens!
	logging.info(f"User login attempt: username={username}")
	# ...existing authentication logic...
	# If authentication fails, log only non-sensitive info
	# logging.warning(f"Failed login for username={username}")

# Example usage
if __name__ == "__main__":
	login_user("alice")
	# logging.info("User provided password: hunter2")  # <-- BAD PRACTICE, never log passwords!

# --- Data Minimization Principles ---
# - Log only what is necessary for the application's operation and security.
# - Avoid logging full request/response bodies, especially if they may contain PII.
# - Use log rotation and retention policies to minimize data exposure.
