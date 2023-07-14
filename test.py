# print(f"""**********************************************************************
#             aso rock secondary school
# ************************************************************************
# """)
#
# for x in range(10):
#     if x == 5:
#         print(x * 2)
#         continue
#     print(x)
# for idx, x in enumerate("ace-clan"):
#     print(idx, x)

for a in range(10):
    for b in range(a + 1):
        print("*", end=" ")
    for b in range(10 - a):
        print(" ", end=" ")
    for b in range(10 - a):
        print("*", end=" ")
    for b in range(a + 1):
        print(" ", end=" ")
    print(" ")
