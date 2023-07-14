# import char as char
# for x in range(1, 8):
#     print([' ' ' ' ' ', (char) *, ' ' ' ' ' '])
# 0 = [' ']
# 1 = [*]
#

print("' '' '' ''*'' '' '' '")
print("' '' ''*''*''*'' '' '")
print("' ''*''*''*''*''*'' '")
print("'*''*''*''*''*''*''*'")
print("' '' '' ''*'' '' '' '")
print("' '' '' ''*'' '' '' '")
print("' '' '' ''*'' '' '' '")
print("' '' '' ''*'' '' '' '")


print(f""" 
' '' '' ''*'' '' '' '
' '' ''*''*''*'' '' '
' ''*''*''*''*''*'' '
'*''*''*''*''*''*''*'
' '' '' ''*'' '' '' '
' '' '' ''*'' '' '' '
' '' '' ''*'' '' '' '
' '' '' ''*'' '' '' '""")

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
# picture.insert(1, "*")
# for i in range(0, len(picture)):
#     print(picture[i])
# for row in picture:
#     x == *
#     for x in row:
#         print(picture[x])

# for row in picture:
#     for x in row:
#         print(x)
#     for v in row:
#         print(v)
#     if x == 1 and v == 0:
#         print(str(picture)
# int [][]picture ={
#
#
#
# }
# for a in range(10):
#     for b in range(a + 1):
#         print(" ", end="*")
#     for b in range(10 - a):
#         print(" ", end=" ")
#     print(" ")
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end= '')
        elif pixel == 1:
            print('*', end= '')
    print()
numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]