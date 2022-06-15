from application.people import get_employees
from application.salary import calculate_salary
import datetime


def main():
    while True:
        user = input('insert command: ')
        if user == 's':
            calculate_salary()
            print(datetime.datetime.today())
        elif user == 'p':
            get_employees()
            print(datetime.datetime.today())


if __name__ == '__main__':
    main()