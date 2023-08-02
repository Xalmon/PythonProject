dictionary = {
    "name": "grace",
    "age": 21,
    "height": 5.3
}
print(type(dictionary))
print(dictionary)

user = [
    {
        "name": "Titanium",
        "age": 21,
        "height": 5.3,
        "hobbies": "shopping"
    },
    {
        "name": "Grace",
        "age": 20,
        "height": 5.3,
        "hobbies": "shopping, things"
    },
    {
        "name": "Chivied",
        "age": 18,
        "height": 5.6,
        "hobbies": "shipping"
    }
]

user[0]["name"] = "kattie"
user[0]["gender"] = "female"
print(user[0])
print(user)

book = {
    "title": "The tortoise and the snail",
    "author": "Tom",
    "isbn": 121211222,
    "price": 500
}

print("title" in book.keys())
print("tom" in book.values())
print("i" in "hi")
for key, value in book.items():
    print("title" in book.keys())
    for value in book.values():
        print(value)
        for value in book.keys():
            ()

