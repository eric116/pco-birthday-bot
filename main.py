import pypco
from datetime import datetime, timedelta, date
import date_comp as dc
import credentials as cred
import mailer

today = datetime.today().strftime('%m-%d-%Y')

pco = pypco.PCO(cred.pco_app_id, cred.pco_secret)

params = {
    'where[child]': 'true',
    'where[active]': 'true'
}

this_week_bdays = {}

def main():
    for person in pco.iterate('/people/v2/people', **params):
        child_name = person['data']['attributes']['name']
        child_birthdate = person['data']['attributes']['birthdate']
        #add child and birthdate to list if the birthdate is filled out, otherwise pass go and collect $0
        if child_birthdate is None:
            pass
        else:
            child_birthdate = datetime.date(datetime.strptime(child_birthdate, '%Y-%m-%d'))
            if date.today() <= child_birthdate.replace(year=datetime.today().year) <= date.today() + timedelta(days=7):
                this_week_bdays.update({child_name: child_birthdate})
            else:
                pass
    for child_name, child_birthdate in this_week_bdays.items():
        print(child_name, child_birthdate)

def body_builder_catch(this_week_bdays):
    bday_catch = []
    this_week_bdays = {child_name: child_birthdate for child_name, child_birthdate in sorted(this_week_bdays.items(), key=lambda item: item[1])}
    for child_name, child_birthdate in this_week_bdays.items():
        birthday = datetime.strftime(child_birthdate, '%B %d')
        bday_catch.append(f"{child_name}'s birthday is {birthday}\n")
    bday_str = "".join(bday_catch)
    return bday_str

def body_assemble():
    if len(this_week_bdays) > 0:
        body = f'Hi {cred.receiver_name},\n\nHere\'s your list of kiddos with a birthday in the next week:\n\n{formattedBirthdays}\n\nHope you have an amazing day!'
    else:
        body = f'Hi {cred.receiver_name},\n\nNo birthday reminders this week :)'
    return body

main()
formattedBirthdays = body_builder_catch(this_week_bdays)
body = body_assemble()
subject = f'Weekly Birthday Report ({today})'
mailer.send_email(subject, body)