def calculate_change(purchase_price):
    change = 100 - purchase_price

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    return quarters, dimes, nickels, pennies


def main():
    purchase_price = float(input("Enter the purchase price (in dollars or less): "))

    if purchase_price > 1:
        print("Purchase price should be a dollar or less.")
        return

    quarters, dimes, nickels, pennies = calculate_change(purchase_price)

    print("Your change is:")
    if quarters > 0:
        print(f"{quarters} quarter(s)")
    if dimes > 0:
        print(f"{dimes} dime(s)")
    if nickels > 0:
        print(f"{nickels} nickel(s)")
    if pennies > 0:
        print(f"{pennies} pennie(s)")


if __name__ == "__main__":
    main()
