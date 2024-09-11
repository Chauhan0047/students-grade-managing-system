student_grades = { }

# Function to add a student's grades

def add_students(student_name, grade):
    student_grades[student_name] = grade
    print(f"student {student_name}'s and grade has been added.")

# Function to update a student's grade

def update_students(student_name, grade):
    if student_name in student_grades:
        student_grades[student_name] = grade
        print(f"student {student_name}'s grade has been updated.")
    else:
        print(f"student {student_name} does not found.")

# Function to delete a student

def delete_students(student_name):
    if student_name in student_grades:
        del student_grades[student_name]
        print(f"student {student_name}'s record has been deleted.")
    else:
        print(f"student {student_name} does not found.")

# view all students record

def display_students():
    if student_grades:
        for student_name, grade in student_grades.items():
            print(f"Student Name: {student_name}, Grade: {grade}")

        else:
            print("No students found.")

# Test the functions

def main():
    while True:
        print("Student grade managing system...")
        print("1. Add students")
        print("2. Update students")
        print("3. Delete students")
        print("4. View students")
        print("5. Exit")

        choice = input("Enter your choice(in numbers): ")
        

        if choice == '1':
            student_name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))
            add_students(student_name, grade)

        elif choice == '2':
            student_name = input("Enter student name: ")
            grade = float(input("Enter new student grade: "))
            update_students(student_name, grade)

        elif choice == '3':
            student_name = input("Enter student name: ")
            delete_students(student_name)

        elif choice == '4':
            display_students()

        elif choice == '5':

            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

    
