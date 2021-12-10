from person import Person
import smtplib, ssl
from typing import List
from copy import deepcopy
import random
from people_parser import PeopleParser

port = 587
smtp_server = "smtp.gmail.com"
sender_email = input("Type your email address and press enter:")
password = input("Type your password and press enter:")

parser = PeopleParser('peopleList.csv')
people: List[Person] = parser.parse_people()
people_basket = deepcopy(people)

isPeopleConflict = True

while isPeopleConflict:
    random.shuffle(people_basket)

    isPeopleConflict = False
    for ind, personChecked in enumerate(people):
        if personChecked == people_basket[ind]:
            isPeopleConflict = True
            break

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    for ind, personNotified in enumerate(people):
        receiver_email = personNotified.email
        message = 'Hey {}. You have {} for secret santa. \nLimit - 100$\nPowodzenia'\
            .format(personNotified.name, people_basket[ind].name)
        server.sendmail(sender_email, receiver_email, message)
