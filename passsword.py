# Password = input("Enter Your Password: ")
# my_password = len(Password)
# while my_password < 8:
#     print("your password is too short", my_password)
#     if my_password >= 8:
#     my_password += 1
#     print("your password is secure, the length is: ", my_password)
password = input("Enter Your Password: ")
my_password = len(password)
while my_password <= 8:
    my_password = int(input("Password is too Short, Enter a new password: "))
print("your password is secure, the length is: {pass_chars}".format(pass_chars='*' * my_password))