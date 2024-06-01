Overview
  The Employee Management System is a simple application designed to manage employee records. This project utilizes SQLite for database management and Docker for containerization. The application is primarily written in Python.

Features
  Add new employees
  Update existing employee records
  Delete employee records
  View all employees
  Project Structure
main.py:  
  The main script to run the application. This script handles user interactions and calls functions from database.py.
database.py: 
  Contains all the database-related functions, such as connecting to the database, executing queries, and managing employee data.
Dockerfile: 
  Used to create a Docker image for the application, ensuring consistent and portable deployment.
