from database import setup_database
import operations as op

def main():
    setup_database()

    while True:
        print("\n==== E-Learning System ====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. View Students")
        print("4. View Courses")
        print("5. Enroll Student in Course")
        print("6. View Enrollments")
        print("7. Dashboard")
        print("8. Update Student")
        print("9. Delete Student")
        print("10. Update Course")
        print("11. Delete Course")
        print("12. Update Progress")
        print("13. Exit")


        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            op.add_student(name, email)

        elif choice == "2":
            title = input("Enter course title: ")
            description = input("Enter course description: ")
            op.add_course(title, description)

        elif choice == "3":
            op.view_students()

        elif choice == "4":
            op.view_courses()

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            op.enroll_student(student_id, course_id)

        elif choice == "6":
            op.view_enrollments()

        elif choice == "7":
            op.dashboard()

        elif choice == "8":
            student_id = int(input("Enter student ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            op.update_student(student_id, new_name, new_email)

        elif choice == "9":
            student_id = int(input("Enter student ID to delete: "))
            op.delete_student(student_id)

        elif choice == "10":
            course_id = int(input("Enter course ID to update: "))
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            op.update_course(course_id, new_title, new_description)

        elif choice == "11":
            course_id = int(input("Enter course ID to delete: "))
            op.delete_course(course_id)

        elif choice == "12":
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            progress = int(input("Enter new progress (0-100): "))
            op.update_progress(student_id, course_id, progress)

        elif choice == "13":
            print("👋 Exiting... Goodbye!")
            break


if __name__ == "__main__":
    main()
