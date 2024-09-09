from library_oop.library import Library


# Create a library instance and add books and users
library = Library()

# Add some books to the library
library.add_book("The Great Wall", "Scott Main")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

# Add users
library.add_user("Igor")
library.add_user("Laisa")

# Borrow books
library.borrow_book("Igor", "The Great Wall")
library.borrow_book("Laisa", "To Kill a Mockingbird")

# Try borrowing an already borrowed book
library.borrow_book("Igor", "To Kill a Mockingbird")

# List available books
library.list_all_available_books()

# Return books
library.return_book("Igor", "The Great Wall")

# List available books
library.list_all_available_books()

# Try returning a book not borrowed
library.return_book("Laisa", "1984")
