import re
from collections import Counter

# Step 1: Read the file
with open('./uncleaned/book_titles.txt', 'r') as f:
    titles = f.readlines()

# Step 2: Extract and clean titles without list comprehension
cleaned_titles = []
for title in titles:
    title_part = title.split(".")[1].strip()
    cleaned_title = re.sub(r"[0-9]", "", title_part).title()
    cleaned_titles.append(cleaned_title)

# Step 3: Write the cleaned titles back to a new file
with open('./cleaned/cleaned_book_titles.txt', 'w') as f:
    for title in cleaned_titles:
        f.write(title + '\n')

# Bonus Challenge: Find out the most common words in the titles and list the top three
words = []
for title in cleaned_titles:
    for word in title.split():
        words.append(word)

word_count = Counter(words)
common_words = word_count.most_common(3)

print("Top 3 most common words and their counts:")
for word, count in common_words:
    print(f"{word}: {count}")
