"""Simple student-record analytics."""
from collections import Counter

def show_analytics(students):
    print("\n========== STUDENT ANALYTICS ==========")
    print(f"Total registered students : {len(students)}")
    if not students:
        print("No course data available yet.")
        return
    counts = Counter(s["course"] for s in students)
    print("Students by course:")
    for course, count in sorted(counts.items()):
        print(f"  {course}: {count}")
    print("=======================================\n")
