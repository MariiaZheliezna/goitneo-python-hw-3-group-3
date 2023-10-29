from collections import UserDict
import re
import datetime
import pickle
import bd_7d

class PhoneValueError(Exception):
    pass

class PhoneNotFindError(Exception):
    pass

class RecordNotFindError(Exception):
    pass

class DateError(Exception):
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
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.birthday = birthday
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
        if len(phone_new) != Phone.PHONE_LEN:
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

    def save(self):
        with open('addressbook.dat', 'wb') as fh:
            pickle.dump(self, fh)

    def read(self):
        with open('addressbook.dat', 'rb') as fh:
            return pickle.load(fh)
        
    def get_birthdays_per_week(self):
        blist = []
        for name, rec in self.data.items():
            if rec.birthday:
                blist.append({'name' : name, 'birthday' : rec.birthday.birthday})
        #print('>>>',blist)
        return bd_7d.get_birthdays_per_week(blist)

class Birthday:
    def __init__(self, birthday=None):
        self.birthday = birthday

    def add_birthday(self, date):
        result = re.findall(r"\d\d.\d\d.\d\d\d\d", date)
        if not result:
            raise DateError
        else:
            self.birthday = datetime.datetime(year=int(date[6:10]), month=int(date[3:5]), day=int(date[0:2]))
    
    def __str__(self) -> str:
        return 'No Data' if self.birthday == None else self.birthday.strftime('%d.%m.%Y')