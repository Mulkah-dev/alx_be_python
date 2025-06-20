class Book:
    total_books = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author
        #return f"{self.name} by {self.author}"
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        return f"Total number of books: {cls.total_books}"

book1 = Book("Show up", "Naima Roberts")
book2 = Book("Enjoy your life", "Muhammed Al-Arifi")
print(Book.display_total_books())
