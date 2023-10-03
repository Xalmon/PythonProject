from datetime import datetime, timedelta


def get_user_input():
    try:
        cycle_start = input("Enter the date your last period started (MM-DD): ")
        cycle_length = int(input("How many days does your period usually last? "))
        return cycle_start, cycle_length
    except ValueError:
        print("Something went wrong. Please check your input format and try again.")
        return get_user_input()


def calculate_menstrual_cycle():
    cycle_start, cycle_length = get_user_input()

    cycle_start_date = datetime.strptime(cycle_start, "%m-%d")

    period_start = cycle_start_date
    ovulation_date = cycle_start_date + timedelta(days=(cycle_length // 2))
    safe_start = cycle_start_date + timedelta(days=(cycle_length - 18))
    safe_end = cycle_start_date + timedelta(days=(cycle_length - 11))

    print("Below are various information about your cycle")
    print(f"Your next period will start around {period_start.strftime('%B')} {period_start.day}.")
    print(f"You'll be most fertile around {ovulation_date.strftime('%B')} {ovulation_date.day}.")
    print(
        f"Your safe days are from {safe_start.strftime('%B')} {safe_start.day} to {safe_end.strftime('%B')} {safe_end.day}.")


def main():
    calculate_menstrual_cycle()
    another_cycle = input("Do you want to calculate another cycle? (yes/no): ").lower()
    if another_cycle == "yes":
        main()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
