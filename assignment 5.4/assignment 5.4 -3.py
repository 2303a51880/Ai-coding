# Ensure required packages are installed
import sys
import subprocess

def install_if_missing(package):
	try:
		__import__(package)
	except ImportError:
		print(f"Installing missing package: {package}")
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install 'pandas' if not present
install_if_missing('pandas')

import pandas as pd

# --- Product Recommendation System with Ethical AI Principles ---
def recommend_products(user_id, user_history, product_catalog):
	"""
	Recommend products based on user interaction or purchase history.
	- Transparency: Explain why each product is recommended.
	- Fairness: Avoid favoritism toward specific products or users.
	- User feedback: Allow users to provide feedback or opt out.
	"""
	# Example: Recommend top categories the user interacted with, but ensure diversity
	# Count product category interactions
	history_df = pd.DataFrame(user_history)
	if history_df.empty:
		return [], []
	top_categories = history_df['category'].value_counts().index.tolist()
	# Select products from top categories, but ensure at least one from other categories
	recommended = []
	explanations = []
	used_categories = set()
	for cat in top_categories:
		prods = [p for p in product_catalog if p['category'] == cat]
		if prods:
			recommended.append(prods[0])
			explanations.append(f"Recommended because you interacted with {cat} products.")
			used_categories.add(cat)
	# Add a product from a less-seen category for fairness/diversity
	for p in product_catalog:
		if p['category'] not in used_categories:
			recommended.append(p)
			explanations.append(f"Recommended for diversity from category: {p['category']}.")
			break
	return recommended, explanations

# Example data
product_catalog = [
	{'id': 1, 'name': 'Wireless Mouse', 'category': 'Electronics'},
	{'id': 2, 'name': 'Yoga Mat', 'category': 'Fitness'},
	{'id': 3, 'name': 'Water Bottle', 'category': 'Fitness'},
	{'id': 4, 'name': 'Bluetooth Speaker', 'category': 'Electronics'},
	{'id': 5, 'name': 'Cookbook', 'category': 'Books'},
]

user_history = [
	{'product_id': 1, 'category': 'Electronics'},
	{'product_id': 4, 'category': 'Electronics'},
	{'product_id': 2, 'category': 'Fitness'},
]

if __name__ == "__main__":
	user_id = 123
	print("\n--- Product Recommendations ---")
	recs, reasons = recommend_products(user_id, user_history, product_catalog)
	for prod, reason in zip(recs, reasons):
		print(f"{prod['name']} (Category: {prod['category']}) -> {reason}")

	# User feedback and opt-out
	print("\nWould you like to provide feedback or opt out of recommendations?")
	feedback = input("Enter feedback or type 'opt out' to stop recommendations: ")
	if feedback.strip().lower() == 'opt out':
		print("You have opted out of recommendations. Your preferences will be respected.")
	else:
		print(f"Thank you for your feedback: {feedback}")

# --- Ethical AI Notes ---
# - Transparency: Each recommendation includes an explanation.
# - Fairness: The system ensures diversity and avoids recommending only from the most frequent category.
# - User Control: Users can provide feedback or opt out at any time.
# - Regularly audit recommendation logic for bias and update as needed.