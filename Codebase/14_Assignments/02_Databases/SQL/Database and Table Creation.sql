/*
1. Database and Table Creation
Objective: Learn to create and structure a database for data storage.
Assignment:
Create a database named SchoolDB.
Create a students table with columns: id (INT, PRIMARY KEY), name (VARCHAR), age (INT), and grade (VARCHAR).
Deliverable: SQL script for creating the database and table.
*/

-- Create the SchoolDB database if it doesn't exist
CREATE DATABASE IF NOT EXISTS SchoolDB;

-- Select the SchoolDB database to use
USE SchoolDB;

-- Create the students table if it doesn't exist
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,         -- Student ID as the primary key
    name VARCHAR(50),           -- Student name (max 50 characters)
    age INT,                    -- Student age
    grade VARCHAR(5)            -- Student grade (e.g., "A", "B+", etc.)
);

