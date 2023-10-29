from cmd_helper import AddressBook, Record

def main():
    book = AddressBook()

    while True:
        command = input("Enter a command (add, find, delete, exit): ")
        if command == "add":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            try:
                record = book.find(name)
                if record:
                    record.add_phone(phone)
                else:
                    record = Record(name)
                    record.add_phone(phone)
                book.add_record(record)
                print("Contact added.")
            except ValueError as e:
                print(e)
        elif command == "find":
            name = input("Enter name: ")
            record = book.find(name)
            if record:
                print(record)
            else:
                print("Contact not found.")
        elif command == "delete":
            name = input("Enter name: ")
            book.delete(name)
            print("Contact deleted.")
        elif command == "exit":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
