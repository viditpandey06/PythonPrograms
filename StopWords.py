import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stop_word_separation(text):
    # Download the stopwords corpus if not already downloaded
    nltk.download('stopwords')

    # Download the punkt tokenizer if not already downloaded
    nltk.download('punkt')

    # Tokenize the input text into words
    words = word_tokenize(text)

    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))

    # Remove the stopwords from the tokenized words
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    # Return the filtered words as a string
    return ' '.join(filtered_words)

# Example usage
input_text = "This is an example sentence with some stop words."
output_text = stop_word_separation(input_text)
print(output_text)