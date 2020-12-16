# Coursera - "Crash course on Python" Final assignment

## 1. Overview

The goal of this assignment was to create a Python script that generates a word cloud, using a text file submitted 
by the user, as input.

A sample text file, Alice_in_Wonderland_excerpt.txt , is included in the repository.

The project was initially completed in Jupyter Notebook and the guiding comments were retained in the code.

## 2. Implementation
Starting from the requirements, I created the following implementation plan:

* Create a file read function.
* Go through text and remove punctuation.
* Split text into a list of words.
* Remove common words.
* Remove words that contain numbers.
* Remove standalone numbers.
* Iterate through the list and create a dictionary, but ignore word case when inputting keys.
* Use the word cloud function, passing the dictionary as input, to display word cloud.
