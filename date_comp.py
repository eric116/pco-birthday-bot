from datetime import datetime, timedelta, date

today = datetime.today()
this_week_bdays = {}

def evalBirthday(child_name, child_birthdate):
    if child_birthdate <= date.today() + timedelta(days=7) and child_birthdate >= date.today():
        this_week_bdays.update({child_name: child_birthdate})
    else:
        pass

def body_builder_catch(dict_of_bdays):
    bday_catch = []
    for name, bday in dict_of_bdays.items():
        birthday = datetime.strftime(bday, '%y-%m-%d')
        bday_catch.append(f"Reminder: {name}'s birthday is {birthday}\n")
    bday_str = "".join(bday_catch)
    return bday_str