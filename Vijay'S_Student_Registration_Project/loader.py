"""CSV storage functions for the CAIAS student registration system."""
import csv
from pathlib import Path

FIELDS = ["student_id", "name", "email", "phone", "course"]
DEFAULT_FILE = Path(__file__).with_name("contacts.csv")

def load_students(file_path=DEFAULT_FILE):
    path = Path(file_path)
    if not path.exists():
        save_students([], path)
        return []
    with path.open("r", newline="", encoding="utf-8-sig") as file:
        return [
            {field: (row.get(field) or "").strip() for field in FIELDS}
            for row in csv.DictReader(file)
        ]

def save_students(students, file_path=DEFAULT_FILE):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for student in students:
            writer.writerow({field: student.get(field, "") for field in FIELDS})
