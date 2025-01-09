# Python Test Project

## Overview
This repository contains solutions for two Python tests:

1. **Python Test 1**: A function to validate strings based on specific regular expression criteria.
2. **Python Test 2**: A program to count word frequencies in a text and display them in descending order of frequency.

---

## Python Test 1: String Validation

### Problem Description
Create a function that checks if a passed-in string is valid for a given regular expression. The string must meet the following conditions:

- **Length**: At least 6 characters long.
- **Numbers**: At least 2 characters must be numbers, but no more than 3.
- **Spacing**: At least 1 non-numerical character must appear between each number.

### Example Usage
```python
import re

def is_valid_string(s):
    # Check if the string is at least 6 characters long
    if len(s) < 6:
        return False
    
    # Define the regex to match the required pattern
    pattern = r"^(?=(.*\d.*\d)(?!.*\d.*\d.*\d))(?=.*\D.*\d)(?!.*\d\d).+$"
    
    # Use regex to check the validity of the string
    return bool(re.match(pattern, s))

# Example Test Cases
print(is_valid_string("a1b2c3"))  # True
print(is_valid_string("123abc"))  # False
print(is_valid_string("abc123"))  # False
print(is_valid_string("a1b2c"))   # False
```

---

## Python Test 2: Word Frequency Counter

### Problem Description
Create a Python program that:
- Reads a string of text.
- Counts the frequency of each word.
- Displays the words in descending order of frequency.

### Example Input
```plaintext
text = "Hello world! This is a test. Hello, this test is only a test."
```

### Example Output
```plaintext
Word Frequencies:
test: 3
hello: 2
this: 2
is: 2
a: 2
world: 1
only: 1
```

### Example Code
```python
from collections import Counter
import re

def count_word_frequencies(text):
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Sort by frequency (descending), then alphabetically
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Display the word frequencies
    print("Word Frequencies:")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

# Example Input
text = "Hello world! This is a test. Hello, this test is only a test."

# Run the function
count_word_frequencies(text)
```

---

## How to Run the Code

1. **Clone the Repository**:
   ```bash
   https://github.com/Bien-venu/python-tests.git
   cd python-tests
   ```

2. **Run Python Test 1**:
   ```bash
   python test1.py
   ```

3. **Run Python Test 2**:
   ```bash
   python test2.py
   ```

---
