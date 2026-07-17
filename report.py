"""
report.py

Generate salary reports and statistics
for employees.
"""

from decimal import Decimal

from employee import Employee


def employee_count(employees: list[Employee]) -> int:
    """
    Return number of employees.
    """

    return len(employees)


def total_base_salary(employees: list[Employee]) -> Decimal:
    """
    Calculate total base salary.
    """

    # Generator Expression: # Generator expression avoids creating an intermediate list.
    return sum(employee.base_salary for employee in employees)


def total_overtime_pay(employees: list[Employee]) -> Decimal:
    """
    Calculate total overtime payment.
    """

    return sum(employee.overtime_pay for employee in employees)


def total_fines(employees: list[Employee]) -> Decimal:
    """
    Calculate total fines.
    """

    return sum(employee.fine for employee in employees)


def total_gross_salary(employees: list[Employee]) -> Decimal:
    """
    Calculate total gross salary.
    """

    return sum(employee.gross_salary for employee in employees)


def total_net_salary(employees: list[Employee]) -> Decimal:
    """
    Calculate total net salary.
    """

    return sum(employee.net_salary for employee in employees)


def average_net_salary(employees: list[Employee]) -> Decimal:
    """
    Calculate average net salary.
    """
    # Avoid division by zero when the list is empty.
    if not employees:
        return Decimal("0")

    return total_net_salary(employees) / Decimal(len(employees))


def highest_salary(employees: list[Employee]) -> Employee | None:
    """
    Return employee with highest net salary.
    """

    if not employees:
        return None

    # Compare employees by their net salary and return the employee object.
    return max(employees, key=lambda employee: employee.net_salary)


def lowest_salary(employees: list[Employee]) -> Employee | None:
    """
    Return employee with lowest net salary.
    """

    if not employees:
        return None

    # Compare employees by their net salary and return the employee object.
    return min(employees, key=lambda employee: employee.net_salary)


def print_employee_details(employees: list[Employee]) -> None:
    """
    Print salary details of all employees.
    """

    print("\n")
    print("=" * 60)
    print("EMPLOYEE DETAILS")
    print("=" * 60)

    for employee in employees:
        print(f"""
Employee ID   : {employee.employee_id}

Name          : {employee.first_name} {employee.last_name}

Position      : {employee.position}

-------------------------------

Base Salary   : {employee.base_salary}

Overtime      : {employee.overtime}

Overtime Pay  : {employee.overtime_pay}

Fine          : {employee.fine}

-------------------------------

Gross Salary  : {employee.gross_salary}

Net Salary    : {employee.net_salary}

{"=" * 60}
""")


# Orchestrates report generation by combining smaller helper functions.
def generate_report(employees: list[Employee]) -> None:
    """
    Generate complete salary report.
    """

    print("\n")
    print("=" * 60)
    print("EMPLOYEE SALARY REPORT".center(60))
    print("=" * 60)

    print(f"Number of Employees : {employee_count(employees)}")

    print()

    print(f"Total Base Salary   : {total_base_salary(employees)}")

    print(f"Total Overtime Pay  : {total_overtime_pay(employees)}")

    print(f"Total Fines         : {total_fines(employees)}")

    print()

    print(f"Total Gross Salary  : {total_gross_salary(employees)}")

    print(f"Total Net Salary    : {total_net_salary(employees)}")

    print()

    print(f"Average Net Salary  : {average_net_salary(employees)}")

    # Highest salary employee

    highest = highest_salary(employees)

    if highest:
        print("\nHighest Salary:")

        # Split a long f-string across multiple lines for better readability.
        # "->" is only a visual separator in the output.
        print(f"{highest.first_name} {highest.last_name} -> {highest.net_salary:,.2f}")

    # Lowest salary employee

    lowest = lowest_salary(employees)

    if lowest:
        print("\nLowest Salary:")

        print(f"{lowest.first_name} {lowest.last_name} -> {lowest.net_salary:,.2f}")

    print_employee_details(employees)
