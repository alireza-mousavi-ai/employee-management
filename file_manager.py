import csv
from datetime import timedelta
from decimal import Decimal

from employee import Employee

# from pathlib import Path


# -------------------------------
# Configuration
# -------------------------------

# CSV file path
# Resolve the directory of the current file and build the CSV path.
# Keeping the file path centralized improves maintainability
# and ensures the application can find the CSV file correctly.
# BASE_DIR = Path(__file__).resolve().parent
# FILE_NAME = BASE_DIR / "employees.csv"

FILE_NAME = "employees.csv"


# CSV column names
# Centralize CSV column names to avoid duplication.
FIELDS = [
    "employee_id",
    "first_name",
    "last_name",
    "national_id",
    "phone_number",
    "email",
    "position",
    "base_salary",
    "overtime",
    "overtime_rate",
    "fine",
]


# -------------------------------
# Helper Functions
# -------------------------------


def parse_timedelta(value: str) -> timedelta:
    """
    Convert a string such as:

        2:30:00

    to

        timedelta(hours=2, minutes=30)
    """

    hours, minutes, seconds = map(int, value.split(":"))

    return timedelta(
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )


# -------------------------------
# Write Functions
# -------------------------------


def save_employee(employee: Employee) -> None:
    """
    Add ONE employee to the end of CSV.

    Used when adding a new employee.
    """

    try:
        # Context manager automatically closes the file, even if an error occurs.
        with open(FILE_NAME, "a", newline="", encoding="utf-8-sig") as file:
            # Prevent blank lines when writing CSV on Windows.
            # Use UTF-8 BOM for better Excel compatibility.
            writer = csv.DictWriter(file, fieldnames=FIELDS)

            # If the file is empty,
            # write the header first.
            # or
            # Write header only when creating a new file.
            if file.tell() == 0:
                writer.writeheader()

            # Convert Employee object to dictionary
            writer.writerow(employee.to_dict())

    # print() is sufficient for this small project.
    # In larger applications, use the logging module for better error tracking.
    except OSError as error:
        print(f"File Error: {error}")


def save_all_employees(employees: list[Employee]) -> None:
    """
    Rewrite the whole CSV.

    Used after:
        - delete
        - update

    because CSV files cannot edit
    or delete a single row directly.
    """

    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)

            writer.writeheader()

            # Write every employee again
            for employee in employees:
                writer.writerow(employee.to_dict())

    except OSError as error:
        print(f"File Error: {error}")


# -------------------------------
# Read Functions
# -------------------------------


def load_employees() -> list[Employee]:
    """
    Read all employees from CSV
    and return a list of Employee objects.
    """

    employees = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                employee = Employee(
                    employee_id=row["employee_id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    national_id=row["national_id"],
                    phone_number=row["phone_number"],
                    email=row["email"],
                    position=row["position"],
                    # Convert strings back to Decimal
                    base_salary=Decimal(row["base_salary"]),
                    overtime=parse_timedelta(row["overtime"]),
                    overtime_rate=Decimal(row["overtime_rate"]),
                    fine=Decimal(row["fine"]),
                )

                employees.append(employee)

    except FileNotFoundError:
        # If the file doesn't exist yet,
        # simply return an empty list.
        pass

    return employees


# -------------------------------
# Search Functions
# -------------------------------


def find_employee(employee_id: str) -> Employee | None:
    """
    Find an employee by ID.

    Returns:
        Employee object

    or

        None
    """

    employees = load_employees()

    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
        # Use early returns (guard clauses) to reduce unnecessary nesting.
        # If a branch ends with return, raise, break, or continue,
        # an 'else' block is usually unnecessary.

    return None


# -------------------------------
# Delete Functions
# -------------------------------


def delete_employee(employee_id: str) -> bool:
    """
    Delete an employee.

    Returns:
        True  -> deleted successfully

        False -> employee not found
    """

    employees = load_employees()

    # Keep every employee except
    # the one we want to delete.
    # List Comprehension
    new_employees = [
        employee for employee in employees if employee.employee_id != employee_id
    ]

    # Nothing was removed.
    if len(new_employees) == len(employees):
        return False

    # Rewrite CSV.
    save_all_employees(new_employees)

    return True


# -------------------------------
# Update Functions
# -------------------------------


def update_employee(updated_employee: Employee) -> bool:
    """
    Update an existing employee.

    Returns:
        True  -> updated

        False -> employee not found
    """

    employees = load_employees()

    for index, employee in enumerate(employees):
        if employee.employee_id == updated_employee.employee_id:
            # Replace old object
            employees[index] = updated_employee

            save_all_employees(employees)

            return True

    return False
