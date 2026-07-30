# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2026, Created Script
#   Erick Epley, 7/24/26, Began Coding Script
#   Erick Epley 7/28/26, Finished Script
# ------------------------------------------------------------------------------------------ #

# Import the json
import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = "" # Hold the choice made by the user.

# Attempt to read the file, provide error handing for exceptions
try:
    # When the program starts, read the file data into a list of lists (table)
    # Extract the data from the file
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

# FileNotFound Error exception
except FileNotFoundError as e:
    print(f"A file named: {FILE_NAME} must exist before running the script.")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')

# General Exception
except Exception as e:
    print("There was a non-specific error!")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')

# Finally check to see if the file has been closed
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        # Begin Try/Except to ensure Names have the correct characters
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The First Name Should Only Contain Letters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The Last Name Should Only Contain Letters.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}     # Format Data into a Dictionary
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        # Value Error exception
        except ValueError as e:
            print(e) # Print the custom message
            print("-- Technical Error Message --")
            print(e.__doc__)

        # General exception
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')

        continue # the loop

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        print("The Current Data is: ")
        for student in students:
            print(f"{student["FirstName"]},{student["LastName"]},{student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()

            # Print the data to screen to tell the user what was saved to the file
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]}" 
                      f" is enrolled in {student["CourseName"]}")

        # Type Error exception
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        #
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')

        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()

        continue # the loop

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
