studentDB = {}

def addStud():
    name = input("Enter Your Name: ")
    age = input("Enter Your Age: ")
    grade = input("Enter Your Grade: ")
    
    studInfo = {'Name': name, 'Age': age, 'Grade': grade}
    studentDB[name] = studInfo
    print(f"Student {name} added successfully")

def viewStud():
    name = input("Enter student name: ")
    if name in studentDB:
        studInfo = studentDB[name]
        print("\nStudent Detail")
        print(f"Name: {studInfo['Name']}")
        print(f"Age: {studInfo['Age']}")
        print(f"Grade: {studInfo['Grade']}")
    else:
        print("Not found")

def allStud():
    print("\nList of All Students:")
    for name, studInfo in studentDB.items():
        print(f"Name: {studInfo['Name']}, Age: {studInfo['Age']}, Grade: {studInfo['Grade']}")

def update():
    name = input("Enter Name of student to be updated: ")
    if name in studentDB:
        studInfo = studentDB[name]
        new_age = input(f"Enter the New age: ")
        new_grade = input("Enter the New grade: ")
        studInfo['Age'] = new_age
        studInfo['Grade'] = new_grade
        print(f"Student {name} has been successfully updated")
    else:
        print(f"Student {name} not found!")

def delete():
    name = input("Enter name of the student to be deleted: ")
    if name in studentDB:
        del studentDB[name]
        print("Student data deleted successfully!!!")
    else:
        print(f"Student {name} not found!!!")

while True:
    print("\nSimple Student Database Management System")
    print("1. ADD STUDENT")
    print("2. VIEW STUDENT")
    print("3. LIST OF ALL STUDENTS")
    print("4. UPDATE STUDENT INFORMATION")
    print("5. DELETE STUDENT DATA")
    print("6. EXIT")
    
    choice = int(input("\nENTER YOUR CHOICE: "))
    if choice == 1:
        addStud()
    elif choice == 2:
        viewStud()
    elif choice == 3:
        allStud()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    elif choice == 6:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid Input")
