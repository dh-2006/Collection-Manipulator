print("=================COLLECTION MANIPULATOR======================")
print()

students = []

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter student details:")

        student_id = int(input("Student ID: "))

        if student_id <= 0:
            print("Invalid Student ID.")
            continue

        found = False

        for student in students:
            old_id, old_dob = student["Student_Info"]

            if old_id == student_id:
                found = True
                break

        if found:
            print("Student ID already exists!")
            continue

        student_name = input("Name: ")
        student_age = int(input("Age: "))

        if student_age < 0:
            print("Age must be greater than 0.")
            continue

        student_grade = input("Grade: ")
        student_dob = input("Date Of Birth (YYYY-MM-DD): ")

        subjects_name = input("Subjects (comma-separated): ").split(",")

        subjects = set()

        for subject in subjects_name:
            subjects.add(subject.strip())

        student_info = (student_id, student_dob)

        student = {
            "Student_Info": student_info,
            "Name": student_name,
            "Age": student_age,
            "Grade": student_grade,
            "Subjects": subjects
        }

        students.append(student)

        print("\nStudent added successfully!!!")


    elif choice == 2:
        print("\n--- Display All Students ---")

        if not students:
            print("No student records found.")

        else:
            for student in students:

                student_id, student_dob = student["Student_Info"]

                print(
                    f"Student ID : {student_id} | "
                    f"Name : {student['Name']} | "
                    f"Age : {student['Age']} | "
                    f"Grade : {student['Grade']} | "
                    f"Subjects : {student['Subjects']}"
                )


    elif choice == 3:

        if not students:
            print("No student records found.")
            continue

        student_id = int(input("\nEnter Student ID to update: "))

        found = False

        for student in students:

            old_id, old_dob = student["Student_Info"]

            if old_id == student_id:
                found = True

                print("Enter new details:")

                student["Name"] = input("New Name: ")

                student_age = int(input("New Age: "))

                if student_age < 0:
                    print("Age must be greater than 0.")
                    break

                student["Age"] = student_age
                student["Grade"] = input("New Grade: ")

                subjects_name = input(
                    "New Subjects (comma-separated): "
                ).split(",")

                subjects = set()

                for subject in subjects_name:
                    subjects.add(subject.strip())

                student["Subjects"] = subjects

                print("Student information updated successfully!")
                break

        if not found:
            print("Student not found!")


    elif choice == 4:

        student_id = int(input("\nEnter student ID to delete: "))

        found = False

        for student in students:

            old_id, old_dob = student["Student_Info"]

            if old_id == student_id:
                found = True

                del students[students.index(student)]

                print("Student deleted successfully!!!")
                break

        if not found:
            print("Student not found!")


    elif choice == 5:
        print("\nSubjects Offered")

        all_subjects = set()

        for student in students:
            all_subjects.update(student["Subjects"])

        if all_subjects:
            for subject in sorted(all_subjects):
                print(subject)

        else:
            print("No subjects available.")


    elif choice == 6:
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")
