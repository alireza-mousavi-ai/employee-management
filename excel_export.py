"""
excel_export.py

Export employee salary information
to Excel file.
"""

from openpyxl import Workbook

from employee import Employee


FILE_NAME = "employees.xlsx"


def export_to_excel(employees: list[Employee]) -> None:
    """Export employee data to an Excel file."""

    # Create a new Excel workbook (Excel file).
    workbook = Workbook()

    # Get the default worksheet from the workbook.
    sheet = workbook.active

    # Rename the worksheet.
    sheet.title = "Employees"

    # Add the header row.
    sheet.append(
        [
            "Employee ID",
            "First Name",
            "Last Name",
            "National ID",
            "Phone Number",
            "Email",
            "Position",
            "Base Salary",
            "Overtime",
            "Overtime Rate",
            "Overtime Pay",
            "Fine",
            "Gross Salary",
            "Net Salary",
        ]
    )

    # Add one row per employee.
    for employee in employees:
        # append() adds a new row to the end of the worksheet.
        sheet.append(
            [
                employee.employee_id,
                employee.first_name,
                employee.last_name,
                employee.national_id,
                employee.phone_number,
                employee.email,
                employee.position,
                # Convert Decimal to float for Excel compatibility.
                float(employee.base_salary),
                # Convert timedelta to a readable string.
                str(employee.overtime),
                float(employee.overtime_rate),
                float(employee.overtime_pay),
                float(employee.fine),
                float(employee.gross_salary),
                float(employee.net_salary),
            ]
        )

    # Save the workbook as an Excel file.
    workbook.save(FILE_NAME)

    print(f"Excel file created successfully: {FILE_NAME}")
