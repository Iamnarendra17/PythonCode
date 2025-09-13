'''
Task 1: Create a Dictionary of Student Marks
'''

student_details = {
    "Alice":90,
    "Joy":85,
    "Kartik":75
}
sname = input("Enter the Student's name: ")
if sname in student_details:
    print(f"{sname}'s Marks: {student_details[sname]}")
else:
    print("Student not found")