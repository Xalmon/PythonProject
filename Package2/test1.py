x = "twinkle twinkle little star"
x1 = "How i wonder what you are!"
y = "up above the world so high,"
y1 = "Like a diamond in the sky."

print(x)
print("\t", x1)
print("\t \t", y)
print("\t\t\t", y1)
print(x)
print("\t", x1)


def print_lyric_line(line, indent_level):
    indentation = "\t" * indent_level
    print(f"{indentation}{line}")


def print_twinkle_lyrics():
    x = "twinkle twinkle little star"
    x1 = "How i wonder what you are!"
    y = "up above the world so high,"
    y1 = "Like a diamond in the sky."

    print_lyric_line(x, 0)
    print_lyric_line(x1, 1)
    print_lyric_line(y, 2)
    print_lyric_line(y1, 3)
    print_lyric_line(x, 0)
    print_lyric_line(x1, 1)



print_twinkle_lyrics()
