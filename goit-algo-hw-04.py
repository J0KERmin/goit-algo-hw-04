# 1:
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Invalid data format in line: {line.strip()}")
                    continue
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    if count == 0:
        print("No valid data found in the file.")
        return None

    average = total / count
    return total, average


# Приклад використання функції:
result = total_salary(r"C:\Users\Acer\Desktop\GoIT\4 Module\salaries.txt")
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# 2:
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Invalid data format in line: {line.strip()}")
                    continue
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    if not cats_info:
        print("No valid data found in the file.")
        return None

    return cats_info


# Приклад використання функції:
cats_info = get_cats_info(r"C:\Users\Acer\Desktop\GoIT\4 Module\cats_file.txt")
if cats_info:
    for cat in cats_info:
        print(cat)

# 4:
def add_contact(phone_book, name, phone_number):
    phone_book[name] = phone_number
    print(f"Contact {name} with phone number {phone_number} has been added.")


def change_contact(phone_book, name, new_phone_number):
    if name in phone_book:
        phone_book[name] = new_phone_number
        print(f"Phone number for {name} has been changed to {new_phone_number}.")
    else:
        print(f"Contact {name} not found.")


def show_phone(phone_book, name):
    if name in phone_book:
        print(f"Phone number for {name} is {phone_book[name]}.")
    else:
        print(f"Contact {name} not found.")


def show_all_contacts(phone_book):
    if not phone_book:
        print("Phone book is empty.")
    else:
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")


def parse_input(input_str):
    tokens = input_str.strip().split()
    command = tokens[0].lower()
    args = tokens[1:]
    return command, args


def show_commands():
    print("Available commands:")
    print("hello: Say hello.")
    print("add <name> <phone_number>: Add a new contact with the given name and phone number.")
    print("change <name> <new_phone_number>: Change the phone number for the contact with the given name.")
    print("phone <name>: Show the phone number for the contact with the given name.")
    print("all: Show all contacts.")
    print("close or exit: Exit the program.")


def main():
    phone_book = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        
        if command == "hello":
            print("Hello! How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Usage: add <name> <phone_number>")
            else:
                name, phone_number = args
                add_contact(phone_book, name, phone_number)
        elif command == "change":
            if len(args) != 2:
                print("Usage: change <name> <new_phone_number>")
            else:
                name, new_phone_number = args
                change_contact(phone_book, name, new_phone_number)
        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone <name>")
            else:
                name = args[0]
                show_phone(phone_book, name)
        elif command == "all":
            show_all_contacts(phone_book)
        elif command == "commands":
            show_commands()
        elif command == "exit" or command == "close" or command == "bye":
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()



