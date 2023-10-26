import re
from collections import Counter

# Step 1: Read the file
with open('./uncleaned/book_titles.txt', 'r') as f:
    titles = f.readlines()
    
# Step 2: Use list comprehension to extract and clean titles
cleaned_titles = [re.sub(r"[0-9]", "", title.split(".")[1].strip()).title() for title in titles]

print(cleaned_titles)
# Step 3: Write the cleaned titles back to a new file
with open('./cleaned/cleaned_book_titles.txt', 'w') as f:
    for title in cleaned_titles:
        f.write(title + '\n')

# Bonus Challenge: Find out the most common words in the titles and list the top three
words = [word for title in cleaned_titles for word in title.split()]
word_count = Counter(words)
common_words = word_count.most_common(3)

print("Top 3 most common words and their counts:")
for word, count in common_words:
    print(f"{word}: {count}")
