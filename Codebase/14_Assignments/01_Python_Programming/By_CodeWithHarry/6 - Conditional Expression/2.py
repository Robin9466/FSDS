"""
WAP to find out whether a student is pass or fail,if it requires total 40% and at least 33% in each of the subject to pass. Assume 3 subjects and take marks as an input from the user.
"""
import math
student_marks = []
i = 0
while i < 3:	
	subject_mark = int(input("Enter subject marks: "))
	student_marks.append(subject_mark)
	i +=1

obtained_marks = 0
i = 0
while i < 3:
	obtained_marks += student_marks[i]
	i +=1

print(f"You have scored {obtained_marks} out of 300")
individual_pass = all(mark >= 33 for mark in student_marks)
p = (obtained_marks/300)*100
if p >= 40:
	print("Congrats!, You have passed the exam.")
else:
	print("OOPs not things gone well, Do not worry, Champ")
