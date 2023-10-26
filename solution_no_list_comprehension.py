import re
from collections import Counter

cleaned_dir_path:str = './cleaned/'
uncleaned_dir_path:str ='./uncleaned/'
uncleaned_file_name:str = 'book_titles.txt'


# Step 1: Read the file
def read_file(directory,file):
    with open(directory+file, 'r') as f:
        titles = f.readlines()#returns a list 
        return titles

# Step 2: Extract and clean titles 
def clean_titles(directory, file):
    cleaned_titles = []
    
    for title in read_file(directory,file): #convert string into list 
        title_part = title.split(".")[1].strip()
        cleaned_title = re.sub(r"[0-9]", "", title_part).title() # r'' raw string removes \n also
        cleaned_titles.append(cleaned_title)
    return cleaned_titles



# Step 3: Write the cleaned titles back to a new file
def clean_file(cleaned_folder, uncleaned_dir,uncleanFile, file='cleanedFile.txt'):
    with open(f'{cleaned_folder}{file}', 'w') as f:
        for title in clean_titles(uncleaned_dir,uncleanFile):
            f.write(title + '\n') 
            print(title)
                     
clean_file(cleaned_dir_path,uncleaned_dir_path,uncleaned_file_name)

# # Bonus Challenge: Find out the most common words in the titles and list the top three
def common_words(cleaned_titles=clean_titles(uncleaned_dir_path,uncleaned_file_name)):
    words = []
    for title in cleaned_titles:
        for word in title.split():
            words.append(word)

    word_count = Counter(words)
    common_words = word_count.most_common(3)

    print("Top 3 most common words and their counts:")
    for word, count in common_words:
        print(f"{word}: {count}")

# calling functions
common_words()
print('------')
clean_file(cleaned_dir_path,uncleaned_dir_path,uncleaned_file_name)
