Python Password Manager

A simple command-line password manager written in Python.

Note: This project is currently in an early stage of development. More features and security improvements will be added in future versions.

Warning: This is an educational project and is not intended for storing real passwords or sensitive information. The current version does not provide adequate security for real-world use.

Features

- Generate random passwords using Python's secrets module.
- Store password data in a JSON file.
- Handle missing or invalid JSON files.
- Interactive command-line interface.
- List saved services.
- Search for saved services and display their credentials.
- Detect duplicate services and allow entries to be overwritten.
- Delete existing services from the database.
- User input validation (stripping whitespace and preventing empty entries).

Requirements

Python 3.x

No external dependencies

The project currently uses only Python's standard library:
- json
- secrets
- string

How to Run

Clone the repository and navigate to the project directory:

git clone <repository-url>
cd PassManager

Run the application:

python main.py

The application will create and use a base.json file to store password data.

Note: base.json is excluded from Git using .gitignore because it contains sensitive data in plain text.

Current Limitations

- Passwords are currently stored in plain text in a JSON file.
- The database is not encrypted.
- There is no master password.
- The password generator does not yet allow customization of password requirements.

These limitations are planned to be addressed in future versions.

Roadmap

Planned improvements include:

- Password editing
- Custom password length
- Customizable password generation
- Unit tests
- Master password
- Encrypted password database
- Safer database handling
- Graphical user interface (GUI)

Project Status

This project is mainly intended for learning and improving my Python programming skills.

Security improvements will be implemented gradually as the project develops.