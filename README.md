# Backstory:
You're an intern at a bustling publishing company called "StorySphere Inc." As part of your internship, you're asked to help in preparing metadata for a series of new eBooks the company plans to release.

You've been given a text file that contains the titles of all the books that will be published this year. The company has a specific standard for metadata: the titles should be free of numbers and be capitalized.

# Given Data:

A text file named book_titles.txt is found in the uncleaned in the root dir

# Task:

1) Read the file book_titles.txt.
Using list comprehension, 
2) extract and clean the titles:
- Removing any numbers.
- Capitalizing the first letter of each word in the titles.
3) Write the cleaned titles back to a new file named cleaned_book_titles.txt in the cleaned folder.

# Bonus Challenge: **senior**
Find out which words are most commonly used in the book titles and list the top three.

# Hint:
You might want to use the split() function on strings and the Counter class from the collections module to help with the bonus challenge.

# What this exercise will teach you:
This exercise introduces you to file I/O operations in Python, string manipulation, and a bit of data analysis, all while leveraging the power of list comprehensions. It also introduces them to the useful Counter class from the collections module.


# TestCase

**----cleaned_book_title.txt Output ----**

The Silent Nights
Dreaming In 
Sky Without Stars
Python In 
Memories From 
Adventures In  Cities
Future Of 
A Day In  Hours
Evolution Of G To G
Decades To Millennia


**----Terminal Output -----**
Top 3 most common words and their counts:
In: 4
Of: 2
G: 2




