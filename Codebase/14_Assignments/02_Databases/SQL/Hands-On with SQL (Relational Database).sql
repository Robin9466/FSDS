# Create a Database
CREATE DATABASE School;
USE School;

#  Create a Table
CREATE TABLE Students (
	StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Grade CHAR(1)
);

# Insert Data
INSERT INTO Students (StudentID, Name, Age, Grade) VALUES 
(1, 'Alice', 14, 'A'),
(2, 'Bob', 15, 'B'),
(3, 'Charlie', 14, 'A');

# Query Data
/* Fetch data using SELECT queries:
1. Get all students:
*/
SELECT * FROM Students;

# Find students with Grade 'A':
SELECT Name, Grade FROM Students WHERE Grade = 'A';

# UPDATE Data
# Modify a student's grade.
UPDATE Students SET Grade = 'B' WHERE StudentID = 1;

# Delete Data
# Remove a student from the database
DELETE FROM Students WHERE StudentID = 2;

# Create Relationships
/*
Add another table for Courses and link it to Students using a Foreign Key.
*/
CREATE TABLE Courses (
	CourseID INT PRIMARY KEY, 
    CourseName VARCHAR(50),
    StudentID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

# Insert data and retrieve information using JOIN:
INSERT INTO Courses (CourseID, CourseName, StudentID) VALUES
(101, 'Math', 1), (102, 'Science', 3);


SELECT Students.Name, Courses.CourseName
FROM Students
JOIN Courses ON Students.StudentID = Courses.StudentID;