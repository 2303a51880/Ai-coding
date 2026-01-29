# -------------------------------------------------------------
# Example: Simple Machine Learning Model with Responsible AI Notes
# -------------------------------------------------------------
# This script demonstrates a basic ML workflow using scikit-learn:
#  - Loads the Iris dataset
#  - Trains a logistic regression classifier
#  - Makes a prediction
#
# Responsible Use Guidelines:
# - Accuracy Limitations: This model is for demonstration only and may not generalize to other datasets or real-world scenarios.
# - Explainability: Logistic regression is interpretable, but always explain model decisions to users when possible.
# - Fairness: The Iris dataset is balanced, but real-world data may have bias. Always check for and mitigate bias in your data and model.
# - Appropriate Use: Do not use this model for high-stakes decisions (e.g., healthcare, hiring) without thorough validation and ethical review.
# - Restrictions: Never use ML models to discriminate or make decisions about protected groups without fairness analysis and legal review.
# -------------------------------------------------------------

# Ensure required packages are installed
import sys
import subprocess

def install_if_missing(package):
	try:
		__import__(package)
	except ImportError:
		print(f"Installing missing package: {package}")
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install scikit-learn if not present
install_if_missing('sklearn')

# Import libraries
# Ensure scikit-learn is installed before importing
import sys
import subprocess
def install_if_missing(package):
	try:
		__import__(package)
	except ImportError:
		print(f"Installing missing package: {package}")
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install_if_missing('sklearn')
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model accuracy on test set: {acc:.2f}")

# Make a prediction
sample = X_test[0].reshape(1, -1)
predicted_class = model.predict(sample)[0]
print(f"Predicted class for first test sample: {iris.target_names[predicted_class]}")

# --- Responsible AI Reminders ---
# - Always validate model performance on relevant, representative data.
# - Document and communicate model limitations to users and stakeholders.
# - Regularly audit for bias and update the model as needed.
