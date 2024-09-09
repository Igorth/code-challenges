class User:
    def __init__(self, name):
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.is_available():
            book.borrow_book()
            self.books_borrowed.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.get_book_info()} is not available")

    def return_book(self, book):
        if book in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title} borrowed")
