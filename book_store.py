store_addresses = ["Kecioren, Tunali Hilmi St., No:45, Ankara, Turkey",
                   "Cankaya, Ataturk Blvd., No:120, Ankara, Turkey"]
books = []
books_by_George_Orwell = []

class Book:
    def __init__(self, title, author, publisher, pages, isbn, price, copies):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.isbn = isbn
        self.price = price
        self.copies = copies
    
    @staticmethod
    def list_store_addresses():
        print("\nOur store addresses are:")
        for address in store_addresses:
            print("-", address)

    def display_info(self):
        return f"'{self.title}' by {self.author}, published by {self.publisher}, has {self.pages} pages, ISBN: {self.isbn}, priced at ${self.price:.2f}, Copies available: {self.copies}"
    
    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            print(f"'{self.title}' is out of stock!")
            return False
        
    def sell_copy(self):
        if self.in_stock():
            self.copies -= 1
            message = f"One copy of '{self.title}' sold. Copies left: {self.copies}"
        else:
            message = f"'{self.title}' is out of stock."
        # Ensure feedback is visible even if the caller doesn't print the return value
        print(message)
        return message
    
    @property
    def book_price(self):
        return self.price

    @book_price.setter
    def book_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price
        message = f"The price of '{self.title}' has been updated to ${self.price:.2f}"
        # Property setter return values are ignored; print to provide immediate feedback
        print(message)
        return message
    

if __name__ == '__main__':
    Book.list_store_addresses()
    
    book1 = Book("1984", "George Orwell", "Secker & Warburg", 328, "978-0451524935", 9.99, 12)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", 281, "978-0061120084", 7.99, 0)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", 180, "978-0743273565", 10.99, 5)
    book4 = Book("Animal Farm", "George Orwell", "Secker & Warburg", 112, "978-0451526340", 6.99, 4)

    books.append(book1)
    books.append(book2)
    books.append(book3)
    books.append(book4)

    books_by_George_Orwell.append(book1)
    books_by_George_Orwell.append(book4)

    print("\n")

    print("Bookstore inventory:")
    for book in books:
        print(book.display_info())
    print("\n")

    print("Selling copies...")
    book1.sell_copy()
    book2.sell_copy()
    book1.book_price = 12.99
    book2.book_price = 8.99
    print("\n")

    print("After selling copies:")
    for book in books:
        print(book.display_info())
    print("\n")