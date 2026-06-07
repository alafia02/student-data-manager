students = []

def add_student():
    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")
    marks = input("Marks: ")

    student = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }
    students.append(student)
    print("Student added!")

def view_students():
    for student in students:
        print(student)

def search_student():
    name = input("Enter student name to search: ")
    for student in students:
        if student["Name"] == name:
            print(student)
            return

    print("Student not found!")

def delete_student():
    name = input("Enter name to delete: ")

    for student in students:
        if student["Name"] == name:
            students.remove(student)
            print("Student deleted!")
            return

    print("Student not found!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid ")