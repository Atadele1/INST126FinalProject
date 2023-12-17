import os
import re
import matplotlib as plt

# Step 1: Read Multiple HTML Files
folder_path = r'\Users\goodr\Downloads\INST126FinalProject\HTMLFiles'
html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]

word_count = {}  

#Searching for specific words that are case sensitive Won, Nominated, Runner Up
target_word = 'Won'  

for file_name in html_files:
    with open(os.path.join(folder_path, file_name), 'r') as file:
        html_content = file.read

    
    count = len(target_word)
    word_count[file_name] = count

# Matplotlib to Show Files with Most Case Sensitive Words
file_names = list(word_count.keys())
counts = list(word_count.values())

plt.figure(figsize=(10, 6))
plt.bar(file_names, counts)
plt.xlabel('HTML Files')
plt.ylabel(f'Occurrences of "{target_word}" (Case Sensitive)')
plt.title(f'Occurrences of "{target_word}" in HTML Files')

plt.xticks(rotation=45, ha='right') 
plt.tight_layout()
plt.show()
