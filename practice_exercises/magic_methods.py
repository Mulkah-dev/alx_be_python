class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        #print(f"{self.title} by {self.author} has {self.pages} pages")

    def __str__(self):
       return f"Book is {self.title}"
    
    def __repr__(self):
       return f"Book is {self.title}"

book1 = Book("The gods ar to be blamed", "Chinua Achebe", 100)
print(book1)
print(repr(book1))