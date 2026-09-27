import json
import secrets
import string


# Loads the JSON file and handles missing or invalid files.

def load_pass_base():
    try:
        with open("base.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    return data

# Saves data to the base.json file.

def save_pass_base(data):
    with open("base.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Generates passwords using the secrets and string modules.

def generate_password(length=16):
    password = "".join(secrets.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(length))
    return password

def get_password(service):
    data = load_pass_base()
    if service in data:
        print(f"Service: {service}")
        print(f"Login: {data[service]['login']}")
        print(f"Password: {data[service]['password']}")
    else:
        print("Service not found.")
    

def show_list_services(data):
    if not data:
        print("\nThe database is empty.")
    else:
        print("\nSaved services:")    
        for service_name in data:
            print(f"- {service_name}")
    


# Loads the JSON database, adds a new password entry, and saves it to the file.

def add_password(service, login):
    data = load_pass_base()

    if service in data:
        overwrite = input(f'Service "{service}" already exists. Overwrite? y/n: ')
        if overwrite.lower() != "y":
            print("Operation cancelled.")
            return False


    password = generate_password()

    data[service] = {
        "login": login,
        "password": password
    }
    save_pass_base(data)
    return True


def delete_password(service):
    data = load_pass_base()

    if service in data:
        confirmation = input(f'Do you want to delete service "{service}"? y/n: ')
        if confirmation.lower() == "y":
            del data[service]
            save_pass_base(data)
            print(f'Service "{service}" was deleted.')
        else:
            print("Operation cancelled.")
    else:
        print(f'Service "{service}" does not exist.')



#### User interface ####



while True:
    print("\n--- PASSWORD MANAGER ---\n")
    print("Choose option (1 - 5)")
    print("1. List services in the database.")
    print("2. Find a service in the database.")
    print("3. Add a new service to the database.")
    print("4. Delete service from database.")
    print("5. Exit.")

    try: 
        choice = int(input("Choose an option (1-5): "))
    except ValueError:
        print("Error. Enter a digit 1, 2, 3, 4 or 5. ")
        continue

    if choice == 1:
        data = load_pass_base()
        show_list_services(data)

    elif choice == 2:
        service = input("Enter the name of the service to search for: ").strip()
        get_password(service)

    elif choice == 3:
        service = input("Enter the name of the service: ").strip()
        if not service:
            print("Service name cannot be empty.")
            continue
        login = input("Enter the login: ").strip()
        if not login:
            print("Login cannot be empty.")
            continue

        if add_password(service, login):
            print("Successfully added!")

    elif choice == 4:
        service = input("Enter the name of the service to delete: ").strip()
        delete_password(service)

    elif choice == 5:
        break
    else:
        print("Invalid choice, please try again.")

    