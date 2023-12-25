class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        pass
    def add_student(students,name,age,grade):
        student = Student(students,name,age,grade)
        students.append(student)
        print("Student"+ name + "added successfully")

