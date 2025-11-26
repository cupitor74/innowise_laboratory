students = []

def add_new_student():
    student = {"name": "",
               "grades": []
               }
    try:
        name = input("Enter student name: ").strip()

        if name.isdigit():
            raise ValueError("Name cannot be only numbers.")

        if any(name == std["name"] for std in students):
            print(f"Student with {name} exists")
        else:
            student["name"] = name
            students.append(student)
    except  ValueError as e:
        print(f"Input error: {e}")


def add_grade_student():
    try:
        name = input("Enter student name: ").strip()
        if name.isdigit() or not name:
            raise ValueError("Name cannot be empty or only numbers.")

        found_student = next((std for std in students if std["name"] == name), None)

        if not found_student:
            print(f"Student '{name}' not found.")
            return

        while True:
            entered_grade = input("Enter a grade (or 'done' to finish): ").strip()

            if entered_grade.lower() == "done":
                break

            try:
                grade_int = int(entered_grade)
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
                # if not (0 <= grade_int <= 100):

            if not (0 <= grade_int <= 100):
                print("Please enter integer number between 0 and 100.")
                continue

            found_student["grades"].append(grade_int)
    except ValueError as e:
        print(f"Invalid input: {e}")


def generate_report():
    print("---Student Report---")
    if not students:
        print("Students list is empty. Add students to get a report.")
        return

    available_averages = all(len(std['grades']) == 0 for std in students)
    if available_averages:
        print("All students have no available averages.")
        return

    averages= []
    for student in students:
        student_name = student["name"]
        student_grades = student["grades"]

        try:
            if not student_grades:
                raise ZeroDivisionError

            student_avg = sum(student_grades) / len(student_grades)
            averages.append(student_avg)
            print(f"{student_name}'s average grade is {student_avg}.")

        except ZeroDivisionError:
                print(f"{student_name}'s average grade is N/A.")


    overall_averages = sum(averages) / len(averages)
    max_averages = max(averages)
    min_averages = min(averages)
    print("------------------------")
    print(f"Max average: {max_averages:.2f}")
    print(f"Min average: {min_averages:.2f}")
    print(f"Overall average: {overall_averages:.2f}")


def find_top_student():
    if not students:
        print("Students list is empty. Add students to get a report.")
        return

    found_students = []

    for student in students:
        try:
            if 'grades' in student and isinstance(student['grades'], list) and len(student['grades']) > 0:
                found_students.append(student)
        except (KeyError, TypeError):
            continue

    if not found_students:
        print("No students with grades found.")
        return


    top_student = max(found_students, key=lambda std: sum(std['grades']) / len(std['grades']))
    average_grade = sum(top_student['grades']) / len(top_student['grades'])

    print(f"The student with the highest average is {top_student['name']} with a grade of {average_grade:.2f}")


def grade_analyser():
    text_menu = """---Student Grade Analyzer---
1. Add a new student
2. Add a grades for a students
3. Show report (all students)
4. Find top performer
5. Exit
Enter Option:"""

    while True:

        try:
            option_menu = int(input(text_menu).strip())
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        match option_menu:
            case 1:
                add_new_student()
            case 2:
                add_grade_student()
            case 3:
                generate_report()
            case 4:
                find_top_student()
            case 5:
                print("Existing Program.")
                break


grade_analyser()