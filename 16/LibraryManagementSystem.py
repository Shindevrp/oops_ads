class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available
    
    def getTitle(self):
        # for Book in self.book:
        #     print(Book.title)
        return self.title
    def isAvailable(self):
        # for Book in self.book:
        #     if Book.available==available:
        return self.available

class Library:
    def __init__(self) -> None:
        self.book=[]

    def addBook(self,book):
        self.book.append(book)
    def removeBook(self,isbn):
        # common_book=[]
        for Book in self.book:
            if Book.isbn==isbn:
                self.book.remove(Book)
                return True
        return False
        #     if Book.isbn!=isbn:
        # #         common_book.append(isbn)
        # # self.book=common_book



    def searchBookByTitle(self,title):
        for Book in self.book:
            if Book.title==title:
                return Book
            else:
                return None
        
    def listAllBooks(self):
        return self.book

        