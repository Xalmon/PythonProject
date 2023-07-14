counter = 1
total = 0
students = 0
for counter in range(20):
    students = int(input("Enter student score: "))
    total = total + students
    counter += 1
print(f"""
*************************************************************************
            Aso Rock, Secondary School, Abuja Nigeria
*************************************************************************
Number of Student in class:  {students}
Total score:  {total}
average = {2400 / total}
*************************************************************************""")
