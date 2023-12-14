from fileio import FileCSV

class Library:
    filename = "books.csv"

    essential_keys = {"bookID", "title" , "average_rating", "num_pages"} 

    def __init__(self):
        self.books = FileCSV(self.filename).read_dict()
        self.books = list(map(self.__filter_book, self.books))
        print(self.books[:3])

    
    def __filter_book(self, book):
        filtered = dict(filter(lambda item: True if item[0] in self.essential_keys else False, book.items()))
        try:
            filtered["average_rating"] = float(filtered["average_rating"])
        except ValueError:
            filtered["average_rating"] = 0
        try:
            filtered["num_pages"] = int(filtered["num_pages"])
        except ValueError:
            filtered["num_pages"] = 100
        return filtered
    
    def popular_books(self):
        books = self.books.copy()
        books.sort(reverse=True, key=lambda x: x["average_rating"])
        print(books[:3])

    def get_book(self, bookId):
        print("get book: " + bookId)

    def return_book(self, bookId):
        print("return book: " + bookId)

    def __del__(self):
        print("del Library")
        