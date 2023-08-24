class Point:

    def plant(self):
        pass

    def draw(self):
        print("drawing...")

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def drawer(self):
        print(f"drawing from point {self.a} to {self.b}")

    def __dir__(self):
        return f"({self.a}, {self.b})"


p1 = Point(1, 2)
p2 = Point(5, 6)
p1.draw()

print(type(True))
print(type(int))
print(type(4.6))
print(type(13))
print(type(bool))
print(type([]))
print(type({}))
print(type("baby"))
print(type(()))
print(type(p1))
print(isinstance(Point, object))



