# Person class represents an individual contact
class Person:
    def __init__(self, name, number=None):
        self.name = name
        self.number = number if number is not None else ""

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def set_number(self, new_number):
        self.number = new_number

    def __str__(self):
        return f"{self.name} {self.number}"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.number == other.number
        return False


# ContactList class handles a list of Person objects and file operations.
class ContactList:
    def __init__(self, file_name):
        self.contacts = []
        self.file_name = file_name
        self.load_data(file_name)

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:  # ignore empty lines
                        parts = line.split()
                        name = parts[0]
                        number = " ".join(parts[1:])  # Handles numbers with spaces or dashes
                        self.contacts.append(Person(name, number))
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Starting with an empty contact list.")

    def get_contacts(self):
        return "\n".join(str(contact) for contact in self.contacts)

    def add(self, name, number):
        self.contacts.append(Person(name, number))

    def find_person(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.get_name() == name:
                return i
        return -1

    def remove_person(self, name):
        index = self.find_person(name)
        if index != -1:
            removed_contact = self.contacts.pop(index)
            return removed_contact.get_number()
        return None

    def add_or_change_contact(self, name, number):
        index = self.find_person(name)
        if index != -1:
            self.contacts[index].set_number(number)
        else:
            self.add(name, number)

    def save(self):
        with open(self.file_name, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.get_name()} {contact.get_number()}\n")


# CLUser class provides the command-line user interface.
class CLUser:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def display_menu(self):
        print("\nContact List Management System")
        print("1. Add/Change Contact")
        print("2. Look Up Contact")
        print("3. Remove Contact")
        print("4. Save Directory")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.add_or_change_contact()
            elif choice == '2':
                self.lookup_contact()
            elif choice == '3':
                self.remove_contact()
            elif choice == '4':
                self.save_directory()
            elif choice == '5':
                self.save_directory()  # Save before exiting
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_or_change_contact(self):
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        self.contact_list.add_or_change_contact(name, number)
        print("Contact updated.")

    def lookup_contact(self):
        name = input("Enter contact name to look up: ")
        index = self.contact_list.find_person(name)
        if index != -1:
            contact = self.contact_list.contacts[index]
            print(f"Contact found: {contact.get_name()} - {contact.get_number()}")
        else:
            print("Contact not found.")

    def remove_contact(self):
        name = input("Enter contact name to remove: ")
        removed_number = self.contact_list.remove_person(name)
        if removed_number is not None:
            print(f"Contact '{name}' removed successfully.")
        else:
            print("Contact not found.")

    def save_directory(self):
        self.contact_list.save()
        print("Directory saved.")


# main function to run the application
def main():
    file_name = "phonedata.txt"  # This file should exist or will be created if not found.
    contact_list = ContactList(file_name)
    user_interface = CLUser(contact_list)
    user_interface.run()


if __name__ == "__main__":
    main()
