# PS 15 - Student Record Management System
# Concepts: Lists, Tuples, Dictionaries, CRUD
#
# students = dictionary  ->  roll number : (name, course, marks)   <- tuple
# Run:  python student_records.py          (menu)
#       python student_records.py test     (runs the 4 test cases)

import sys

students = {}


def add_record(roll, name, course, marks):
    if roll in students:
        return "Roll number " + str(roll) + " already exists."
    if marks < 0 or marks > 100:
        return "Marks must be between 0 and 100."
    students[roll] = (name, course, marks)
    return "Record added: " + str(roll) + " | " + name + " | " + course + " | " + str(marks)


def view_records():
    if len(students) == 0:
        print("No records found.")
        return
    print("-" * 40)
    print("Roll No  Name        Course      Marks")
    print("-" * 40)
    for roll in sorted(students):
        name, course, marks = students[roll]
        print(str(roll).ljust(9) + name.ljust(12) + course.ljust(12) + str(marks))
    print("-" * 40)


def search_record(roll):
    if roll not in students:
        return "Roll number " + str(roll) + " not found."
    name, course, marks = students[roll]
    return str(roll) + " | " + name + " | " + course + " | " + str(marks)


def update_marks(roll, new_marks):
    if roll not in students:
        return "Roll number " + str(roll) + " not found."
    if new_marks < 0 or new_marks > 100:
        return "Marks must be between 0 and 100."
    name, course, old_marks = students[roll]
    students[roll] = (name, course, new_marks)
    return "Marks updated: " + str(new_marks)


def delete_record(roll):
    if roll not in students:
        return "Roll number " + str(roll) + " not found."
    del students[roll]
    return "Record deleted: " + str(roll)


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a number.")


def menu():
    options = ["1. Add", "2. View all", "3. Search", "4. Update marks", "5. Delete", "6. Exit"]
    while True:
        print("\n--- Student Record Management System ---")
        for item in options:
            print(item)
        choice = input("Enter choice: ")

        if choice == "1":
            roll = get_number("Roll number: ")
            name = input("Name: ")
            course = input("Course: ")
            marks = get_number("Marks: ")
            print(add_record(roll, name, course, marks))
        elif choice == "2":
            view_records()
        elif choice == "3":
            print(search_record(get_number("Roll number: ")))
        elif choice == "4":
            roll = get_number("Roll number: ")
            marks = get_number("New marks: ")
            print(update_marks(roll, marks))
        elif choice == "5":
            print(delete_record(get_number("Roll number: ")))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def check(title, actual, expected):
    print(title)
    print("  Output  :", actual)
    print("  Expected:", expected)
    print("  ", "PASS" if actual == expected else "FAIL")
    return actual == expected


def run_tests():
    results = []
    results.append(check("Test 1: Add 101, Aman, BTech, 78",
                         add_record(101, "Aman", "BTech", 78),
                         "Record added: 101 | Aman | BTech | 78"))
    results.append(check("Test 2: Add 102, Riya, BTech, 100",
                         add_record(102, "Riya", "BTech", 100),
                         "Record added: 102 | Riya | BTech | 100"))
    results.append(check("Test 3a: Add 101, Neha, BTech, 70",
                         add_record(101, "Neha", "BTech", 70),
                         "Roll number 101 already exists."))
    results.append(check("Test 3b: Add 103, Ravi, BTech, 150",
                         add_record(103, "Ravi", "BTech", 150),
                         "Marks must be between 0 and 100."))
    results.append(check("Test 4a: Search 101", search_record(101), "101 | Aman | BTech | 78"))
    results.append(check("Test 4b: Update marks of 101 to 85", update_marks(101, 85), "Marks updated: 85"))
    results.append(check("Test 4c: Delete 999", delete_record(999), "Roll number 999 not found."))
    print("\nFinal records:")
    view_records()
    print("\nPassed", results.count(True), "of", len(results))


if len(sys.argv) > 1 and sys.argv[1] == "test":
    run_tests()
else:
    menu()