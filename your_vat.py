def calculate_vat_inclusive_price():
    while True:
        try:
            item_price = float(input("Enter item amount: "))
            vat_rate = float(input("Enter VAT rate: "))

            if item_price < 0 or vat_rate < 0:
                print("Please make sure both price and VAT rate are positive.")
            else:
                vat_inclusive_price = item_price + (item_price * vat_rate / 100)
                return vat_inclusive_price
        except ValueError:
            print("Oops! That doesn't look like valid numbers.")


price = calculate_vat_inclusive_price()
print("Total price and VAT inclusive:", price)
