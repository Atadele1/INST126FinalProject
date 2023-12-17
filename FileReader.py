import os
import re
import matplotlib.pyplot as plt

# Step 1: Read Multiple HTML Files
folder_path = 'C:\Users\goodr\Downloads\INST126FinalProject\HTMLFiles'
html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]

word_count = {}  # Dictionary to store count of specific words

# Step 2: Search for Specific Words (Case Sensitive)
target_word = 'your_target_word'  # Replace 'your_target_word' with the word you're looking for

for file_name in html_files:
    with open(os.path.join(folder_path, file_name), 'r') as file:
        html_content = file.read()

    # Search for the target word using regular expressions
    count = len(re.findall(r'\b' + re.escape(target_word) + r'\b', html_content))
    word_count[file_name] = count

# Step 3: Using Matplotlib to Show Files with Most Case Sensitive Words
file_names = list(word_count.keys())
counts = list(word_count.values())

plt.figure(figsize=(10, 6))
plt.bar(file_names, counts)
plt.xlabel('HTML Files')
plt.ylabel(f'Occurrences of "{target_word}" (Case Sensitive)')
plt.title(f'Occurrences of "{target_word}" in HTML Files')

plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
