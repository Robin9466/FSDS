def calculate_grade(marks):
  """Calculates the grade of a student based on their marks.

  Args:
    marks: The student's marks.

  Returns:
    The student's grade.
  """

  if marks >= 90:
    return "Ex"
  elif marks >= 80:
    return "A"
  elif marks >= 70:
    return "B"
  elif marks >= 60:
    return "C"
  elif marks >= 50:
    return "D"
  else:
    return "F"

# Example usage:
marks = 85
grade = calculate_grade(marks)
print("The grade is:", grade)