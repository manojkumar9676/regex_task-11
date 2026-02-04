# regex_task-11
📌 Regex Validation System in Python
📄 Project Name

Regex Validation System

🧠 Description

This project demonstrates how to use Python Regular Expressions (re module) to validate common user inputs such as:

Email addresses

Indian mobile numbers

Passwords

All validation logic is centralized in a single Python file for better reusability, readability, and maintainability.

🛠️ Technologies Used

Python 3

Regular Expressions (re module)

📁 Project Structure
regex_validation.py
README.md

✨ Features

Validates email addresses using industry-standard regex

Validates Indian mobile numbers (with or without country code)

Validates strong passwords

Accepts dynamic user input

Displays meaningful success and error messages

Handles edge cases like empty input and invalid formats

Uses reusable functions for validation logic

📌 Validation Rules
📧 Email Validation

Must contain @ and domain

Valid characters allowed before and after @

Example: example@gmail.com

📱 Indian Mobile Number Validation

Starts with 6–9

Exactly 10 digits

Optional country code +91 or 91

Examples:

9876543210

+919876543210

🔐 Password Validation

Minimum 8 characters

At least 1 letter

At least 1 digit

At least 1 special character (@$!%*#?&)

Example: Abc@1234

▶️ How to Run the Program

Make sure Python is installed:

python --version


Run the file:

python regex_validation.py


Enter:

Email ID

Indian mobile number

Password

🧪 Edge Cases Handled

Empty input

Invalid email formats

Partial matches

Weak passwords

Invalid mobile numbers

📌 Sample Output
Enter Email ID: test@gmail.com
✅ Valid Email Address

Enter Indian Mobile Number: 9876543210
✅ Valid Indian Mobile Number

Enter Password: Abc@1234
✅ Strong Password

🎯 Learning Outcomes

Understanding regex pattern matching

Using re.fullmatch() effectively

Writing modular and reusable functions

Implementing real-world input validation

Improving code structure and readability

🚀 Future Enhancements

Add unit testing using unittest

Create GUI using Tkinter

Store validation logs in a file

Convert into a menu-driven application

👨‍💻 Author

Manoj

If you want, I can:

Convert this into PDF

Add unit test cases

Make it placement-ready

Explain this line-by-line for viva/exams
