from student import Student
      
list = []
while True: 
    print('''
        Choose your options:
        0. Exit
        1. List of students
        2. Add student to list
        3. Remove student from list
        4. Edit student in list      
    ''')
    choice = input("choose your options > ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 0:
            break
        elif choice == 1:
            if len(list) == 0:
                print("No students in list")
            else:
                for student in list:
                    student.show()
        elif choice == 2:
            student_id = input("ID > ")
            if student_id.isdigit():
                student_name = input("Name > ")
                list.append(Student(student_id, student_name))
            else:
                print("Type Error! ID is a number!") 
        elif choice == 3:
            student_id = input("ID > ")
            if student_id.isdigit():
                for student in list:
                    if student.get_id() == student_id:
                        list.remove(student)
            else: 
                print("Type Error! ID is a number!")
        elif choice == 4:
            student_id = input("ID > ")
            if student_id.isdigit():
                for student in list:
                    if student.get_id() == student_id:
                        nameToEdit = input("Change student name > ")
                        student.set_name(nameToEdit)
            else: 
                print("Type Error! ID is a number!") 
                 
    else:
        print("Choose again! Need a number!")
    