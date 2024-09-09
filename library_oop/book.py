class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def get_book_info(self):
        return f"'{self.title}' by {self.author}"

    def is_available(self):
        return self.available

    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True
