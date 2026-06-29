students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo Students Found!\n")
        return

    print("\n------ Student Records ------")
    for s in students:
        print(f"Roll No : {s['Roll']}")
        print(f"Name    : {s['Name']}")
        print(f"Age     : {s['Age']}")
        print(f"Course  : {s['Course']}")
        print("-----------------------------")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for s in students:
        if s["Roll"] == roll:
            print("\nStudent Found")
            print(f"Roll No : {s['Roll']}")
            print(f"Name    : {s['Name']}")
            print(f"Age     : {s['Age']}")
            print(f"Course  : {s['Course']}")
            return

    print("\nStudent Not Found!\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("\nStudent Deleted Successfully!\n")
            return

    print("\nStudent Not Found!\n")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")
