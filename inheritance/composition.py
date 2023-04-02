"""
Inheritance model: A Magazine is subclass of Periodical which is further a subclass for Publication.
Composition Model: Book class has
"""


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for chapter in self.chapters:
            result += chapter.pagecount
        return result


class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 11, author)

b1.addchapter(Chapter("Chapter 1", 120))
b1.addchapter(Chapter("Chapter 2", 80))

print(b1.author)
print(b1.getbookpagecount())
