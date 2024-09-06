books = {
    "Prince": {
        "Author": "George Orwell",
        "Year": 1943,
        "Genre": "Dystopian Fiction",
        "available": True,
    },
    "Goth": {
        "Author": "Mark Twain",
        "Year": 1847,
        "Genre": "Fiction",
        "available": True,
    },
    "Sandman": {
        "Author": "Dan Brown",
        "Year": 1951,
        "Genre": "Fantasy",
        "available": True,
    }
}


def add_new_book(title: str, author: str, year: str, genre: str, available: bool) -> None:
    if title in books:
        print(f"The new book is already in the library")
    else:
        books[title] = {
            "Author": author,
            "Year": year,
            "Genre": genre,
            "available": available,
        }
        print(f"The new book '{title}' has been added to the library")


def update_book(title: str, author: str, year: str, genre: str, available: bool) -> None:
    if title not in books:
        print(f"The book {title} does not exist in the library")
    else:
        books[title] = {
            "Author": author,
            "Year": year,
            "Genre": genre,
            "available": available,
        }
        print(f"The book '{title}' has been updated in the library")


def check_available(title:str):
    if title not in books:
        print(f"The book '{title}' does not exist in the library")
        return
    else:
        if books[title]["available"]:
            print(f"The book '{title}' is available")
        else:
            print(f"The book '{title}' is not available")


def list_all_books():
    if not books:
        print(f"The library is empty")
        return
    else:
        for title, detail in books.items():
            print(f"{title}: {detail}")


# update_book("Sandman", "York", "2003", "Fantasy", True)
# check_available("Sandman")

list_all_books()
