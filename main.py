from classes import *




def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# додаємо контакт
def add_contact(book:AddressBook, args:list):
    if len(args) == 2 and len(args[0]) > 0:
        try:
            if args[0] in book.data:
                rec = book.data[args[0]]
                rec.add_phone(args[1])
            else:
                rec = Record(args[0])
                rec.add_phone(args[1])
                book.add_record(rec)
            print("Contact added sucessfully")
        except PhoneValueError:
            print("Error: Phone must be 10 digits")
    else:
        print("Invalid command")

# показуємо всі контакти.
def show_all(book:AddressBook):
    # print(book, "\n")
    for name, record in book.data.items():
        print(record)

#змінюємо контакт
def change_contact(book:AddressBook, args:list):
    if len(args) == 3 and len(args[0]) > 0:
        try:
            record = book.find(args[0])
            record.edit_phone(args[1], args[2])
            print("Contact phone number has been changed")
        except PhoneValueError:
            print("Error: New phone must be 10 digits")
        except RecordNotFindError:
            print("Name was not found")
    else:
        print("Invalid command")

#Показати телефонний номер для вказаного контакту
def show_phone(book:AddressBook, args:list):
    if len(args) == 1 and len(args[0]) > 0:
        if args[0] in book.data:
            print(book.data[args[0]])
        else:
            print("Name was not found")
    else:
        print("Invalid command")

#Додати дату народження для вказаного контакту
def add_birthday(book:AddressBook, args:list):
    if len(args) == 2 and len(args[0]) > 0:
        if args[0] in book.data:
            try:
                birthday=Birthday()
                birthday.add_birthday(args[1])
                book.data[args[0]].birthday = birthday
                print("Birthday added")
            except DateError:
                print("Invalid date")
        else:
            print("Name was not found")
    else:
        print("Invalid command")

#Показати дату народження для вказаного контакту
def show_birthday(book:AddressBook, args:list):
    if len(args) == 1 and len(args[0]) > 0:
        if args[0] in book.data:
            if book.data[args[0]].birthday:
                b_day = book.data[args[0]].birthday
                print(b_day)
            else:
                print("There is no birthday for this contact")
        else:
            print("Name was not found")
    else:
        print("Invalid command")


def main():
    print("Welcome to the assistant bot!")
    try:
        book = AddressBook().read()
    except:
        book = AddressBook()

    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                # выход, тут сохраняем AdressBook
                book.save()
                print("Good bye!")
                break
            
            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                add_contact(book, args)      

            elif command == "all":
                show_all(book)

            elif command == "change":
                change_contact(book, args)
            
            elif command == "phone":
                show_phone(book,args)

            elif command == "add-birthday":
                add_birthday(book, args)

            elif command == "show-birthday":
                show_birthday(book, args)

            elif command == "birthdays":
                print(book.get_birthdays_per_week())

            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()