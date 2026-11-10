# CAIAS Student Registration System

A menu-driven Python CLI project using CSV files and four modules.

## Files
- `main.py` — interactive menu and CRUD operations.
- `loader.py` — reads and writes CSV records.
- `validator.py` — validates student details.
- `analytics.py` — displays total registrations and course counts.
- `contacts.csv` — editable student/contact dataset.
- `students_clean.csv` — copy of the supplied clean sample data.

## Requirements
Python 3.8 or newer. No third-party packages are required.

## Run in Jupyter Notebook
Open this folder in Jupyter and run in a notebook cell:
```python
%run main.py
```

Alternatively, open a terminal in this folder and run:
```bash
python main.py
```

## CLI operations
1. View all students
2. Search by Student ID, name or email
3. Add a student
4. Update a student (press Enter to keep a field unchanged)
5. Delete a student (requires typing `YES`)
6. View analytics
7. Save and exit

All successful add, update and delete operations are saved immediately to `contacts.csv`.
Student IDs and email addresses must be unique.
