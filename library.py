from fileio import FileCSV

class Library:
    filename = "books.csv"

    def __init__(self):
        self.books = FileCSV(self.filename).read_dict()

    def popular_books(self):
        i = 0
        for book in self.books:
            if i<10:
                print(book)
            i += 1

    def get_book(self, bookId):
        print("get book: " + bookId)

    def return_book(self, bookId):
        print("return book: " + bookId)

    def __del__(self):
        print("del Library")
        