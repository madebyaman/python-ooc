# Basic class
class Book():
    def __init__(self, title):
        self.title = title  # self = this


# Instance
b1 = Book("War and Peace")

# Print the class and property
print(b1)
print(b1.title)
