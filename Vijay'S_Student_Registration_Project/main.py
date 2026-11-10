"""Menu-driven CLI: View, Search, Add, Update and Delete students."""
from loader import load_students, save_students
from validator import validate_student
from analytics import show_analytics

def print_students(students):
    if not students:
        print("\nNo student records found.\n")
        return
    print("\n{:<12} {:<22} {:<30} {:<14} {}".format(
        "STUDENT ID", "NAME", "EMAIL", "PHONE", "COURSE"))
    print("-" * 100)
    for s in students:
        print("{:<12} {:<22} {:<30} {:<14} {}".format(
            s["student_id"], s["name"], s["email"], s["phone"], s["course"]))
    print()

def find_by_id(students, student_id):
    return next((s for s in students if s["student_id"].lower() == student_id.lower()), None)

def view_students(students):
    print_students(students)

def search_student(students):
    term = input("Enter Student ID, name or email to search: ").strip().lower()
    matches = [s for s in students if term in s["student_id"].lower()
               or term in s["name"].lower() or term in s["email"].lower()]
    print_students(matches)

def collect_student(existing=None):
    existing = existing or {}
    prompts = [
        ("student_id", "Student ID"),
        ("name", "Full name"),
        ("email", "Email"),
        ("phone", "10-digit phone"),
        ("course", "Course"),
    ]
    result = {}
    for key, label in prompts:
        current = existing.get(key, "")
        value = input(f"{label}" + (f" [{current}]" if current else "") + ": ").strip()
        result[key] = value if value else current
    return result

def add_student(students):
    print("\n--- Add New Student (leave fields blank only if keeping an existing value) ---")
    record = collect_student()
    valid, error = validate_student(record)
    if not valid:
        print(f"Cannot add student: {error}")
        return
    if find_by_id(students, record["student_id"]):
        print("Cannot add student: Student ID already exists.")
        return
    if any(s["email"].lower() == record["email"].lower() for s in students):
        print("Cannot add student: Email address already exists.")
        return
    students.append(record)
    save_students(students)
    print("Student added and saved successfully.")

def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()
    old = find_by_id(students, student_id)
    if not old:
        print("Student ID not found.")
        return
    print("Enter new values. Press Enter to keep the current value.")
    updated = collect_student(old)
    valid, error = validate_student(updated)
    if not valid:
        print(f"Update cancelled: {error}")
        return
    if updated["student_id"].lower() != old["student_id"].lower() and find_by_id(students, updated["student_id"]):
        print("Update cancelled: Student ID already exists.")
        return
    if any(s is not old and s["email"].lower() == updated["email"].lower() for s in students):
        print("Update cancelled: Email address already exists.")
        return
    old.update(updated)
    save_students(students)
    print("Student updated and saved successfully.")

def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()
    student = find_by_id(students, student_id)
    if not student:
        print("Student ID not found.")
        return
    confirm = input(f"Delete {student['name']} ({student['student_id']})? Type YES to confirm: ").strip()
    if confirm == "YES":
        students.remove(student)
        save_students(students)
        print("Student deleted and CSV updated.")
    else:
        print("Deletion cancelled.")

def main():
    students = load_students()
    actions = {
        "1": lambda: view_students(students),
        "2": lambda: search_student(students),
        "3": lambda: add_student(students),
        "4": lambda: update_student(students),
        "5": lambda: delete_student(students),
        "6": lambda: show_analytics(students),
    }
    while True:
        print("\n========== CAIAS STUDENT MANAGEMENT SYSTEM ==========")
        print("1. View All Students")
        print("2. Search Student")
        print("3. Add New Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Analytics")
        print("7. Save and Exit")
        choice = input("Choose an option (1-7): ").strip()
        if choice in actions:
            actions[choice]()
        elif choice == "7":
            save_students(students)
            print("All changes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
