"""
regex_validation.py
Centralized validation logic using Regular Expressions
"""

import re


# -----------------------------
# Regex Patterns
# -----------------------------

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

INDIAN_MOBILE_PATTERN = r'^(?:\+91|91)?[6-9]\d{9}$'

PASSWORD_PATTERN = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'


# -----------------------------
# Validation Functions
# -----------------------------

def validate_email(email: str) -> bool:
    if not email:
        print("❌ Email cannot be empty")
        return False
    if re.fullmatch(EMAIL_PATTERN, email):
        print("✅ Valid Email Address")
        return True
    else:
        print("❌ Invalid Email Format")
        return False


def validate_mobile(mobile: str) -> bool:
    if not mobile:
        print("❌ Mobile number cannot be empty")
        return False
    if re.fullmatch(INDIAN_MOBILE_PATTERN, mobile):
        print("✅ Valid Indian Mobile Number")
        return True
    else:
        print("❌ Invalid Mobile Number")
        return False


def validate_password(password: str) -> bool:
    if not password:
        print("❌ Password cannot be empty")
        return False
    if re.fullmatch(PASSWORD_PATTERN, password):
        print("✅ Strong Password")
        return True
    else:
        print(
            "❌ Invalid Password\n"
            "Password must contain:\n"
            "- Minimum 8 characters\n"
            "- At least 1 letter\n"
            "- At least 1 digit\n"
            "- At least 1 special character (@$!%*#?&)"
        )
        return False


# -----------------------------
# Main Program
# -----------------------------

def main():
    print("\n--- REGEX VALIDATION SYSTEM ---\n")

    email = input("Enter Email ID: ").strip()
    validate_email(email)

    print()

    mobile = input("Enter Indian Mobile Number: ").strip()
    validate_mobile(mobile)

    print()

    password = input("Enter Password: ").strip()
    validate_password(password)


# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
    main()
