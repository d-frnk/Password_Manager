Python Password Manager

A simple command-line password manager written in Python.

Note: This project is currently in an early stage of development. New features, code improvements, and security enhancements will be introduced gradually.

Warning: This is an educational project intended for learning and improving Python programming skills. It is not recommended for storing real passwords or sensitive information, as the current implementation has known security limitations.

Features
Generate random passwords using Python's secrets module.
Customize password length (minimum 8 characters, default 16).
Encrypt the password database using Fernet symmetric encryption.
Use a master password to derive the encryption key.
Store encrypted password data in a local file (base.json).
Load and decrypt the password database when the application starts.
Handle missing database files.
List saved services.
Search for saved services and display their credentials.
Detect duplicate services and ask for confirmation before overwriting entries.
Delete existing services with user confirmation.
Generate new passwords for existing services.
Validate user input and prevent empty service names, logins, and master passwords.
Provide an interactive command-line interface (CLI).
Requirements
Python 3.x
cryptography

The project uses the following Python standard library modules:

json — serialize and deserialize password data.
secrets — generate cryptographically secure random passwords.
string — provide character sets for password generation.
base64 — encode the encryption key in a format accepted by Fernet.
hashlib — derive the encryption key from the master password.
Installation

Clone the repository and navigate to the project directory:

git clone <repository-url>
cd PassManager


Install the required dependency:

pip install cryptography

How to Run

Run the application:

python main.py


Enter your master password when prompted, then select an option from the menu.

The application supports the following operations:

List saved services.
Search for a service and display its credentials.
Add a new service and generate a password.
Delete an existing service.
Generate a new password for an existing service.
Exit the application.

The encrypted database is stored in base.json in the application's working directory.

Encryption

The application uses the Fernet implementation provided by the cryptography library to encrypt and decrypt the password database.

The current implementation derives a 32-byte key from the master password using SHA-256 and encodes it using URL-safe Base64 before passing it to Fernet.

Important: Although the database is encrypted, the current key derivation approach is not sufficiently resistant to offline password-guessing attacks. A stronger key derivation function, such as Scrypt or PBKDF2HMAC, together with a randomly generated salt, is planned for a future version.

The master password is not stored in the database. However, losing it means the encrypted database cannot normally be recovered.

Current Limitations
The encryption key is derived using a fast SHA-256 hash rather than a password-based key derivation function.
No salt is currently used when deriving the encryption key.
The master password is entered using input(), so it is visible while typing.
An incorrect master password or corrupted database can cause the application to treat the database as empty, potentially leading to accidental data loss if new data is saved.
Database writes are not atomic, so an interrupted write may damage the database.
Passwords are displayed in plain text when retrieved.
There is no graphical user interface.
Automated unit tests have not yet been implemented.

These limitations are acknowledged and will be addressed gradually as the project develops.

Roadmap

Planned improvements include:

Replace SHA-256 key derivation with Scrypt or PBKDF2HMAC.
Introduce a randomly generated salt for key derivation.
Hide master password input using Python's getpass module.
Improve error handling for incorrect master passwords and corrupted databases.
Implement safer database saving and backup mechanisms.
Add unit tests for password generation, encryption, and database operations.
Improve the command-line interface and user experience.
Add the ability to edit saved logins and other service details.
Introduce optional password generation settings.
Consider developing a graphical user interface (GUI).
Project Status

This project is primarily intended for educational purposes and for improving my Python programming skills.

It is an ongoing personal project focused on learning object-oriented programming, file handling, password generation, encryption, and secure application design.

Features and security improvements will be implemented incrementally as the project evolves.