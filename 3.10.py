total_miles = 0
total_gallons = 0
tankfuls = 0

while True:
    miles = float(input("Enter miles driven (or -1 to end): "))
    if miles == -1:
        break

    gallons = float(input("Enter gallons used: "))

    mpg = miles / gallons

    print(f"Miles per gallon for this tankful: {mpg}\n")

    total_miles += miles
    total_gallons += gallons
    tankfuls += 1

if tankfuls > 0:
    combined_mpg = total_miles / total_gallons
    print(f"Combined miles per gallon for all tankfuls: {combined_mpg}")
else:
    print("No tankfuls were entered.")
