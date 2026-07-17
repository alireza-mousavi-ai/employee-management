from datetime import timedelta
from decimal import Decimal


class Employee:
    """Represents an employee and provides salary calculations."""

    # Instead of __init__, we can use @dataclass.
    #     @dataclass
    # class Employee:

    def __init__(
        self,
        employee_id: str,
        first_name: str,
        last_name: str,
        national_id: str,
        phone_number: str,
        email: str,
        position: str,
        base_salary: Decimal,
        overtime: timedelta,
        overtime_rate: Decimal,
        fine: Decimal,
    ) -> None:
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.base_salary = base_salary
        self.overtime = overtime
        self.overtime_rate = overtime_rate
        self.fine = fine

    # Use @property for computed values to provide attribute-like access.
    @property
    def overtime_hours(self) -> Decimal:
        """Return overtime as decimal hours."""
        # Convert float to string first to preserve Decimal precision.
        return Decimal(str(self.overtime.total_seconds())) / Decimal("3600")

    @property
    def overtime_pay(self) -> Decimal:
        """Calculate overtime payment."""
        return self.overtime_hours * self.overtime_rate

    @property
    def gross_salary(self) -> Decimal:
        """Return gross salary."""
        return self.base_salary + self.overtime_pay

    @property
    def net_salary(self) -> Decimal:
        """Return net salary."""
        return self.gross_salary - self.fine

    def to_dict(self) -> dict[str, str]:
        """Convert employee object to a dictionary for CSV writing."""
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "national_id": self.national_id,
            "phone_number": self.phone_number,
            "email": self.email,
            "position": self.position,
            # CSV stores text, so convert Decimal explicitly.
            "base_salary": str(self.base_salary),
            "overtime": str(self.overtime),
            "overtime_rate": str(self.overtime_rate),
            "fine": str(self.fine),
        }

    def __str__(self) -> str:
        return (
            f"Employee ID : {self.employee_id}\n"
            f"Name        : {self.first_name} {self.last_name}\n"
            f"Position    : {self.position}\n"
            f"Net Salary  : {self.net_salary}"
        )
