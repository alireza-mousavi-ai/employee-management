from decimal import Decimal, InvalidOperation
from datetime import timedelta
import re


def get_decimal(message):
    # Keep asking until the user enters a valid value.
    while True:
        try:
            return Decimal(input(f"Enter {message}:   "))
        except InvalidOperation:
            print("Enter a valid number.")


def get_string(message):
    while True:
        value = input(f"Enter {message}:   ").strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_email(message):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    while True:
        email = input(f"Enter {message}: ").strip()

        if re.match(pattern, email):
            return email

        print("Invalid email address.")


def get_phone(message):
    while True:
        phone = input(f"Enter {message} (ex. 09123456789):   ").strip()

        if phone.isdigit() and len(phone) == 11:
            return phone

        print("Invalid phone number.")


def get_overtime(message: str) -> timedelta:
    """
    Get overtime from user.

    Accepted formats:
        HH:MM   (e.g. 2:30)
        Decimal (e.g. 2.5)

    Returns:
        timedelta
    """

    while True:
        try:
            value = input(f"Enter {message} (HH:MM or decimal): ").strip()

            if ":" in value:
                hours_str, minutes_str = value.split(":", maxsplit=1)

                hours = Decimal(hours_str)
                minutes = Decimal(minutes_str)

            else:
                hours = Decimal(value)
                minutes = Decimal("0")

            if hours < 0:
                print("Hours cannot be negative.")
                continue

            if not (Decimal("0") <= minutes < Decimal("60")):
                print("Minutes must be between 0 and 59.")
                continue

            # Convert Decimal to float because timedelta does not support Decimal.
            return timedelta(hours=float(hours), minutes=float(minutes))

        # Handle both conversion and input format errors.
        except (ValueError, InvalidOperation):
            print("Invalid format. Examples: 2:30 or 2.5")
