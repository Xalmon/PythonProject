from datetime import datetime, timedelta


def get_user_input():
    while True:
        try:
            cycle_start = input("Enter the date your last period started (MM/DD): ")
            cycle_length = int(input("How many days does your period usually last? "))

            datetime.strptime(cycle_start, "%m/%d")

            if cycle_length < 0:
                raise ValueError("Cycle length cannot be negative.")

            return cycle_start, cycle_length

        except ValueError as e:
            print(f"Invalid input: {e}. Please check your input format and try again.")
            continue


def calculate_menstrual_cycle():
    cycle_start, cycle_length = get_user_input()

    cycle_start_date = datetime.strptime(cycle_start, "%m/%d")

    period_start = cycle_start_date
    ovulation_date = cycle_start_date + timedelta(days=(cycle_length // 2))

    if cycle_start_date.day + cycle_length > 28:
        period_start = cycle_start_date.replace(month=cycle_start_date.month + 1,
                                                day=(cycle_start_date.day + cycle_length) % 28)

    safe_start = period_start - timedelta(days=18)
    safe_end = period_start - timedelta(days=11)

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
