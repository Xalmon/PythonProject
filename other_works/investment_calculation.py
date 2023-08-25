def calculate_investment(principal, rate_of_return, years):
    amount = principal * (1 + rate_of_return / 100) ** years
    return amount


principal = 1000
rate_of_return = 7
years_list = [10, 20, 30]

for years in years_list:
    amount = calculate_investment(principal, rate_of_return, years)
    print(f"After {years} years, you'll have ${amount:.2f}")
