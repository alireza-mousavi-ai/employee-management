"""
main.py

Main controller of Employee Management System.
"""

# This module acts as the application's controller.
# It coordinates other modules without implementing business logic.

from employee import Employee

from validators import (
    get_string,
    get_decimal,
    get_email,
    get_phone,
    get_overtime,
)

from file_manager import (
    save_employee,
    load_employees,
    find_employee,
    delete_employee,
    update_employee,
)

from report import generate_report
from excel_export import export_to_excel


# ---------------------------------
# Create Employee
# ---------------------------------


def create_employee() -> Employee:
    """
    Get employee information from user
    and create an Employee object.
    """

    employee = Employee(
        employee_id=get_string("Employee ID"),
        first_name=get_string("First Name"),
        last_name=get_string("Last Name"),
        national_id=get_string("National ID"),
        phone_number=get_phone("Phone Number"),
        email=get_email("Email"),
        position=get_string("Position"),
        base_salary=get_decimal("Base Salary"),
        overtime=get_overtime("Overtime"),
        overtime_rate=get_decimal("Overtime Rate"),
        fine=get_decimal("Fine"),
    )

    return employee


# ---------------------------------
# Add Employee
# ---------------------------------


def add_employee() -> None:
    """
    Add a new employee to the CSV file.
    """

    employee = create_employee()

    save_employee(employee)

    print("\nEmployee added successfully.")


# ---------------------------------
# Show Employees
# ---------------------------------


def show_employees() -> None:
    """
    Display all employees.
    """

    employees = load_employees()

    if not employees:
        # Exit early if no employees exist.
        return print("\nNo employees found.")

    for employee in employees:
        print("-" * 50)
        print(employee)


# ---------------------------------
# Search Employee
# ---------------------------------


def search_employee() -> None:
    """
    Search for an employee by ID.
    """

    employee_id = get_string("Employee ID")

    employee = find_employee(employee_id)

    if employee is not None:
        print(employee)
    else:
        print("\nEmployee not found.")


# ---------------------------------
# Update Employee
# ---------------------------------


def edit_employee() -> None:
    """
    Update employee information.
    """

    employee_id = get_string("Employee ID")

    employee = find_employee(employee_id)

    if employee is None:
        return print("\nEmployee not found.")  # Exit early if no employees exist.

    print("\nEnter new information:")

    employee.first_name = get_string("First Name")
    employee.last_name = get_string("Last Name")
    employee.phone_number = get_phone("Phone Number")
    employee.email = get_email("Email")
    employee.position = get_string("Position")
    employee.base_salary = get_decimal("Base Salary")
    employee.overtime = get_overtime("Overtime")
    employee.overtime_rate = get_decimal("Overtime Rate")
    employee.fine = get_decimal("Fine")

    update_employee(employee)

    print("\nEmployee updated.")


# ---------------------------------
# Delete Employee
# ---------------------------------


def remove_employee() -> None:
    """
    Delete an employee by ID.
    """

    employee_id = get_string("Employee ID")

    result = delete_employee(employee_id)

    if result:
        print("\nEmployee deleted.")
    else:
        print("\nEmployee not found.")


# ---------------------------------
# Menu
# ---------------------------------


def menu() -> None:
    """
    Display the main menu and handle user choices.
    """

    # Keep showing the menu until the user chooses to exit.
    while True:
        print("""

=================================
 Employee Management System
=================================

1. Add Employee

2. Show Employees

3. Search Employee

4. Update Employee

5. Delete Employee

6. Salary Report

7. Export Excel

0. Exit

=================================

""")

        choice = input("Select option: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            edit_employee()

        elif choice == "5":
            remove_employee()

        # elif choice == "6":
        #     employees = load_employees()
        #     generate_report(employees)
        # To understand the cause of the project error in reporting
        elif choice == "6":
            try:
                employees = load_employees()

                generate_report(employees)

            except Exception as error:
                print("\nREPORT ERROR:")
                print(type(error).__name__)
                print(error)

        elif choice == "7":
            employees = load_employees()
            export_to_excel(employees)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


# ---------------------------------
# Program Entry Point
# ---------------------------------

# Run the application only when this file is executed directly.
if __name__ == "__main__":
    menu()
