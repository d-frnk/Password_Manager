import json
import secrets
import string

from cryptography.fernet import Fernet
import base64
import hashlib


class PasswordManager:
    def __init__(self, master_password):
        self.fernet = self._create_fernet(master_password)
        self.data = self.load_pass_base()


    def _create_fernet(self,password):
        key = hashlib.sha256(password.encode()).digest()
        return Fernet(base64.urlsafe_b64encode(key))

# Loads the JSON file and handles missing or invalid files.

    def load_pass_base(self):
        try:
            with open("base.json", "rb") as file:
                encrypted_data = file.read()
            if not encrypted_data:
                return {}
            decrypted_data = self.fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode("utf-8"))
        
        except FileNotFoundError:
            return {}
        except Exception:
            print(f"\n[Error] Database cannot be decrypted. Probably Master Password is wrong.")

            return {}

# Loads the JSON database, adds a new password entry, and saves it to the file.

    def add_password(self, service, login):
        data = self.load_pass_base()

        if service in data:
            overwrite = input(f'Service "{service}" already exists. Overwrite? y/n: ')
            if overwrite.lower() != "y":
                print("Operation cancelled.")
                return False
        
        length = self.ask_password_length()
        password = self.generate_password(length)

        data[service] = {
            "login": login,
            "password": password
        }
        self.save_pass_base(data)
        return True

# Saves data to the base.json file.

    def save_pass_base(self, data):
        json_string = json.dumps(data, indent=4)
        encrypted_data = self.fernet.encrypt(json_string.encode("utf-8"))
        with open("base.json", "wb") as file:
            file.write(encrypted_data)


# Generates passwords using the secrets and string modules.

    def generate_password(self, length=16):
        return "".join(secrets.choice(string.ascii_letters + string.punctuation + string.digits)    for _ in range(length))
        


    def ask_password_length(self, default=16):
        while True:
            user_input = input(f"Enter password length (min 8, default {default}): ").strip()
            if not user_input:
                return default
            try:
                length = int(user_input)
                if length >= 8:
                    return length
                print("Password length must be at least 8 characters.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    


    def get_password(self, service):
        data = self.load_pass_base()
        if service in data:
            print(f"Service: {service}")
            print(f"Login: {data[service]['login']}")
            print(f"Password: {data[service]['password']}")
        else:
            print("Service not found.")
    

    def show_list_services(self):
        data = self.load_pass_base()
        if not data:
            print("\nThe database is empty.")
        else:
            print("\nSaved services:")    
            for service_name in data:
                print(f"- {service_name}")
    


    def delete_service(self, service):
        data = self.load_pass_base()

        if service in data:
            confirmation = input(f'Do you want to delete service "{service}"? y/n: ')
            if confirmation.lower() == "y":
                del data[service]
                self.save_pass_base(data)
                print(f'Service "{service}" was deleted.')
            else:
                print("Operation cancelled.")
        else:
            print(f'Service "{service}" does not exist.')


    def change_password(self, service):
        data = self.load_pass_base()

        if service in data:
            confirmation = input(f'Do you want to change service password: "{service}"? y/n: ')
            if confirmation.lower() == "y":
                length = self.ask_password_length()
                data[service]['password'] = self.generate_password(length)
                self.save_pass_base(data)
                return True
            else:
                print("Operation canceled.")
                return False
        else:
            print(f'Service "{service}" does not exist.')
            return False


    


def main():
    master_password = input("Enter Master Password: ").strip()
    if not master_password:
        print("Master password cannot be empty.")
        return

    manager = PasswordManager(master_password)

#### User interface ####

    while True:
        print("\n--- PASSWORD MANAGER ---\n")
        print("Choose option (1 - 6)")
        print("1. List services in the database.")
        print("2. Find a service in the database.")
        print("3. Add a new service to the database.")
        print("4. Delete service from database.")
        print("5. Change service password in the database.")
        print("6. Exit.")

        try: 
            choice = int(input("Choose an option (1-6): "))
        except ValueError:
            print("Error. Enter a digit 1, 2, 3, 4, 5 or 6. ")
            continue

        if choice == 1:
            manager.show_list_services()

        elif choice == 2:
            service = input("Enter the name of the service to search for: ").strip()
            manager.get_password(service)

        elif choice == 3:
            service = input("Enter the name of the service: ").strip()
            if not service:
                print("Service name cannot be empty.")
                continue
            login = input("Enter the login: ").strip()
            if not login:
                print("Login cannot be empty.")
                continue

            if manager.add_password(service, login):
                print("Successfully added!")

        elif choice == 4:
            service = input("Enter the name of the service to delete: ").strip()
            manager.delete_service(service)

        elif choice == 5:
            service = input("Enter the name of the service to change password: ").strip()
            manager.change_password(service)

        elif choice == 6:
            break
        else:
            print("Invalid choice, please try again.")




if __name__ == "__main__":
    main()