import datetime
from my_package.people import *
from my_package.salary import *


if __name__ == '__main__':
    print(datetime.date.today())
    calculate_salary()
    get_employees()