Student Grade Management System
Overview
This Python script manages student grades using a dictionary. It allows you to add, update, delete, and view student records. The script includes a simple command-line interface for interaction.

Features
Add Students: Add new student records with their grades.
Update Students: Update the grades of existing students.
Delete Students: Remove student records.
View Students: Display all student records.

Requirements
Python 3.x

Installation
Clone the repository:
Copy code = git clone https://github.com/yourusername/student-grade-management.git


Navigate to the project directory:
Copy code = cd student-grade-management


Usage
Run the script:
Copy code = python student_grade_management.py


Follow the on-screen menu to interact with the system:

Add Students: Choose option 1 to add a student's name and grade.
Update Students: Choose option 2 to update the grade of an existing student.
Delete Students: Choose option 3 to delete a student's record.
View Students: Choose option 4 to view all student records.
Exit: Choose option 5 to exit the application.


Example Usage
Here's how you might use the script:
Copy code:{
Student grade managing system...
1. Add students
2. Update students
3. Delete students
4. View students
5. Exit
Enter your choice(in numbers): 1
Enter student name: John Doe
Enter student grade: 85
student John Doe's and grade has been added.

Enter your choice(in numbers): 4
Student Name: John Doe, Grade: 85

Enter your choice(in numbers): 5
Exiting...
}

Code Details
add_students(student_name, grade): Adds a new student's record.
update_students(student_name, grade): Updates the grade of an existing student.
delete_students(student_name): Deletes a student's record.
display_students(): Displays all student records.

Contributing
Feel free to open issues or submit pull requests if you have any suggestions or improvements.
