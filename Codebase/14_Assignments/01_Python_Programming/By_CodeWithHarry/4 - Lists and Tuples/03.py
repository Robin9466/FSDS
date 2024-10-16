"""
WAP to accept marks of 6 students, and display them in the sorted manner.
"""
student_marks = []
i = 0
while i < 6:
	student_mark = float(input("Enter marks of 6 student: "))
	i+=1
	student_marks.append(student_mark)
student_marks.sort()
print("sorted marks: ", student_marks)