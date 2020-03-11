import random
import datetime
# from registration.models import BirthRegistration


def birth_cert_number(start_number):
    start_serial = 'KBRT'
    end_serial = datetime.date.today().strftime("%d%m%Y")
    cert_number = start_serial + str(start_number) + str(end_serial)
    return cert_number


# a = birth_cert_number(3)
# print(a)


def death_cert_number(start_number):
    start_serial = 'KDRT'
    end_serial = datetime.date.today().strftime("%d%m%Y")
    cert_number = start_serial + str(start_number) + str(end_serial)
    return cert_number.capitalize()


def increment_cert_number(previous_cert_number):
    cert_number = previous_cert_number[4:-8]
    the_cert_number = int(cert_number)
    return the_cert_number + 1


# b = increment_cert_number('KBRT308102019')
# print(b)

