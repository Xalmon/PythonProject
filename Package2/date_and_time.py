import datetime


def date_time():
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()

    print("Current date:", current_date)
    print("Current time:", current_time)


date_time()
