#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:40:35 2021

@author: Siri Gjersøe
"""
# ""
#()


# The basics of creating new files and write something in them using:
# 'with open("filename.txt", "w+")'. Ispired by Code Academy courses in Python3.
#
# Options:  w for write, '+' to create a file that does not exist
#             'r' open for reading (default)
#             'x' open for exclusive creation, failing if the file already exists#
#             'a' open for writing, appending to the end of the file if it exists
#
# The 'with' function ensures the files closes

# 1. Open a file, indicate path if the file is somewhere else than in the script folder,
# specify the encoding if necessary. Save it as as the temporary file object 'file'
with open("TestFile.txt", "w+", encoding='utf8') as file:
# write something in the file:
    file.write("this is not a sentence")

# 2. Read what you wrote in the file
with open("TestFile.txt") as file:
    x = file.read()
    print(x)

# 3. Append material: The option 'a' gives you the option to append more sentences without
# overwriting the excisitng ones. Get line breaks with '\n'.
with open("TestFile.txt", "a") as file:
    file.write("\nThis is a another sentence\nThis is the third sentence\nThis is a fairly long sentence")

# 4. The 'read.line' method
# 'read.line' reads only one line from the file
# 'readline' appends a newline ("\n") at the end of the line.
# the argument specifies the number of characers retured. Default is
with open('TestFile.txt') as txt_file:
    line = txt_file.readline(4)
    print(line)

#  Use a 'for loop' to iterate over the temporary file object called 'txt_file' that points to the file TestFile.txt.
# 'read.line' iterates over each line in the document and prints the entire file out.
with open('TestFile.txt') as txt_file:
    for line in txt_file.readline():
        print(line)

# Use a for loop to read the file line-by-line
with open('TestFile.txt') as txt_file:
    for line in txt_file:
        print(line)

# The readlines() function reads until the End of the file using the readline() function
# internally and returns a list with all the lines read from the file.

# read a specific sentence in a file
# size argument for number of words
with open('TestFile.txt',"r") as txt_file:
    first_line = txt_file.readlines(50)
    print(first_line)

# Print the sentences which are longer than x number of characters
with open('TestFile.txt') as txt_file:
    for line in txt_file:
        if len(line) > 26:
            print(line)
