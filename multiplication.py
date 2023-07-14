# for a in range(1, 13):
#     for b in range(1, 13):
#         print(b, 'x', a, '=', b * a, end="\t\t\t\t")
#     print("\n")
def multiplication_table(number):
    number = int(input("enter a number: "))


for x in range(1, 21):
    print('\t')
    for y in range(1, 21):
        print("%i * %i = %-4i" % (y, x, (y * x)), end="\t\t")
        # print(f"{x} x {y} = {x * y}", end="\t\t\t")
