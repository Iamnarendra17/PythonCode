'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''

n = int(input("Enter the number: "))
if n%2==1:
    print(n," is the odd number")
else:
    print(n," is the even number")