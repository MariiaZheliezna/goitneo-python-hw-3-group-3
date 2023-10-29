# Домашнє завдання 1, завдання 1
from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Bill Gates1", "birthday": datetime(1955, 10, 20)},
    {"name": "Bill Gates2", "birthday": datetime(1955, 10, 14)},
    {"name": "Bill Gates3", "birthday": datetime(1975, 10, 15)},
    {"name": "Bill Gates4", "birthday": datetime(1985, 10, 17)},
    {"name": "Bill Gates5", "birthday": datetime(1955, 9, 1)},
    {"name": "Bill Gates6", "birthday": datetime(1995, 11, 2)},
    {"name": "Bill Gates7", "birthday": datetime(2000, 10, 21)},
    {"name": "Bill Gates8", "birthday": datetime(2001, 12, 18)},
    {"name": "Bill Gates9", "birthday": datetime(2002, 10, 22)},
]

# виводить у консоль список користувачів, яких потрібно привітати по днях на наступному тижні
def get_birthdays_per_week(users):
    current_date = datetime.today().date()
    current_year = int(datetime.today().date().strftime('%Y'))
    # print (current_date)
    workdays = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=int(datetime.now().strftime("%Y")))
        # print(birthday_this_year, current_date)
        if birthday_this_year.strftime('%A') == 'Saturday':
            birthday_this_year = birthday_this_year + timedelta(days=2)
        if birthday_this_year.strftime('%A') == 'Sunday':
            birthday_this_year = birthday_this_year + timedelta(days=1)    
        # перевірка на тиждень
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_year+1)
            #print(birthday_this_year, current_date)
        delta_days = (birthday_this_year - current_date).days
        #print (delta_days)
    
        # остаточно визначили дати святкування дней народження
        if delta_days < 7: 
            weekday = birthday_this_year.strftime('%A')
            workdays[weekday].append(user['name'])
    
    #print(workdays)
    # сортування для виводу
    weekdays_order_dict = defaultdict(list)
    for i in range(7):
        dt = current_date + timedelta(days=i)
        day = dt.strftime("%A")
        weekdays_order_dict[i] = day
    #print(weekdays_order_dict)

    # вивід результату
    for week_day_index, week_day_name in weekdays_order_dict.items():
        if workdays[week_day_name]:
            birthday_selebrate_str = ", ".join(workdays[week_day_name])
            print(f"{week_day_name:<10} : {birthday_selebrate_str}")
            


