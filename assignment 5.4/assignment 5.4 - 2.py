# Ensure required packages are installed
import sys
import subprocess

def install_if_missing(package):
	try:
		__import__(package)
	except ImportError:
		print(f"Installing missing package: {package}")
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install 'textblob' if not present
install_if_missing('textblob')


# Sentiment analysis function with bias awareness and mitigation strategies
from textblob import TextBlob

def analyze_sentiment(text):
	"""
	Analyzes the sentiment of the input text.
	Returns polarity (-1 to 1) and subjectivity (0 to 1).

	Potential sources of bias in training data:
	- Imbalanced datasets (e.g., more positive than negative samples)
	- Presence of offensive, discriminatory, or culturally specific terms
	- Overrepresentation or underrepresentation of certain topics or groups

	Strategies to mitigate bias:
	- Balance the dataset across sentiment classes and demographic groups
	- Remove or flag offensive/discriminatory terms during preprocessing
	- Use diverse and representative data sources
	- Document known limitations and test for bias regularly
	- Involve domain experts in dataset curation
	"""
	# Example: Using TextBlob for simple sentiment analysis
	blob = TextBlob(text)
	polarity = blob.sentiment.polarity
	subjectivity = blob.sentiment.subjectivity
	return polarity, subjectivity

# Example usage
if __name__ == "__main__":
	user_text = input("Enter text for sentiment analysis: ")
	polarity, subjectivity = analyze_sentiment(user_text)
	print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")

# Note: For production, train your own model on a carefully curated dataset and regularly audit for bias.
# The above function uses TextBlob, which is trained on general-purpose data and may inherit its biases.
