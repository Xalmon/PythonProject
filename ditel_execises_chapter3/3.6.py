print("What is your problem?: ")
user = input()

print("Have you had this problem before (yes or no)?")
user = input()

if user.lower() == "yes":
    print("Well, you have it again.")
elif user.lower() == "no":
    print("Well, you have it now.")
