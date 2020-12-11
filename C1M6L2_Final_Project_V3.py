# Final Project - Word Cloud

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs to process the
# text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies,
# and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.
# The `wordcloud` module will then generate the image from your dictionary.
# For the input text of your script, you will need to provide a file that contains text only.

# The following libraries need to be installed for the script to function:
# get_ipython().system('pip install wordcloud')
# get_ipython().system('pip install fileupload')
# get_ipython().system('pip install ipywidgets')

import wordcloud
from matplotlib import pyplot as plt
from collections import defaultdict


def read_file():
    '''read_file asks the user for a file name and returns its contents as a string'''
    file_name = input("Please enter your file name, with the extension: ")
    with open(file_name, 'r', encoding='utf-8') as reader:
        contents = reader.read()
    return contents


file_contents = read_file()


# Write a function that iterates through the words in *file_contents*, removes punctuation,
# and counts the frequency of each word.  Oh, and be sure to make it ignore word case, words that do not contain all
# alphabets and boring words like "and" or "the".  Then use it in the `generate_from_frequencies` function to
# generate your very own word cloud


def calculate_frequencies(file_text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers",
                           "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am",
                           "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did",
                           "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both",
                           "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",
                           "chapter", "in", "for", "not", "there", "about", "so", "up", "out", "on", "down", "ebook"]

    # Remove punctuation
    new_string = ''.join(ch for ch in file_text if ch not in set(punctuation))

    # Split new_string into a list of words
    word_list = new_string.split()

    # freq_dict is a dictionary that tracks word frequencies
    # this step also removes unwanted words and all numbers
    freq_dict = defaultdict(int)
    for word in word_list:
        if word.lower() not in uninteresting_words and word.isalpha():
            freq_dict[word.lower()] += 1

    # word cloud creation
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq_dict)
    return cloud.to_array()


# Display our word cloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
