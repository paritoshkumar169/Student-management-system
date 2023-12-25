class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


USERNAME = "admin"
PASSWORD = "admin123"

def authenticate():
    print("Enter your credentials to access the Student Management System.")
    username_input = input("Username: ")
    password_input = input("Password: ")

    return username_input == USERNAME and password_input == PASSWORD

def add_student(students, name, age, grade):
    student = Student(name, age, grade)
    students.append(student)
    print(f"Student {name} added successfully.")

def view_students(students):
    print("\nStudent List:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

def search_student(students, search_query):
    for student in students:
        if search_query.lower() in student.name.lower():
            print(f"\nStudent found: Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
            return
    print("\nStudent not found.")

def update_student(students, search_query, new_age, new_grade):
    for student in students:
        if search_query.lower() in student.name.lower():
            student.age = new_age
            student.grade = new_grade
            print(f"\nStudent {student.name}'s details updated successfully.")
            return
    print("\nStudent not found.")

def calculate_average_grade(students):
    if not students:
        print("\nNo students in the system.")
        return
    total_grades = sum(student.grade for student in students)
    average_grade = total_grades / len(students)
    print(f"\nAverage Grade: {average_grade}")

def display_student_count(students):
    print(f"\nTotal Students: {len(students)}")

def main():
    # Check credentials
    if not authenticate():
        print("Authentication failed. Exiting program.")
        return

    students = []

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student Details")
        print("5. Calculate Average Grade")
        print("6. Display Student Count")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = float(input("Enter student grade: "))
            add_student(students, name, age, grade)

        elif choice == '2':
            view_students(students)

        elif choice == '3':
            search_query = input("Enter student name to search: ")
            search_student(students, search_query)

        elif choice == '4':
            search_query = input("Enter student name to update: ")
            new_age = int(input("Enter new age: "))
            new_grade = float(input("Enter new grade: "))
            update_student(students, search_query, new_age, new_grade)

        elif choice == '5':
            calculate_average_grade(students)

        elif choice == '6':
            display_student_count(students)

        elif choice == '7':
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
