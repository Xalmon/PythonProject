print("Enter your total amount: ")
Dollar = int(input())
if Dollar == 1:
    print(f"""
    your change is:
    2 quarters
    2 dimes
    3 pennies
    """)
else:
    print('insufficient funds')
