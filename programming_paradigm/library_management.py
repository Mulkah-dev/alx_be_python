class Book:
    def __init__(self,title,author,_is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def get_checked_out(self):
        return self._is_checked_out
    
    def set_checked_out(self, value):
        self._is_checked_out = value

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        #print(f"{book.title} has been added")
    
    def check_out_book(self,title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book.get_checked_out():
                    book.set_checked_out(True)
                    #print(f"{book.title} checked out successfully")
                else:
                    print(f"{book.title} is already checked out")
                    break
        if not found:
            print(f"{title} not found in the library")

    def return_book(self,title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.get_checked_out():
                    book.set_checked_out(False)
                    #print(f"{title} has been returned successfully")
                else:
                    print(f"{title} was never checked out")
        if not found:
            print(f"{book.title} not found")

    def list_available_books(self):
        found = False
        for book in self._books:
            if not book.get_checked_out():    
                print(f"{book.title} by {book.author}")
                found = True
        if not found:
            print(f"No books are currently available")