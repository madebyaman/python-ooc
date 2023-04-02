# Basic class
class Book():
    def __init__(self, title):
        self.title = title  # self = this


class Newspaper:
    def __init__(self, name):
        self.name = name


# Instance
b1 = Book("War and Peace")
b2 = Book("Journey to End of Earth")
n1 = Newspaper("Indian Express")

# use type() to inspect the object type
# print(type(b1) == type(b2))

# Use isInstacne to compare a specific instance to a known type
# print(isinstance(n1, Book))
print(isinstance(n1, object))
