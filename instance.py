# Basic class
class Book():
    def __init__(self, title, author, pages, price):
        self.title = title  # self = this
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "Secret"

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount  # Method is intended only for that class


# Instance
b1 = Book("War and Peace",  "Leo Tolstoy", 900, 1000)

# Print the class and property
print(b1)
b1.setdiscount(0.25)
print(b1.getPrice())

# properties with double underscores are hidden by the interpreter
print(b1._Book__secret)
