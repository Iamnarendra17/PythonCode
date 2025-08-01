'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
    file1 = open('sample.txt','r+')
    line1 = file1.readlines()
    print("Line 1: ",line1[0])
    print("Line 2: ",line1[1])
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")