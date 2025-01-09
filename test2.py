from collections import Counter
import re

def count_word_frequencies(text):
    words = re.findall(r'\b\w+\b', text.lower())
    
    word_counts = Counter(words)
    
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    print("Word Frequencies:")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

text = "Hello world! This is a test. Hello, this test is only a test."

count_word_frequencies(text)
