class Book:
    # properties defined at class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK", "AUDIOBOOK")

    __booklist = None

    # static method: they don't modify the state
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    def setTitle(self, newTitle):
        self.title = newTitle

    # class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    def __init__(self, title, booktype) -> None:
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# print("Book types: ", Book.getbooktypes())
b1 = Book("War and Peace", "HARDCOVER")

# static methods
books = Book.getbooklist()
books.append(b1)
print(books)
