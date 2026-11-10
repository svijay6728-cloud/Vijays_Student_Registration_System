"""Validation functions for the CAIAS student registration system."""
import re

def validate_student(record):
    """Return (is_valid, error_message) for a student dictionary."""
    required = ("student_id", "name", "email", "phone", "course")
    for field in required:
        if not str(record.get(field, "")).strip():
            return False, f"{field.replace('_', ' ').title()} cannot be empty."

    if not re.fullmatch(r"[A-Za-z0-9_-]{3,12}", record["student_id"].strip()):
        return False, "Student ID must be 3-12 characters (letters, digits, _ or -)."

    if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]{1,59}", record["name"].strip()):
        return False, "Enter a valid name (letters, spaces, apostrophes, dots or hyphens)."

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", record["email"].strip()):
        return False, "Enter a valid email address."

    digits = re.sub(r"\D", "", record["phone"])
    if len(digits) != 10:
        return False, "Phone number must contain exactly 10 digits."

    if len(record["course"].strip()) > 60:
        return False, "Course name must be 60 characters or fewer."

    return True, ""
