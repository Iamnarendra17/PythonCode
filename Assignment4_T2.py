'''
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
try:
    userinput = input("Enter text to write to the file: ")
    file1 = open('output.txt','w')
    file1.writelines(userinput)
    file1.close()
    file1 = open('output.txt','r+')
    fileread = file1.read()
    file1.close()
    if userinput == fileread:
        print("Data successfully written to output.txt")
    else:
        print("Data is not written")

    userinput = input("Enter additional text to append: ")
    file1 = open('output.txt','a')
    file1.writelines(userinput)
    file1.close()
    file1 = open('output.txt','r')
    appendedString = file1.readlines()
    #apps = appendedString[1]
    print("Data successfully appended.")
    file1.close()
    # if userinput == appendedString[1]:
    #     print("Data successfully appended.")
    # else:
    #     print("Data is not successfully appended")
    print("Final content of output.txt")
    print(appendedString)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

