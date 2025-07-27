'''
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

'''
n = int(input("Enter the number to calculate factorial: "))
# f=1
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)

result= fact(n)
print("Factorial of given number is: ", result)