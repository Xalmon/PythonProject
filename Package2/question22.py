def celsius_from_fahrenheit(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    try:
        fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
        celsius = celsius_from_fahrenheit(fahrenheit)
        print("Temperature in Celsius:", celsius)
    except ValueError:
        print("Invalid input. Please enter a valid numerical temperature.")


if __name__ == "__main__":
    main()
