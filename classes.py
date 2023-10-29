from collections import UserDict

class PhoneValueError(Exception):
    pass

class PhoneNotFindError(Exception):
    pass

class RecordNotFindError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value
   

class Phone(Field):
    PHONE_LEN = 10
    
    def __init__(self, value):
        if not len(value) == Phone.PHONE_LEN and not value.isdigit():
            raise PhoneValueError
        self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        find_phone = False
        for p in self.phones:
            if p.value == phone:
                find_phone = True
                phone_to_remove = p
        if find_phone:
            self.phones.remove(phone_to_remove)
        else:
            raise PhoneNotFindError
    
    def edit_phone(self, phone, phone_new):
        if len(phone_new) != Phone.MAX_PHONE_LEN:
            raise PhoneValueError
        else:
            for p in self.phones:
                if p.value == phone:
                    p.value = phone_new

    def find_phone(self, phone):
        res = None
        for p in self.phones:
            if p.value == phone:
                res = phone
        return res

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = UserDict()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        res = self.data.get(name)
        if res == None:
            raise RecordNotFindError
        else:
            return res
        
    def delete(self, name):
        if self.data.get(name) == None:
            raise RecordNotFindError
        else:
            self.data.pop(name)
