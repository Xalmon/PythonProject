def palindrome(x: str):
    if x == x[::-1]:
        return True
    else:
        return False


def palindrome2(x: str):
    if x[::-1] == x:
        return x


print(palindrome("baa"))
print(palindrome2("Hello"))
