from library_oop.book import Book
from library_oop.user import User


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def list_all_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if available_books:
            print("Available books: ")
            for book in available_books:
                print(f"- {book.get_book_info()}")
        else:
            print("No available books in the library.")

    def add_user(self, username):
        user = User(username)
        self.users.append(user)
        print(f"User '{username}' added to the library.")

    def get_user(self, username):
        for user in self.users:
            if user.name == username:
                return user
        return None

    def borrow_book(self, username, book_title):
        user = self.get_user(username)
        if user:
            for book in self.books:
                if book.title == book_title:
                    user.borrow_book(book)
                    return
            print(f"The book '{book_title}' is not found in the library.")
        else:
            print(f"User '{username}' not found in the library.")

    def return_book(self, username, book_title):
        user = self.get_user(username)
        if user:
            for book in self.books:
                if book.title == book_title:
                    user.return_book(book)
                    return
            print(f"The book '{book_title}' is not found in the library.")
        else:
            print(f"User '{username}' not found in the library.")